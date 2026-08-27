import os
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import re

router = APIRouter()

class TransactionDescription(BaseModel):
    description: str

class SuggestedEntry(BaseModel):
    transaction_type: str
    debit_account: str
    credit_account: str
    amount: float
    narration: str
    confidence: float

@router.post("/suggest-entry", response_model=SuggestedEntry)
async def suggest_entry(entry: TransactionDescription):
    """
    AI-Powered Manual Entry System (Stub)
    Parses natural language into a suggested double-entry journal posting.
    Architected to accept a real LLM integration (like Anthropic) when the API key is provided.
    Currently uses intelligent mock responses for end-to-end pipeline testing.
    """
    api_key = os.getenv("LLM_API_KEY")
    
    # If API key is present, this is where the real LLM call would happen.
    if api_key:
        # e.g., call_anthropic(entry.description)
        pass 
    
    # --- MOCK/STUB LOGIC (Fallback when no API key) ---
    desc = entry.description.lower()
    
    # Extract amount using simple regex
    amount_match = re.search(r'\b\d+(?:,\d+)*(?:\.\d+)?\b', desc)
    amount = float(amount_match.group(0).replace(',', '')) if amount_match else 0.0
    
    # Heuristics for mock response
    if "cash given" in desc or "paid" in desc or "payment" in desc:
        return SuggestedEntry(
            transaction_type="Payment",
            debit_account="Accounts Payable", # Assuming payment to supplier by default
            credit_account="Cash and Bank",
            amount=amount,
            narration=entry.description.capitalize(),
            confidence=0.85
        )
    elif "received" in desc or "receipt" in desc:
        return SuggestedEntry(
            transaction_type="Receipt",
            debit_account="Cash and Bank",
            credit_account="Accounts Receivable",
            amount=amount,
            narration=entry.description.capitalize(),
            confidence=0.88
        )
    elif "sold" in desc or "sale" in desc:
        return SuggestedEntry(
            transaction_type="Journal",
            debit_account="Accounts Receivable",
            credit_account="Sales Revenue",
            amount=amount,
            narration=entry.description.capitalize(),
            confidence=0.92
        )
    elif "bought" in desc or "purchase" in desc:
        return SuggestedEntry(
            transaction_type="Journal",
            debit_account="Inventory",
            credit_account="Accounts Payable",
            amount=amount,
            narration=entry.description.capitalize(),
            confidence=0.90
        )
    else:
        # Default generic response
        return SuggestedEntry(
            transaction_type="Journal",
            debit_account="Miscellaneous Expense",
            credit_account="Cash and Bank",
            amount=amount,
            narration=entry.description.capitalize(),
            confidence=0.50
        )
