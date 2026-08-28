import os
import json
import logging
import asyncio
from typing import Optional
from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel, Field

logger = logging.getLogger(__name__)

router = APIRouter()

class TransactionDescription(BaseModel):
    description: str

class SuggestedEntry(BaseModel):
    transaction_type: str = Field(description="One of 'Payment', 'Receipt', 'Journal', 'Contra'")
    debit_account: str
    credit_account: str
    amount: float
    narration: str
    confidence: float
    is_ambiguous: bool = False
    clarification_needed: Optional[str] = None

SYSTEM_INSTRUCTION = """You are an expert Indian Chartered Accountant and bookkeeping AI for 'Meso' (an Indian accounting platform).
Your task is to analyze plain-language transaction descriptions and output a strictly valid double-entry journal suggestion.

Follow standard Indian Accounting Principles (Golden Rules of Accounting / AS / Ind AS):
1. Rules:
   - Real Accounts: Debit what comes in, Credit what goes out (Cash/Bank/Assets).
   - Personal Accounts: Debit the receiver, Credit the giver (Customers/Vendors/Parties).
   - Nominal Accounts: Debit all expenses & losses, Credit all incomes & gains.

2. Account naming conventions:
   - Cash / Bank transactions: Use "Cash and Bank" or specific bank account.
   - Payments to individuals/parties (e.g., "Cash given to Nitin"): Debit the party (e.g., "Nitin" or "Advances to Nitin"), Credit "Cash and Bank".
   - Specific expenses (e.g., "Paid electricity bill 3000 by bank"): Debit "Electricity Expense" (or "Utility Expense"), Credit "Cash and Bank".
   - Customer receipts (e.g., "Received 5000 from Ramesh against invoice"): Debit "Cash and Bank", Credit "Ramesh" (or "Accounts Receivable - Ramesh").
   - Ambiguous / vague inputs (e.g., "office thing 500"):
     - If the description lacks sufficient details to know the actual nature of expense/party, set `is_ambiguous: true`, provide a low confidence score (< 0.60), and specify what needs clarification in `clarification_needed`.
     - Debit a best-guess account (e.g., "Office Expenses") and Credit "Cash and Bank".

3. Transaction types:
   - "Payment": Outflow of cash/bank to vendor, expense, or party.
   - "Receipt": Inflow of cash/bank from customer or income.
   - "Contra": Transfer between Cash and Bank or between Bank accounts.
   - "Journal": Non-cash adjustments, depreciation, provision, or credit purchases/sales.

Return ONLY a valid JSON object matching this schema:
{
  "transaction_type": "Payment" | "Receipt" | "Journal" | "Contra",
  "debit_account": string,
  "credit_account": string,
  "amount": number,
  "narration": string,
  "confidence": number (between 0.0 and 1.0),
  "is_ambiguous": boolean,
  "clarification_needed": string | null
}
"""

PRIMARY_MODEL = "gemini-3.6-flash"
FALLBACK_MODEL = "gemini-3.5-flash"

async def call_gemini_api(prompt: str, api_key: str) -> dict:
    """
    Calls Gemini API using curl.exe on Windows for maximum speed and zero network handshake lag.
    """
    payload = {
        "contents": [
            {
                "parts": [
                    {"text": prompt}
                ]
            }
        ],
        "systemInstruction": {
            "parts": [
                {"text": SYSTEM_INSTRUCTION}
            ]
        },
        "generationConfig": {
            "responseMimeType": "application/json",
            "temperature": 0.1
        }
    }

    payload_json = json.dumps(payload)

    for model in [PRIMARY_MODEL, FALLBACK_MODEL]:
        url = f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent?key={api_key}"
        
        proc = await asyncio.create_subprocess_exec(
            "curl.exe", "-s", "-X", "POST", url,
            "-H", "Content-Type: application/json",
            "-d", payload_json,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE
        )
        
        try:
            stdout, stderr = await asyncio.wait_for(proc.communicate(), timeout=15.0)
        except asyncio.TimeoutError:
            proc.kill()
            continue

        if not stdout:
            continue

        try:
            res_data = json.loads(stdout.decode("utf-8"))
        except Exception:
            continue

        if "error" in res_data:
            err = res_data["error"]
            code = err.get("code", 500)
            msg = err.get("message", "API Error")
            if code == 429:
                raise HTTPException(
                    status_code=status.HTTP_429_TOO_MANY_REQUESTS,
                    detail="AI classification rate limit reached — please try again or enter manually."
                )
            elif code in [400, 401, 403]:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="AI classification authentication error — please verify API key."
                )
            continue  # Try fallback model for other errors

        candidates = res_data.get("candidates", [])
        if candidates and "content" in candidates[0]:
            parts = candidates[0]["content"].get("parts", [])
            if parts and "text" in parts[0]:
                return json.loads(parts[0]["text"])

    raise HTTPException(
        status_code=status.HTTP_502_BAD_GATEWAY,
        detail="AI classification service unavailable — please enter manually."
    )

@router.post("/suggest-entry", response_model=SuggestedEntry)
async def suggest_entry(entry: TransactionDescription):
    """
    AI-Powered Manual Entry System using real Gemini API.
    Parses natural language into a suggested double-entry journal posting.
    """
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail="AI classification unavailable — GEMINI_API_KEY environment variable is not configured."
        )

    if not entry.description or not entry.description.strip():
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Transaction description cannot be empty."
        )

    prompt = f"Analyze this transaction and return the structured double-entry posting:\n\"{entry.description.strip()}\""

    try:
        parsed_json = await call_gemini_api(prompt, api_key)
        
        return SuggestedEntry(
            transaction_type=parsed_json.get("transaction_type", "Journal"),
            debit_account=parsed_json.get("debit_account", ""),
            credit_account=parsed_json.get("credit_account", ""),
            amount=float(parsed_json.get("amount", 0.0)),
            narration=parsed_json.get("narration", entry.description),
            confidence=float(parsed_json.get("confidence", 0.7)),
            is_ambiguous=bool(parsed_json.get("is_ambiguous", False)),
            clarification_needed=parsed_json.get("clarification_needed")
        )
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Unexpected error in suggest_entry: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="AI classification failed — please enter manually."
        )
