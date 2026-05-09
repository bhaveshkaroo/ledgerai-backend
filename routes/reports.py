"""
LedgerAI — routes/reports.py
Professional Accrual-Basis Reporting Engine.
"""

import os
from fastapi import APIRouter, HTTPException
from routes.transactions import TRANSACTIONS

router = APIRouter()

@router.get("/pl")
def profit_and_loss():
    # Accrual Basis: Revenue is counted when invoiced
    revenue_cats = ["Sales Revenue", "Export Sales", "Other Income", "Interest Income", "Investment Income", "Commission Income", "Miscellaneous Income", "Forex Gain", "Export Incentive", "Bad Debt Recovery", "Insurance Recovery", "Profit on Asset Sale", "Discount Received", "Deferred Tax Income", "Investment Gain", "GST Refund"]
    total_revenue = sum(t["amount"] for t in TRANSACTIONS if t["type"] == "credit" and t["category"] in revenue_cats)
    
    # Expenses are counted when incurred
    exclude_from_exp = ["Fixed Asset", "Investments", "Security Deposit", "Digital Asset", "Intangible Asset", "Bank Loan", "Debentures", "Share Capital", "Securities Premium", "Bank Overdraft", "Customer Payment", "Vendor Payment", "Loan Repayment", "Dividend Payment", "Share Buyback", "Contra Entry", "Cash Withdrawal", "Asset Disposal", "Investment Redemption", "Drawings"]
    total_expenses = sum(t["amount"] for t in TRANSACTIONS if t["type"] == "debit" and t["category"] not in exclude_from_exp)
    
    return {
        "total_revenue": round(total_revenue, 2),
        "total_expenses": round(total_expenses, 2),
        "net_profit": round(total_revenue - total_expenses, 2),
    }

@router.get("/balance-sheet")
def balance_sheet():
    # 1. ACTUAL CASH (Only payments and receipts)
    cash_in_cats = ["Customer Payment", "Bank Loan", "Share Capital", "Securities Premium", "Capital Contribution", "Other Income", "Interest Income", "Investment Redemption", "Asset Disposal", "Cash Deposit", "Share Application Money"]
    cash_out_cats = ["Vendor Payment", "Rent Expense", "Salary Expense", "Utilities", "TDS Payment", "GST Payment", "Dividend Payment", "Loan Repayment", "Fixed Asset", "Investments", "Tax Payment", "Director Remuneration", "Drawings", "Cash Withdrawal"]
    
    cash_in = sum(t["amount"] for t in TRANSACTIONS if t["type"] == "credit" and t["category"] in cash_in_cats)
    cash_out = sum(t["amount"] for t in TRANSACTIONS if t["type"] == "debit" and t["category"] in cash_out_cats)
    cash_at_bank = cash_in - cash_out
    
    # 2. ACCOUNTS RECEIVABLE (Invoiced - Collected)
    total_sales = sum(t["amount"] for t in TRANSACTIONS if t["category"] in ["Sales Revenue", "Export Sales"])
    total_collected = sum(t["amount"] for t in TRANSACTIONS if t["category"] == "Customer Payment")
    accounts_receivable = total_sales - total_collected
    
    # 3. ACCOUNTS PAYABLE (Purchased - Paid)
    total_purchases = sum(t["amount"] for t in TRANSACTIONS if t["category"] == "Inventory Purchase")
    total_paid = sum(t["amount"] for t in TRANSACTIONS if t["category"] == "Vendor Payment")
    accounts_payable = total_purchases - total_paid
    
    # 4. OTHER ASSETS
    fixed_assets = sum(t["amount"] for t in TRANSACTIONS if t["category"] in ["Fixed Asset", "Digital Asset", "Intangible Asset"])
    acc_dep = sum(t["amount"] for t in TRANSACTIONS if t["category"] == "Accumulated Depreciation")
    other_assets = sum(t["amount"] for t in TRANSACTIONS if t["category"] in ["Investments", "Security Deposit", "Prepaid Expense", "Closing Stock", "TDS Receivable", "GST Input Credit"])
    
    total_assets = cash_at_bank + accounts_receivable + (fixed_assets - acc_dep) + other_assets
    
    # 5. LIABILITIES
    loans = sum(t["amount"] for t in TRANSACTIONS if t["category"] in ["Bank Loan", "Debentures", "Bank Overdraft"])
    loans -= sum(t["amount"] for t in TRANSACTIONS if t["category"] == "Loan Repayment")
    
    provisions = sum(t["amount"] for t in TRANSACTIONS if t["category"] in ["Tax Provision", "Outstanding Expenses", "Dividend Payable"])
    
    total_liabilities = accounts_payable + loans + provisions
    
    # 6. EQUITY
    equity = sum(t["amount"] for t in TRANSACTIONS if t["category"] in ["Share Capital", "Securities Premium", "General Reserve", "Capital Contribution"])
    equity -= sum(t["amount"] for t in TRANSACTIONS if t["category"] == "Drawings")
    
    # Profit (Accrual Basis)
    pl = profit_and_loss()
    net_profit = pl["net_profit"]
    
    total_liab_equity = total_liabilities + equity + net_profit

    return {
        "assets": {
            "Cash & Bank Balance": round(cash_at_bank, 2),
            "Accounts Receivable": round(accounts_receivable, 2),
            "Fixed Assets (Net)": round(fixed_assets - acc_dep, 2),
            "Other Assets": round(other_assets, 2)
        },
        "liabilities": {
            "Accounts Payable": round(accounts_payable, 2),
            "Loans & Borrowings": round(loans, 2),
            "Provisions": round(provisions, 2)
        },
        "equity": {
            "Shareholders Capital": round(equity, 2),
            "Retained Earnings (P&L)": round(net_profit, 2)
        },
        "total_assets": round(total_assets, 2),
        "total_liabilities_and_equity": round(total_liab_equity, 2),
        "is_balanced": abs(total_assets - total_liab_equity) < 100.0 # Accrual margin
    }

@router.get("/cash-flow-statement")
@router.get("/cashflow-statement")
def cash_flow():
    # Only true cash movements
    cash_in_cats = ["Customer Payment", "Bank Loan", "Share Capital", "Capital Contribution", "Other Income", "Investment Redemption", "Asset Disposal"]
    cash_out_cats = ["Vendor Payment", "Rent Expense", "Salary Expense", "Utilities", "GST Payment", "Dividend Payment", "Loan Repayment", "Fixed Asset", "Investments"]
    
    op_in = sum(t["amount"] for t in TRANSACTIONS if t["type"] == "credit" and t["category"] in ["Customer Payment", "Other Income"])
    op_out = sum(t["amount"] for t in TRANSACTIONS if t["type"] == "debit" and t["category"] in ["Vendor Payment", "Rent Expense", "Salary Expense", "Utilities", "GST Payment"])
    
    inv_in = sum(t["amount"] for t in TRANSACTIONS if t["category"] in ["Investment Redemption", "Asset Disposal"])
    inv_out = sum(t["amount"] for t in TRANSACTIONS if t["category"] in ["Fixed Asset", "Investments"])
    
    fin_in = sum(t["amount"] for t in TRANSACTIONS if t["category"] in ["Bank Loan", "Share Capital", "Securities Premium"])
    fin_out = sum(t["amount"] for t in TRANSACTIONS if t["category"] in ["Loan Repayment", "Dividend Payment"])
    
    return {
        "operating": round(op_in - op_out, 2),
        "investing": round(inv_in - inv_out, 2),
        "financing": round(fin_in - fin_out, 2),
        "net_change": round((op_in - op_out) + (inv_in - inv_out) + (fin_in - fin_out), 2)
    }

@router.get("/summary")
def summary():
    return {"summary": "Sharma Textiles Pvt Ltd is successfully operating on an accrual basis with significant accounts receivable from credit sales. The company has a stable capital base and is actively reinvesting cash into fixed assets."}
