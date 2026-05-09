"""
LedgerAI — routes/transactions.py
Holds the realistic dummy transaction data for Sharma Textiles Pvt Ltd.
"""

from fastapi import APIRouter

router = APIRouter()

# 30 Realistic Transactions for April 2026
TRANSACTIONS = [
    {"id": 1, "date": "2026-04-01", "description": "Capital introduced by directors", "amount": 500000.0, "type": "credit", "category": "Equity"},
    {"id": 2, "date": "2026-04-02", "description": "Office rent paid for April", "amount": 45000.0, "type": "debit", "category": "Rent Expense"},
    {"id": 3, "date": "2026-04-03", "description": "Fabric purchase from Gujarat Cotton Mills", "amount": 120000.0, "type": "debit", "category": "Vendor Payment"},
    {"id": 4, "date": "2026-04-04", "description": "Payment received from Rajan Fabrics", "amount": 185000.0, "type": "credit", "category": "Revenue"},
    {"id": 5, "date": "2026-04-05", "description": "Electricity bill payment", "amount": 12000.0, "type": "debit", "category": "Utility Expense"},
    {"id": 6, "date": "2026-04-06", "description": "Salary paid to warehouse staff", "amount": 68000.0, "type": "debit", "category": "Salary Expense"},
    {"id": 7, "date": "2026-04-07", "description": "Payment received from Mehta Garments", "amount": 142000.0, "type": "credit", "category": "Revenue"},
    {"id": 8, "date": "2026-04-08", "description": "GST payment to government", "amount": 52000.0, "type": "debit", "category": "GST Payment"},
    {"id": 9, "date": "2026-04-09", "description": "Vendor payment to Surat Silk Suppliers", "amount": 76000.0, "type": "debit", "category": "Vendor Payment"},
    {"id": 10, "date": "2026-04-10", "description": "Payment received from Patel Traders", "amount": 168000.0, "type": "credit", "category": "Revenue"},
    {"id": 11, "date": "2026-04-11", "description": "Internet and office expenses", "amount": 8500.0, "type": "debit", "category": "Miscellaneous"},
    {"id": 12, "date": "2026-04-12", "description": "Loan EMI repayment", "amount": 40000.0, "type": "debit", "category": "Loan Repayment"},
    {"id": 13, "date": "2026-04-13", "description": "Payment received from Bombay Fashion House", "amount": 126000.0, "type": "credit", "category": "Revenue"},
    {"id": 14, "date": "2026-04-14", "description": "Purchase of office printer", "amount": 18000.0, "type": "debit", "category": "Miscellaneous"},
    {"id": 15, "date": "2026-04-15", "description": "Bank processing charges", "amount": 2500.0, "type": "debit", "category": "Bank Charges"},
    {"id": 16, "date": "2026-04-16", "description": "Payment received from Kiran Exports", "amount": 193000.0, "type": "credit", "category": "Revenue"},
    {"id": 17, "date": "2026-04-17", "description": "Transportation and freight charges", "amount": 14000.0, "type": "debit", "category": "Miscellaneous"},
    {"id": 18, "date": "2026-04-18", "description": "Vendor payment to Vardhman Threads", "amount": 88000.0, "type": "debit", "category": "Vendor Payment"},
    {"id": 19, "date": "2026-04-19", "description": "Payment received from Lucky Hosiery", "amount": 156000.0, "type": "credit", "category": "Revenue"},
    {"id": 20, "date": "2026-04-20", "description": "Staff salary payment", "amount": 72000.0, "type": "debit", "category": "Salary Expense"},
    {"id": 21, "date": "2026-04-21", "description": "Purchase of warehouse shelves", "amount": 35000.0, "type": "debit", "category": "Miscellaneous"},
    {"id": 22, "date": "2026-04-22", "description": "Payment received from Rajan Fabrics", "amount": 98000.0, "type": "credit", "category": "Revenue"},
    {"id": 23, "date": "2026-04-23", "description": "Miscellaneous office maintenance expense", "amount": 9000.0, "type": "debit", "category": "Miscellaneous"},
    {"id": 24, "date": "2026-04-24", "description": "GST input credit adjustment", "amount": 18000.0, "type": "credit", "category": "Revenue"},
    {"id": 25, "date": "2026-04-25", "description": "Payment to Reliance Textile Wholesale", "amount": 67000.0, "type": "debit", "category": "Vendor Payment"},
    {"id": 26, "date": "2026-04-26", "description": "Customer advance received from Mehta Garments", "amount": 75000.0, "type": "credit", "category": "Revenue"},
    {"id": 27, "date": "2026-04-27", "description": "Insurance premium payment", "amount": 22000.0, "type": "debit", "category": "Miscellaneous"},
    {"id": 28, "date": "2026-04-28", "description": "Cash withdrawal for petty expenses", "amount": 10000.0, "type": "debit", "category": "Miscellaneous"},
    {"id": 29, "date": "2026-04-29", "description": "Payment received from Patel Traders", "amount": 134000.0, "type": "credit", "category": "Revenue"},
    {"id": 30, "date": "2026-04-30", "description": "Interest paid on working capital loan", "amount": 16000.0, "type": "debit", "category": "Bank Charges"}
]

@router.get("/all")
def get_transactions():
    return TRANSACTIONS

@router.get("/classify")
def classify_transaction(description: str):
    # Dummy classifier for UI testing (AI summary handles real logic)
    if "payment" in description.lower() or "received" in description.lower():
        return {"category": "Revenue"}
    return {"category": "Miscellaneous"}
