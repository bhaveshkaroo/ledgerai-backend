"""
LedgerAI — routes/transactions.py
Handles all transaction-related endpoints:
  • GET  /transactions/all          → return all dummy transactions
  • GET  /transactions/{id}         → return one transaction by ID
  • POST /transactions/classify     → ask Claude AI to categorise a transaction
"""

import os
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import anthropic

router = APIRouter()

# ── Dummy transaction data (10 realistic Indian MSME entries) ──────────────

TRANSACTIONS = [
    {
        "id": 1,
        "date": "2025-04-01",
        "description": "Sharma Traders — invoice payment received",
        "amount": 1_25_000.00,
        "type": "credit",
        "category": "",
    },
    {
        "id": 2,
        "date": "2025-04-03",
        "description": "Office rent for April — WeWork Andheri",
        "amount": 45_000.00,
        "type": "debit",
        "category": "",
    },
    {
        "id": 3,
        "date": "2025-04-05",
        "description": "GST payment to Government — Q4 FY25",
        "amount": 18_750.00,
        "type": "debit",
        "category": "",
    },
    {
        "id": 4,
        "date": "2025-04-07",
        "description": "Salary disbursement — staff payroll April",
        "amount": 2_10_000.00,
        "type": "debit",
        "category": "",
    },
    {
        "id": 5,
        "date": "2025-04-10",
        "description": "Patel Enterprises — consulting fee received",
        "amount": 75_000.00,
        "type": "credit",
        "category": "",
    },
    {
        "id": 6,
        "date": "2025-04-12",
        "description": "Electricity bill — MSEDCL April",
        "amount": 8_500.00,
        "type": "debit",
        "category": "",
    },
    {
        "id": 7,
        "date": "2025-04-15",
        "description": "TDS deducted on professional fees — Section 194J",
        "amount": 7_500.00,
        "type": "debit",
        "category": "",
    },
    {
        "id": 8,
        "date": "2025-04-18",
        "description": "Raw material purchase — Gupta Suppliers",
        "amount": 62_000.00,
        "type": "debit",
        "category": "",
    },
    {
        "id": 9,
        "date": "2025-04-22",
        "description": "Bank charges — HDFC Current Account maintenance",
        "amount": 1_180.00,
        "type": "debit",
        "category": "",
    },
    {
        "id": 10,
        "date": "2025-04-25",
        "description": "Mehta & Sons — product sale received",
        "amount": 1_50_000.00,
        "type": "credit",
        "category": "",
    },
]

# ── Request body schema for /classify ──────────────────────────────────────

class ClassifyRequest(BaseModel):
    description: str
    amount: float


# ── Endpoints ──────────────────────────────────────────────────────────────

@router.get("/all")
def get_all_transactions():
    """Return all ten transactions."""
    return TRANSACTIONS


@router.get("/{transaction_id}")
def get_transaction_by_id(transaction_id: int):
    """Return a single transaction by its ID."""
    for txn in TRANSACTIONS:
        if txn["id"] == transaction_id:
            return txn
    raise HTTPException(status_code=404, detail="Transaction not found")


@router.post("/classify")
def classify_transaction(payload: ClassifyRequest):
    """
    Send the transaction description + amount to Claude AI and
    get back a single accounting category.
    """
    api_key = os.getenv("ANTHROPIC_API_KEY")
    if not api_key:
        raise HTTPException(status_code=500, detail="Anthropic API key is not set")

    client = anthropic.Anthropic(api_key=api_key)

    prompt = (
        "You are an accounting AI assistant for Indian MSMEs (Micro, Small & Medium Enterprises). "
        f"A transaction has the following details:\n"
        f"Description: {payload.description}\n"
        f"Amount: ₹{payload.amount:,.2f}\n\n"
        "Classify this transaction into exactly ONE of the following categories:\n"
        "Revenue, Salary Expense, Rent Expense, GST Payment, TDS Payment, "
        "Vendor Payment, Utility Expense, Bank Charges, Loan Repayment, Miscellaneous.\n\n"
        "Reply with ONLY the category name and nothing else."
    )

    message = client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=50,
        messages=[{"role": "user", "content": prompt}],
    )

    category = message.content[0].text.strip()
    return {"category": category}
