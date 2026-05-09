"""
LedgerAI — routes/transactions.py
Holds 50 realistic corporate-level transactions for Sharma Textiles Pvt Ltd.
"""

from fastapi import APIRouter

router = APIRouter()

TRANSACTIONS = [
    # --- April 1 to April 20 (Existing/Optimized) ---
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
    {"id": 14, "date": "2026-04-14", "description": "Purchase of office printer", "amount": 18000.0, "type": "debit", "category": "Fixed Asset"},
    {"id": 15, "date": "2026-04-15", "description": "Bank processing charges", "amount": 2500.0, "type": "debit", "category": "Bank Charges"},
    {"id": 16, "date": "2026-04-16", "description": "Payment received from Kiran Exports", "amount": 193000.0, "type": "credit", "category": "Revenue"},
    {"id": 17, "date": "2026-04-17", "description": "Transportation and freight charges", "amount": 14000.0, "type": "debit", "category": "Miscellaneous"},
    {"id": 18, "date": "2026-04-18", "description": "Vendor payment to Vardhman Threads", "amount": 88000.0, "type": "debit", "category": "Vendor Payment"},
    {"id": 19, "date": "2026-04-19", "description": "Payment received from Lucky Hosiery", "amount": 156000.0, "type": "credit", "category": "Revenue"},
    {"id": 20, "date": "2026-04-20", "description": "Staff salary payment", "amount": 72000.0, "type": "debit", "category": "Salary Expense"},
    
    # --- New Advanced Corporate Transactions (Items 21-50) ---
    {"id": 21, "date": "2026-04-20", "description": "Interest received on Fixed Deposit", "amount": 4500.0, "type": "credit", "category": "Investing Income"},
    {"id": 22, "date": "2026-04-21", "description": "Purchase of high-speed textile machinery", "amount": 250000.0, "type": "debit", "category": "Fixed Asset"},
    {"id": 23, "date": "2026-04-22", "description": "Secured term loan received from HDFC Bank", "amount": 500000.0, "type": "credit", "category": "Loan Received"},
    {"id": 24, "date": "2026-04-23", "description": "Interest payment on 9% Debentures", "amount": 18000.0, "type": "debit", "category": "Finance Cost"},
    {"id": 25, "date": "2026-04-24", "description": "Final dividend paid to shareholders", "amount": 60000.0, "type": "debit", "category": "Dividend Paid"},
    {"id": 26, "date": "2026-04-25", "description": "Sale of old office scrap (investing)", "amount": 3200.0, "type": "credit", "category": "Investing Income"},
    {"id": 27, "date": "2026-04-26", "description": "Pre-payment for annual insurance cover", "amount": 24000.0, "type": "debit", "category": "Prepayment"},
    {"id": 28, "date": "2026-04-27", "description": "Refund received from GST department (ITC)", "amount": 15400.0, "type": "credit", "category": "GST Refund"},
    {"id": 29, "date": "2026-04-28", "description": "Audit and professional fees paid", "amount": 25000.0, "type": "debit", "category": "Professional Fees"},
    {"id": 30, "date": "2026-04-29", "description": "Bad debts written off", "amount": 4000.0, "type": "debit", "category": "Bad Debt"},
    {"id": 31, "date": "2026-04-29", "description": "Payment received from Rajan Fabrics", "amount": 112000.0, "type": "credit", "category": "Revenue"},
    {"id": 32, "date": "2026-04-30", "description": "Interest paid on working capital loan", "amount": 16500.0, "type": "debit", "category": "Finance Cost"},
    {"id": 33, "date": "2026-04-30", "description": "Subscription for industry journal", "amount": 1200.0, "type": "debit", "category": "Miscellaneous"},
    {"id": 34, "date": "2026-04-30", "description": "Office refreshments and staff welfare", "amount": 5400.0, "type": "debit", "category": "Miscellaneous"},
    {"id": 35, "date": "2026-04-30", "description": "Payment to Vardhman Threads", "amount": 42000.0, "type": "debit", "category": "Vendor Payment"},
    {"id": 36, "date": "2026-04-30", "description": "Courier and postage charges", "amount": 800.0, "type": "debit", "category": "Miscellaneous"},
    {"id": 37, "date": "2026-04-30", "description": "TDS deposit for professional fees", "amount": 2500.0, "type": "debit", "category": "GST Payment"},
    {"id": 38, "date": "2026-04-30", "description": "Sales commission paid to agent", "amount": 15000.0, "type": "debit", "category": "Miscellaneous"},
    {"id": 39, "date": "2026-04-30", "description": "Payment received from Bombay Fashion House", "amount": 85000.0, "type": "credit", "category": "Revenue"},
    {"id": 40, "date": "2026-04-30", "description": "Vehicle maintenance for delivery van", "amount": 6200.0, "type": "debit", "category": "Miscellaneous"},
    {"id": 41, "date": "2026-04-30", "description": "Bonus paid to sales team", "amount": 30000.0, "type": "debit", "category": "Salary Expense"},
    {"id": 42, "date": "2026-04-30", "description": "Property tax for warehouse", "amount": 18000.0, "type": "debit", "category": "Miscellaneous"},
    {"id": 43, "date": "2026-04-30", "description": "Interest on security deposit received", "amount": 1500.0, "type": "credit", "category": "Investing Income"},
    {"id": 44, "date": "2026-04-30", "description": "Repairs to electrical fittings", "amount": 4500.0, "type": "debit", "category": "Miscellaneous"},
    {"id": 45, "date": "2026-04-30", "description": "Payment to Reliance Textile Wholesale", "amount": 55000.0, "type": "debit", "category": "Vendor Payment"},
    {"id": 46, "date": "2026-04-30", "description": "Printing of new marketing brochures", "amount": 12000.0, "type": "debit", "category": "Miscellaneous"},
    {"id": 47, "date": "2026-04-30", "description": "Recovery of old bad debt", "amount": 3500.0, "type": "credit", "category": "Revenue"},
    {"id": 48, "date": "2026-04-30", "description": "Bank charge for cheque bounce (customer)", "amount": 500.0, "type": "debit", "category": "Bank Charges"},
    {"id": 49, "date": "2026-04-30", "description": "Payment received from Patel Traders", "amount": 122000.0, "type": "credit", "category": "Revenue"},
    {"id": 50, "date": "2026-04-30", "description": "Closing Petty Cash adjustment", "amount": 1000.0, "type": "debit", "category": "Miscellaneous"}
]

@router.get("/all")
def get_transactions():
    return TRANSACTIONS

@router.get("/classify")
def classify_transaction(description: str):
    # Dummy classifier
    if "payment" in description.lower() or "received" in description.lower():
        return {"category": "Revenue"}
    return {"category": "Miscellaneous"}
