import os
import json
import logging
import asyncio
from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel

logger = logging.getLogger(__name__)

router = APIRouter()

class AuditQuery(BaseModel):
    question: str
    financial_context: dict = {}

class AuditResponse(BaseModel):
    answer: str
    scope: str  # "in_scope" or "out_of_scope"

SYSTEM_INSTRUCTION = """You are Meso AI Audit Assistant — an expert Indian Chartered Accountant and financial auditor embedded in an Indian MSME accounting platform called "Meso".

Your capabilities:
1. **Ledger Review**: Analyze ledger transactions for anomalies — duplicates, unusual amounts, missing narrations, or entries that look inconsistent with normal business operations.
2. **AS Compliance**: Check whether the books reflect proper treatment under Indian Accounting Standards (AS 1 disclosure, AS 2 inventory valuation, AS 3 cash flow, AS 9 revenue recognition, AS 10 fixed assets, AS 15 employee benefits, AS 22 deferred tax, AS 26 intangibles, AS 29 provisions).
3. **Financial Q&A**: Answer questions about the user's own financial statements — Balance Sheet, P&L, Cash Flow, Trial Balance, GST position — using the actual data provided in the context.
4. **Corrective Entries**: When asked, suggest corrective journal entries in proper double-entry format (Debit account, Credit account, Amount, Narration). Always present these as SUGGESTIONS requiring user confirmation — NEVER state that an entry has been posted or will be auto-posted.

Constraints:
- Always ground your answers in the actual financial data provided in the context. If the context doesn't contain enough information to answer, say so explicitly rather than guessing.
- If the user asks something outside your scope (weather, sports, general knowledge, coding, etc.), politely decline and redirect: "I'm your accounting audit assistant — I can help with ledger reviews, AS compliance checks, financial statement analysis, and corrective journal entries. How can I help with your books?"
- Use Indian accounting terminology and INR formatting (₹).
- Be concise and professional. Use bullet points for lists.
- When suggesting corrective entries, format them clearly as:
  • Debit: [Account Name] — ₹[Amount]
  • Credit: [Account Name] — ₹[Amount]
  • Narration: [Description]
  And always end with: "⚠️ This is a suggestion — please review and confirm before posting."

Return ONLY a valid JSON object with this schema:
{
  "answer": "Your detailed response text here",
  "scope": "in_scope" or "out_of_scope"
}
"""

PRIMARY_MODEL = "gemini-3.6-flash"
FALLBACK_MODEL = "gemini-3.5-flash"

async def call_gemini_audit(prompt: str, api_key: str) -> dict:
    """
    Calls Gemini API using curl.exe subprocess (same pattern as ai_entry.py).
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
            "temperature": 0.3
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
            stdout, stderr = await asyncio.wait_for(proc.communicate(), timeout=20.0)
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
            if code == 429:
                raise HTTPException(
                    status_code=status.HTTP_429_TOO_MANY_REQUESTS,
                    detail="AI Audit Assistant rate limit reached — please try again shortly."
                )
            elif code in [400, 401, 403]:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="AI Audit Assistant authentication error — please verify API key."
                )
            continue

        candidates = res_data.get("candidates", [])
        if candidates and "content" in candidates[0]:
            parts = candidates[0]["content"].get("parts", [])
            if parts and "text" in parts[0]:
                return json.loads(parts[0]["text"])

    raise HTTPException(
        status_code=status.HTTP_502_BAD_GATEWAY,
        detail="AI Audit Assistant unavailable — please try again."
    )


@router.post("/audit-query", response_model=AuditResponse)
async def audit_query(query: AuditQuery):
    """
    AI Audit Assistant: answers accounting questions grounded in the user's actual financial data.
    """
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail="AI Audit Assistant unavailable — GEMINI_API_KEY is not configured."
        )

    if not query.question or not query.question.strip():
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Question cannot be empty."
        )

    # Build the context-enriched prompt
    context_section = ""
    ctx = query.financial_context
    if ctx:
        context_parts = []
        if ctx.get("cashBalance") is not None:
            context_parts.append(f"Cash & Bank Balance: ₹{ctx['cashBalance']:,.0f}")
        if ctx.get("totalRevenue") is not None:
            context_parts.append(f"Total Revenue: ₹{ctx['totalRevenue']:,.0f}")
        if ctx.get("totalExpenses") is not None:
            context_parts.append(f"Total Expenses: ₹{ctx['totalExpenses']:,.0f}")
        if ctx.get("netProfit") is not None:
            context_parts.append(f"Net Profit (PAT): ₹{ctx['netProfit']:,.0f}")
        if ctx.get("accountsReceivable") is not None:
            context_parts.append(f"Accounts Receivable: ₹{ctx['accountsReceivable']:,.0f}")
        if ctx.get("accountsPayable") is not None:
            context_parts.append(f"Accounts Payable: ₹{ctx['accountsPayable']:,.0f}")
        if ctx.get("totalAssets") is not None:
            context_parts.append(f"Total Assets: ₹{ctx['totalAssets']:,.0f}")
        if ctx.get("totalEquityAndLiabilities") is not None:
            context_parts.append(f"Total Equity & Liabilities: ₹{ctx['totalEquityAndLiabilities']:,.0f}")
        if ctx.get("bsBalanced") is not None:
            context_parts.append(f"Balance Sheet Status: {'Balanced' if ctx['bsBalanced'] else 'IMBALANCED'}")
        if ctx.get("totalDebits") is not None and ctx.get("totalCredits") is not None:
            context_parts.append(f"Trial Balance — Debits: ₹{ctx['totalDebits']:,.0f}, Credits: ₹{ctx['totalCredits']:,.0f}")
        if ctx.get("transactionCount") is not None:
            context_parts.append(f"Total Ledger Entries: {ctx['transactionCount']}")
        if ctx.get("inventoryValue") is not None:
            context_parts.append(f"Inventory Valuation (FIFO): ₹{ctx['inventoryValue']:,.0f}")
        if ctx.get("invoiceCount") is not None:
            context_parts.append(f"Total Invoices: {ctx['invoiceCount']}")
        if ctx.get("recentTransactions"):
            context_parts.append(f"Recent Transactions (last 10):\n{ctx['recentTransactions']}")

        context_section = f"\n\n--- CURRENT FINANCIAL DATA ---\n" + "\n".join(context_parts) + "\n--- END FINANCIAL DATA ---\n"

    prompt = f"User question: \"{query.question.strip()}\"{context_section}"

    try:
        parsed = await call_gemini_audit(prompt, api_key)
        return AuditResponse(
            answer=parsed.get("answer", "I couldn't process that question. Please try rephrasing."),
            scope=parsed.get("scope", "in_scope")
        )
    except HTTPException:
        raise
    except Exception as e:
        import traceback
        traceback.print_exc()
        logger.error(f"Unexpected error in audit_query: {type(e).__name__}: {str(e)}", exc_info=True)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"AI Audit Assistant failed: {type(e).__name__}: {str(e)}"
        )
