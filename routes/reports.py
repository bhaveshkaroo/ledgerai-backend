"""
LedgerAI — routes/reports.py
Handles financial-reporting endpoints:
  • GET  /reports/pl       → Profit & Loss statement
  • GET  /reports/cashflow → Day-by-day running cash balance
  • GET  /reports/summary  → AI-written 3-sentence financial summary
"""

import os
from fastapi import APIRouter, HTTPException
import anthropic

# Import the shared transaction data
from routes.transactions import TRANSACTIONS

router = APIRouter()


@router.get("/pl")
def profit_and_loss():
    """
    Calculate total revenue (credits), total expenses (debits),
    and net profit from the transaction list.
    """
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
    """
    Walk through transactions chronologically and compute a
    running balance at the end of each day.
    """
    # Sort by date
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
    """
    Compute P&L figures, then ask Claude to write a plain-English
    3-sentence summary of the business's financial health.
    """
    total_revenue = sum(t["amount"] for t in TRANSACTIONS if t["type"] == "credit")
    total_expenses = sum(t["amount"] for t in TRANSACTIONS if t["type"] == "debit")
    net_profit = total_revenue - total_expenses

    api_key = os.getenv("ANTHROPIC_API_KEY")
    if not api_key:
        raise HTTPException(status_code=500, detail="Anthropic API key is not set")

    client = anthropic.Anthropic(api_key=api_key)

    prompt = (
        "You are a financial advisor for a small textile trading company based in Mumbai called Sharma Textiles Pvt Ltd. "
        "Here are the current numbers:\n"
        f"Total Revenue: ₹{total_revenue:,.2f}\n"
        f"Total Expenses: ₹{total_expenses:,.2f}\n"
        f"Net Profit: ₹{net_profit:,.2f}\n\n"
        "Write exactly 3 sentences summarising the financial health of this business. "
        "Be direct and helpful. Use an Indian business context."
    )

    message = client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=300,
        messages=[{"role": "user", "content": prompt}],
    )

    summary_text = message.content[0].text.strip()
    return {"summary": summary_text}


@router.get("/trial-balance")
def trial_balance():
    """
    Feature Two: Groups transactions and adds a Cash/Bank offset to balance the books.
    """
    accounts = {}
    categories = set(t["category"] for t in TRANSACTIONS)

    # Calculate net for each category
    for cat in categories:
        debits = sum(t["amount"] for t in TRANSACTIONS if t["category"] == cat and t["type"] == "debit")
        credits = sum(t["amount"] for t in TRANSACTIONS if t["category"] == cat and t["type"] == "credit")
        if debits > 0 or credits > 0:
            accounts[cat] = {"debit": debits, "credit": credits}

    # The 'Missing' side of every transaction is the Cash/Bank account
    total_credits_others = sum(a["credit"] for a in accounts.values())
    total_debits_others = sum(a["debit"] for a in accounts.values())
    
    # In a double entry system, if we credit Revenue, we debit Cash.
    # So Cash Debit = Total Credits of other accounts
    # And Cash Credit = Total Debits of other accounts
    accounts["Cash & Bank"] = {"debit": total_credits_others, "credit": total_debits_others}

    final_debits = sum(a["debit"] for a in accounts.values())
    final_credits = sum(a["credit"] for a in accounts.values())

    return {
        "accounts": accounts,
        "total_debits": final_debits,
        "total_credits": final_credits,
        "is_balanced": abs(final_debits - final_credits) < 1.0
    }


@router.get("/balance-sheet")
def balance_sheet():
    """
    Professional Corporate Balance Sheet:
    Handles Share Capital, Reserves, Loans, Fixed Assets, and Accruals.
    """
    # 1. Assets
    cash_at_bank = sum(t["amount"] if t["type"] == "credit" else -t["amount"] for t in TRANSACTIONS)
    
    asset_cats = ["Fixed Asset", "Security Deposit", "GST Input Credit", "TDS Receivable", "Vendor Advance", "Investments", "Prepaid Expense", "Cash Deposit", "Petty Cash", "Digital Asset", "GST Receivable", "Deferred Tax Asset"]
    other_assets = sum(t["amount"] for t in TRANSACTIONS if t["category"] in asset_cats)
    
    # 2. Liabilities
    liab_cats = ["GST Payable", "Bank Loan", "Debenture Interest Payable", "Debentures", "Current Liabilities", "Loan Received", "Outstanding Expenses", "Dividend Payable", "Tax Provision", "Deferred Tax Liability", "Bank Overdraft", "Outstanding Expense", "Lease Liability", "Debenture Interest Payable", "Unearned Revenue"]
    total_liabilities = sum(t["amount"] for t in TRANSACTIONS if t["category"] in liab_cats)

    # 3. Equity
    equity_cats = ["Share Capital", "Securities Premium", "DRR Reserve", "General Reserve", "Capital Contribution", "Share Application Money", "Bonus Share Capital", "Preference Share Capital", "ESOP Reserve", "Retained Earnings"]
    capital = sum(t["amount"] for t in TRANSACTIONS if t["category"] in equity_cats)
    
    # PROFIT = (Incomes) - (Expenses)
    income_cats = ["Sales Revenue", "Other Income", "Interest Income", "Forex Gain", "Export Incentive", "Commission Income", "Investment Income", "GST Refund", "Bad Debt Recovery", "Deferred Tax Income", "Export Sales", "Investment Gain"]
    total_income = sum(t["amount"] for t in TRANSACTIONS if t["type"] == "credit" and t["category"] in income_cats)
    
    expense_exclude = asset_cats + liab_cats + equity_cats + income_cats + ["Loan Repayment", "Dividend Payment", "Share Issue Expense", "Debenture Redemption", "Share Buyback", "Tax Payment", "Advance Tax", "Preference Share Redemption", "Dividend Declaration", "Profit Appropriation", "Closing Entry", "COGS"]
    total_expenses = sum(t["amount"] for t in TRANSACTIONS if t["type"] == "debit" and t["category"] not in expense_exclude)
    
    # Add explicit COGS from the closing entries if present
    cogs = sum(t["amount"] for t in TRANSACTIONS if t["category"] == "COGS")
    
    net_profit = total_income - (total_expenses + cogs)
    
    # Deduct dividends paid directly from profit for equity calculation
    dividends_paid = sum(t["amount"] for t in TRANSACTIONS if "Dividend" in t["category"] and t["type"] == "debit")
    retained_earnings = net_profit - dividends_paid
    
    total_assets = cash_at_bank + other_assets
    total_liabilities_and_equity = total_liabilities + capital + retained_earnings

    return {
        "assets": {
            "Cash & Bank Balance": round(cash_at_bank, 2),
            "Non-Current Assets": round(other_assets, 2)
        },
        "liabilities": {
            "Total Liabilities": round(total_liabilities, 2)
        },
        "equity": {
            "Shareholders Funds": round(capital, 2),
            "Retained Earnings": round(retained_earnings, 2)
        },
        "total_assets": round(total_assets, 2),
        "total_liabilities_and_equity": round(total_liabilities_and_equity, 2),
        "is_balanced": abs(total_assets - total_liabilities_and_equity) < 1.0
    }


@router.get("/cashflow-statement")
def cashflow_statement():
    """
    Corporate Cash Flow Statement: Operating, Investing, Financing
    """
    # 1. Operating
    cash_from_customers = sum(t["amount"] for t in TRANSACTIONS if t["category"] == "Revenue")
    cash_to_suppliers = sum(t["amount"] for t in TRANSACTIONS if t["category"] == "Vendor Payment")
    gst_movements = sum(t["amount"] for t in TRANSACTIONS if t["category"] == "GST Refund") - \
                    sum(t["amount"] for t in TRANSACTIONS if t["category"] == "GST Payment")
    
    operating_cats = ["Salary Expense", "Rent Expense", "Utility Expense", "Miscellaneous", "Professional Fees", "Bad Debt"]
    cash_for_ops = sum(t["amount"] for t in TRANSACTIONS if t["category"] in operating_cats)
    
    net_operating = cash_from_customers - (cash_to_suppliers + cash_for_ops) + gst_movements

    # 2. Investing
    fixed_asset_purchase = sum(t["amount"] for t in TRANSACTIONS if t["category"] == "Fixed Asset")
    investing_income = sum(t["amount"] for t in TRANSACTIONS if t["category"] == "Investing Income")
    net_investing = investing_income - fixed_asset_purchase

    # 3. Financing
    loans_in = sum(t["amount"] for t in TRANSACTIONS if t["category"] == "Loan Received")
    loans_out = sum(t["amount"] for t in TRANSACTIONS if t["category"] == "Loan Repayment")
    finance_costs = sum(t["amount"] for t in TRANSACTIONS if t["category"] in ["Bank Charges", "Finance Cost"])
    dividends = sum(t["amount"] for t in TRANSACTIONS if t["category"] == "Dividend Paid")
    
    net_financing = loans_in - (loans_out + finance_costs + dividends)

    return {
        "operating": {
            "Cash from Customers": cash_from_customers,
            "Cash to Suppliers & Ops": -(cash_to_suppliers + cash_for_ops),
            "Net GST Movements": gst_movements,
            "subtotal": net_operating
        },
        "investing": {
            "Purchase of Assets": -fixed_asset_purchase,
            "Investment Income": investing_income,
            "subtotal": net_investing
        },
        "financing": {
            "New Loans Received": loans_in,
            "Loan & Finance Costs": -(loans_out + finance_costs),
            "Dividends Paid": -dividends,
            "subtotal": net_financing
        },
        "net_change": net_operating + net_investing + net_financing,
        "closing_cash": sum(t["amount"] if t["type"] == "credit" else -t["amount"] for t in TRANSACTIONS)
    }


@router.get("/income-statement")
def income_statement():
    """
    Feature Six: Formal P&L with COGS, EBIT, and Margins.
    """
    total_revenue = sum(t["amount"] for t in TRANSACTIONS if t["category"] == "Revenue")
    cogs = sum(t["amount"] for t in TRANSACTIONS if t["category"] == "Vendor Payment")
    gross_profit = total_revenue - cogs

    operating_expenses = sum(t["amount"] for t in TRANSACTIONS if t["category"] in ["Salary Expense", "Rent Expense", "Utility Expense", "Miscellaneous"])
    ebit = gross_profit - operating_expenses

    finance_costs = sum(t["amount"] for t in TRANSACTIONS if t["category"] in ["Bank Charges", "Loan Repayment"])
    pbt = ebit - finance_costs

    tax = pbt * 0.25
    net_profit = pbt - tax

    return {
        "revenue": total_revenue,
        "cogs": cogs,
        "gross_profit": gross_profit,
        "operating_expenses": operating_expenses,
        "ebit": ebit,
        "finance_costs": finance_costs,
        "pbt": pbt,
        "tax": tax,
        "net_profit": net_profit,
        "margins": {
            "gross": (gross_profit / total_revenue * 100) if total_revenue else 0,
            "net": (net_profit / total_revenue * 100) if total_revenue else 0
        }
    }
