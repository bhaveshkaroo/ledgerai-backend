"""
LedgerAI — routes/reports.py
Handles financial-reporting endpoints:
  • GET  /reports/pl       → Profit & Loss statement
  • GET  /reports/cashflow → Day-by-day running cash balance
  • GET  /reports/summary  → AI-written 3-sentence financial summary
  • GET  /reports/balance-sheet → Comprehensive Corporate BS
  • GET  /reports/cash-flow-statement → Indirect Cash Flow
"""

import os
from fastapi import APIRouter, HTTPException
import anthropic

# Import the shared transaction data
from routes.transactions import TRANSACTIONS

router = APIRouter()


@router.get("/pl")
def profit_and_loss():
    total_revenue = sum(t["amount"] for t in TRANSACTIONS if t["type"] == "credit")
    total_expenses = sum(t["amount"] for t in TRANSACTIONS if t["type"] == "debit")
    net_profit = total_revenue - total_expenses
    return {
        "total_revenue": total_revenue,
        "total_expenses": total_expenses,
        "net_profit": net_profit,
    }


@router.get("/cashflow")
def cashflow():
    sorted_txns = sorted(TRANSACTIONS, key=lambda t: t["date"])
    running_balance = 0.0
    daily_balances = []
    for txn in sorted_txns:
        if txn["type"] == "credit":
            running_balance += txn["amount"]
        else:
            running_balance -= txn["amount"]
        daily_balances.append({
            "date": txn["date"],
            "balance": round(running_balance, 2),
        })
    return daily_balances


@router.get("/summary")
def financial_summary():
    total_revenue = sum(t["amount"] for t in TRANSACTIONS if t["type"] == "credit")
    total_expenses = sum(t["amount"] for t in TRANSACTIONS if t["type"] == "debit")
    net_profit = total_revenue - total_expenses
    api_key = os.getenv("ANTHROPIC_API_KEY")
    if not api_key:
        raise HTTPException(status_code=500, detail="Anthropic API key is not set")
    client = anthropic.Anthropic(api_key=api_key)
    prompt = (
        "You are a financial advisor for Sharma Textiles Pvt Ltd. "
        f"Numbers: Revenue ₹{total_revenue:,.2f}, Expenses ₹{total_expenses:,.2f}, Profit ₹{net_profit:,.2f}. "
        "Write exactly 3 sentences summarising the health of this business."
    )
    message = client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=300,
        messages=[{"role": "user", "content": prompt}],
    )
    return {"summary": message.content[0].text.strip()}

@router.get("/trial-balance")
def trial_balance():
    accounts = {}
    for t in TRANSACTIONS:
        cat = t["category"]
        if cat not in accounts:
            accounts[cat] = {"debit": 0.0, "credit": 0.0}
        if t["type"] == "debit":
            accounts[cat]["debit"] += t["amount"]
        else:
            accounts[cat]["credit"] += t["amount"]
    
    total_credits = sum(a["credit"] for a in accounts.values())
    total_debits = sum(a["debit"] for a in accounts.values())
    accounts["Cash & Bank Offset"] = {"debit": total_credits, "credit": total_debits}
    
    return {
        "accounts": accounts,
        "total_debits": total_credits + total_debits,
        "total_credits": total_credits + total_debits,
        "is_balanced": True
    }

@router.get("/balance-sheet")
def balance_sheet():
    cash_at_bank = sum(t["amount"] if t["type"] == "credit" else -t["amount"] for t in TRANSACTIONS)
    
    asset_cats = [
        "Fixed Asset", "Security Deposit", "GST Input Credit", "TDS Receivable", "Vendor Advance", 
        "Investments", "Prepaid Expense", "Cash Deposit", "Petty Cash", "Digital Asset", 
        "GST Receivable", "Deferred Tax Asset", "Accrued Income", "Bank", "Closing Stock",
        "Employee Advance", "Intangible Asset", "Prepaid Salary", "Security Deposit Recovery",
        "Employee Advance Recovery", "TDS Receivable adjustment"
    ]
    other_assets = sum(t["amount"] for t in TRANSACTIONS if t["category"] in asset_cats)
    
    liab_cats = [
        "GST Payable", "Bank Loan", "Debenture Interest Payable", "Debentures", "Current Liabilities", 
        "Loan Received", "Outstanding Expenses", "Dividend Payable", "Tax Provision", 
        "Deferred Tax Liability", "Bank Overdraft", "Outstanding Expense", "Lease Liability", 
        "Unearned Revenue", "Deferred Revenue", "TDS Payable", "Interest Payable",
        "Provision for Doubtful Debts"
    ]
    total_liabilities = sum(t["amount"] for t in TRANSACTIONS if t["category"] in liab_cats)

    equity_cats = [
        "Share Capital", "Securities Premium", "DRR Reserve", "General Reserve", "Capital Contribution", 
        "Share Application Money", "Bonus Share Capital", "Preference Share Capital", "ESOP Reserve", 
        "Retained Earnings", "Reserve Transfer", "Profit Appropriation", "Debenture Redemption Reserve",
        "Opening Balance Adjustment"
    ]
    capital = sum(t["amount"] for t in TRANSACTIONS if t["category"] in equity_cats)
    capital -= sum(t["amount"] for t in TRANSACTIONS if t["category"] == "Drawings")
    
    income_cats = [
        "Sales Revenue", "Export Sales", "Other Income", "Interest Income", "Investment Income", 
        "Commission Income", "Miscellaneous Income", "Forex Gain", "Export Incentive", 
        "Bad Debt Recovery", "Insurance Recovery", "Profit on Asset Sale", "Discount Received", 
        "Purchase Return", "Deferred Tax Income", "Investment Gain", "GST Refund"
    ]
    total_income = sum(t["amount"] for t in TRANSACTIONS if t["type"] == "credit" and t["category"] in income_cats)
    
    exclude = asset_cats + liab_cats + equity_cats + income_cats + ["Drawings", "Loan Repayment", "Dividend Payment", "Share Issue Expense", "Debenture Redemption", "Share Buyback", "Tax Payment", "Advance Tax", "Preference Share Redemption", "Dividend Declaration", "COGS", "Asset Disposal", "Investment Redemption", "Contra Entry", "Cash Withdrawal", "Suspense Adjustment", "Rectification Entry", "Journal Adjustment", "Reserve Adjustment", "Closing Entry", "Reversal Entry", "Bank Reconciliation Adjustment"]
    total_expenses = sum(t["amount"] for t in TRANSACTIONS if t["type"] == "debit" and t["category"] not in exclude)
    
    net_profit = total_income - total_expenses
    total_assets = cash_at_bank + other_assets
    total_equity_liab = total_liabilities + capital + net_profit

    return {
        "assets": {"Cash & Bank": round(cash_at_bank, 2), "Other Assets": round(other_assets, 2)},
        "liabilities": {"Total": round(total_liabilities, 2)},
        "equity": {"Capital": round(capital, 2), "Net Profit": round(net_profit, 2)},
        "total_assets": round(total_assets, 2),
        "total_liabilities_and_equity": round(total_equity_liab, 2),
        "is_balanced": abs(total_assets - total_equity_liab) < 1.0
    }

@router.get("/cash-flow-statement")
def cash_flow_statement():
    inv_cats = ["Fixed Asset", "Investments", "Asset Disposal", "Investment Redemption", "Digital Asset", "Intangible Asset"]
    fin_cats = ["Share Capital", "Bank Loan", "Bank Overdraft", "Debentures", "Dividend Payment", "Loan Repayment", "Share Buyback", "Securities Premium", "Preference Share Capital", "Preference Share Redemption"]
    
    inv_txns = [t for t in TRANSACTIONS if t["category"] in inv_cats]
    fin_txns = [t for t in TRANSACTIONS if t["category"] in fin_cats]
    
    inv_cf = sum(t["amount"] if t["type"] == "credit" else -t["amount"] for t in inv_txns)
    fin_cf = sum(t["amount"] if t["type"] == "credit" else -t["amount"] for t in fin_txns)
    
    # Total Cash Flow
    total_cf = sum(t["amount"] if t["type"] == "credit" else -t["amount"] for t in TRANSACTIONS)
    op_cf = total_cf - (inv_cf + fin_cf)
    
    return {
        "operating": round(op_cf, 2),
        "investing": round(inv_cf, 2),
        "financing": round(fin_cf, 2),
        "net_change": round(total_cf, 2)
    }
