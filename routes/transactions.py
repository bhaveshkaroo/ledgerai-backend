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
    { "id": 1, "date": "2026-04-01", "description": "Sales Revenue - Rajan Fabrics", "amount": 150000.00, "type": "credit", "category": "Revenue" },
    { "id": 2, "date": "2026-04-02", "description": "Monthly Office Rent - WeWork", "amount": 50000.00, "type": "debit", "category": "Rent Expense" },
    { "id": 3, "date": "2026-04-03", "description": "Electricity Bill - BEST", "amount": 12000.00, "type": "debit", "category": "Utility Expense" },
    { "id": 4, "date": "2026-04-05", "description": "Sales Revenue - Mehta Garments", "amount": 85000.00, "type": "credit", "category": "Revenue" },
    { "id": 5, "date": "2026-04-06", "description": "Bank Charges - HDFC Account Maintenance", "amount": 5000.00, "type": "debit", "category": "Bank Charges" },
    { "id": 6, "date": "2026-04-08", "description": "Vendor Payment - Surat Silk Mills", "amount": 75000.00, "type": "debit", "category": "Vendor Payment" },
    { "id": 7, "date": "2026-04-10", "description": "Sales Revenue - Patel Traders", "amount": 120000.00, "type": "credit", "category": "Revenue" },
    { "id": 8, "date": "2026-04-12", "description": "GST Payment to Government", "amount": 30000.00, "type": "debit", "category": "GST Payment" },
    { "id": 9, "date": "2026-04-14", "description": "Loan Repayment - SBI", "amount": 45000.00, "type": "debit", "category": "Loan Repayment" },
    { "id": 10, "date": "2026-04-15", "description": "Miscellaneous Office Supplies", "amount": 8000.00, "type": "debit", "category": "Miscellaneous" },
    { "id": 11, "date": "2026-04-17", "description": "Sales Revenue - Rajan Fabrics Bulk Order", "amount": 180000.00, "type": "credit", "category": "Revenue" },
    { "id": 12, "date": "2026-04-19", "description": "Vendor Payment - Arvind Mills", "amount": 65000.00, "type": "debit", "category": "Vendor Payment" },
    { "id": 13, "date": "2026-04-21", "description": "TDS Payment", "amount": 15000.00, "type": "debit", "category": "TDS Payment" },
    { "id": 14, "date": "2026-04-23", "description": "Sales Revenue - Mehta Garments New Collection", "amount": 90000.00, "type": "credit", "category": "Revenue" },
    { "id": 15, "date": "2026-04-25", "description": "Vendor Payment - Textile Dyeing Co", "amount": 40000.00, "type": "debit", "category": "Vendor Payment" },
    { "id": 16, "date": "2026-04-26", "description": "Water Bill - BMC", "amount": 5000.00, "type": "debit", "category": "Utility Expense" },
    { "id": 17, "date": "2026-04-27", "description": "Sales Revenue - Patel Traders", "amount": 110000.00, "type": "credit", "category": "Revenue" },
    { "id": 18, "date": "2026-04-28", "description": "Staff Salary - April 2026", "amount": 80000.00, "type": "debit", "category": "Salary Expense" },
    { "id": 19, "date": "2026-04-29", "description": "Freelance Designer Fee", "amount": 25000.00, "type": "debit", "category": "Vendor Payment" },
    { "id": 20, "date": "2026-04-30", "description": "Walk-in Retail Sales", "amount": 55000.00, "type": "credit", "category": "Revenue" }
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
