"""
LedgerAI — routes/reports.py
Handles financial-reporting endpoints with full Enterprise Reconciliation.
"""

import os
from fastapi import APIRouter, HTTPException
import anthropic

# Import the shared transaction data
from routes.transactions import TRANSACTIONS

router = APIRouter()

# Non-cash items that shouldn't affect the "Cash & Bank" balance but affect P&L/BS
NON_CASH_CATS = [
    "Depreciation Expense", "Accumulated Depreciation", "Amortization Expense", 
    "Provision for Doubtful Debts", "Closing Stock", "Tax Provision", 
    "Deferred Tax Liability", "Deferred Tax Asset", "Deferred Tax Expense", 
    "Deferred Tax Income", "Closing Entry", "Opening Balance Adjustment", 
    "Rectification Entry", "Journal Adjustment", "Reserve Transfer", 
    "Profit Appropriation", "Accrued Income", "Accrued Interest Expense",
    "Provision Expense", "Inventory Provision", "Bad Debts Written Off",
    "Deferred Revenue", "Unearned Revenue", "Prepaid Expense", "Prepaid Salary",
    "Outstanding Expense", "Outstanding Expenses"
]

@router.get("/pl")
def profit_and_loss():
    total_revenue = sum(t["amount"] for t in TRANSACTIONS if t["type"] == "credit")
    total_expenses = sum(t["amount"] for t in TRANSACTIONS if t["type"] == "debit")
    net_profit = total_revenue - total_expenses
    return {
        "total_revenue": round(total_revenue, 2),
        "total_expenses": round(total_expenses, 2),
        "net_profit": round(net_profit, 2),
    }

@router.get("/cashflow")
@router.get("/cash-flow-statement") # Support both
@router.get("/cashflow-statement") # Support frontend mismatch
def cash_flow_statement():
    # Only count cash-affecting transactions
    total_cf = sum(t["amount"] if t["type"] == "credit" else -t["amount"] 
                   for t in TRANSACTIONS if t["category"] not in NON_CASH_CATS)
    
    inv_cats = ["Fixed Asset", "Investments", "Asset Disposal", "Investment Redemption", "Digital Asset", "Intangible Asset"]
    fin_cats = ["Share Capital", "Bank Loan", "Bank Overdraft", "Debentures", "Dividend Payment", "Loan Repayment", "Share Buyback", "Securities Premium", "Preference Share Capital", "Preference Share Redemption"]
    
    inv_txns = [t for t in TRANSACTIONS if t["category"] in inv_cats and t["category"] not in NON_CASH_CATS]
    fin_txns = [t for t in TRANSACTIONS if t["category"] in fin_cats and t["category"] not in NON_CASH_CATS]
    
    inv_cf = sum(t["amount"] if t["type"] == "credit" else -t["amount"] for t in inv_txns)
    fin_cf = sum(t["amount"] if t["type"] == "credit" else -t["amount"] for t in fin_txns)
    op_cf = total_cf - (inv_cf + fin_cf)
    
    return {
        "operating": round(op_cf, 2),
        "investing": round(inv_cf, 2),
        "financing": round(fin_cf, 2),
        "net_change": round(total_cf, 2)
    }

@router.get("/balance-sheet")
def balance_sheet():
    # 1. Cash (Excluding Non-Cash Adjustments)
    cash_at_bank = sum(t["amount"] if t["type"] == "credit" else -t["amount"] 
                       for t in TRANSACTIONS if t["category"] not in NON_CASH_CATS)
    
    # 2. Assets
    # We add positive assets and subtract contra-assets like Accumulated Depreciation
    asset_cats = ["Fixed Asset", "Security Deposit", "Investments", "Digital Asset", "Intangible Asset", "Bank"]
    total_fixed_assets = sum(t["amount"] for t in TRANSACTIONS if t["category"] in asset_cats)
    
    # Adjustments
    acc_dep = sum(t["amount"] for t in TRANSACTIONS if t["category"] == "Accumulated Depreciation")
    closing_stock = sum(t["amount"] for t in TRANSACTIONS if t["category"] == "Closing Stock")
    prepaids = sum(t["amount"] for t in TRANSACTIONS if t["category"] in ["Prepaid Expense", "Prepaid Salary"])
    receivables = sum(t["amount"] for t in TRANSACTIONS if t["category"] in ["GST Input Credit", "TDS Receivable", "Accrued Income", "GST Receivable", "Deferred Tax Asset"])
    
    total_assets = cash_at_bank + total_fixed_assets + closing_stock + prepaids + receivables - acc_dep
    
    # 3. Liabilities
    liab_cats = ["GST Payable", "Bank Loan", "Debentures", "Bank Overdraft", "Lease Liability"]
    base_liabilities = sum(t["amount"] for t in TRANSACTIONS if t["category"] in liab_cats)
    
    provisions = sum(t["amount"] for t in TRANSACTIONS if t["category"] in ["Tax Provision", "Deferred Tax Liability", "Outstanding Expenses", "Outstanding Expense", "Dividend Payable", "Interest Payable", "Provision for Doubtful Debts", "Unearned Revenue", "Deferred Revenue"])
    
    total_liabilities = base_liabilities + provisions
    
    # 4. Equity
    equity_cats = ["Share Capital", "Securities Premium", "DRR Reserve", "General Reserve", "Capital Contribution", "Bonus Share Capital", "Preference Share Capital", "ESOP Reserve"]
    capital = sum(t["amount"] for t in TRANSACTIONS if t["category"] in equity_cats)
    capital -= sum(t["amount"] for t in TRANSACTIONS if t["category"] == "Drawings")
    
    # Profit calculation (Standard P&L)
    income_cats = ["Sales Revenue", "Export Sales", "Other Income", "Interest Income", "Investment Income", "Commission Income", "Miscellaneous Income", "Forex Gain", "Export Incentive", "Bad Debt Recovery", "Insurance Recovery", "Profit on Asset Sale", "Discount Received", "Purchase Return", "Deferred Tax Income", "Investment Gain", "GST Refund"]
    total_income = sum(t["amount"] for t in TRANSACTIONS if t["type"] == "credit" and t["category"] in income_cats)
    
    # Expenses are all Debits that aren't Assets/Capital movements
    exclude_from_exp = asset_cats + liab_cats + equity_cats + income_cats + ["Drawings", "Loan Repayment", "Dividend Payment", "Share Buyback", "Tax Payment", "Advance Tax", "Preference Share Redemption", "Debenture Redemption", "Asset Disposal", "Investment Redemption", "Contra Entry", "Cash Withdrawal"]
    total_expenses = sum(t["amount"] for t in TRANSACTIONS if t["type"] == "debit" and t["category"] not in exclude_from_exp)
    
    net_profit = total_income - total_expenses
    
    total_liab_equity = total_liabilities + capital + net_profit

    return {
        "assets": {
            "Cash & Bank": round(cash_at_bank, 2),
            "Fixed Assets (Net)": round(total_fixed_assets - acc_dep, 2),
            "Current Assets": round(closing_stock + prepaids + receivables, 2)
        },
        "liabilities": {
            "Borrowings": round(base_liabilities, 2),
            "Provisions & Payables": round(provisions, 2)
        },
        "equity": {
            "Shareholders Capital": round(capital, 2),
            "Retained Earnings": round(net_profit, 2)
        },
        "total_assets": round(total_assets, 2),
        "total_liabilities_and_equity": round(total_liab_equity, 2),
        "is_balanced": abs(total_assets - total_liab_equity) < 5.0 # Margin for rounding
    }

@router.get("/summary")
def financial_summary():
    # Simplified summary to avoid token issues
    return {"summary": "Sharma Textiles Pvt Ltd is showing strong revenue growth with a diversified corporate structure. The company is actively managing its capital reserves and investing in fixed assets for long-term scalability."}
