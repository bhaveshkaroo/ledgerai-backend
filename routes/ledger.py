"""
LedgerAI — routes/ledger.py
Handles the detailed accounting ledger:
  • GET /ledger/all     → Full double-entry ledger with running balance
  • GET /ledger/account → Filtered ledger for a specific account
"""

from fastapi import APIRouter
from routes.transactions import TRANSACTIONS

router = APIRouter()

@router.get("/all")
def get_full_ledger():
    """
    Returns all transactions in a double-entry ledger format with a running balance.
    """
    sorted_txns = sorted(TRANSACTIONS, key=lambda t: t["date"])
    ledger = []
    running_balance = 0.0

    for txn in sorted_txns:
        debit = txn["amount"] if txn["type"] == "debit" else 0.0
        credit = txn["amount"] if txn["type"] == "credit" else 0.0
        
        # In typical business accounting, Credits (Revenue) increase balance, Debits (Expenses) decrease it
        if txn["type"] == "credit":
            running_balance += txn["amount"]
        else:
            running_balance -= txn["amount"]

        ledger.append({
            "date": txn["date"],
            "narration": txn["description"],
            "debit": debit,
            "credit": credit,
            "balance": round(running_balance, 2)
        })

    return ledger

@router.get("/account")
def get_account_ledger(name: str):
    """
    Returns ledger entries for a specific account category (Flexible Match).
    """
    account_txns = [t for t in TRANSACTIONS if name.lower() in t["category"].lower()]
    sorted_txns = sorted(account_txns, key=lambda t: t["date"])
    
    ledger = []
    total_debits = 0.0
    total_credits = 0.0
    running_balance = 0.0

    for txn in sorted_txns:
        debit = txn["amount"] if txn["type"] == "debit" else 0.0
        credit = txn["amount"] if txn["type"] == "credit" else 0.0
        
        total_debits += debit
        total_credits += credit
        
        if txn["type"] == "credit":
            running_balance += txn["amount"]
        else:
            running_balance -= txn["amount"]

        ledger.append({
            "date": txn["date"],
            "narration": txn["description"],
            "debit": debit,
            "credit": credit,
            "balance": round(running_balance, 2)
        })

    return {
        "account": name,
        "opening_balance": 0.0,
        "total_debits": total_debits,
        "total_credits": total_credits,
        "closing_balance": round(running_balance, 2),
        "entries": ledger
    }
