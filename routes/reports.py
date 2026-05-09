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
    Feature Four: Assets = Liabilities + (Capital + Net Profit)
    """
    # 1. Assets
    cash_at_bank = sum(t["amount"] if t["type"] == "credit" else -t["amount"] for t in TRANSACTIONS)
    # Estimate receivables as 10% of revenue
    receivables = sum(t["amount"] for t in TRANSACTIONS if t["category"] == "Revenue") * 0.10
    total_assets = cash_at_bank + receivables

    # 2. Liabilities
    # Estimate payables as 10% of vendor payments
    payables = sum(t["amount"] for t in TRANSACTIONS if t["category"] == "Vendor Payment") * 0.10
    total_liabilities = payables

    # 3. Equity (Capital + Retained Earnings)
    initial_capital = sum(t["amount"] for t in TRANSACTIONS if t["category"] == "Equity")
    
    total_revenue = sum(t["amount"] for t in TRANSACTIONS if t["type"] == "credit" and t["category"] != "Equity")
    total_expenses = sum(t["amount"] for t in TRANSACTIONS if t["type"] == "debit")
    net_profit = total_revenue - total_expenses
    
    total_equity = initial_capital + net_profit

    # The final check: Assets + Adjustment vs Liabilities + Equity
    # We add receivables to Assets and payables to Liabilities to simulate accrual
    return {
        "assets": {
            "Cash & Bank Balance": round(cash_at_bank, 2),
            "Accounts Receivable": round(receivables, 2)
        },
        "liabilities": {
            "Accounts Payable": round(payables, 2)
        },
        "equity": {
            "Shareholders Capital": round(initial_capital, 2),
            "Retained Earnings (Profit)": round(net_profit, 2)
        },
        "total_assets": round(total_assets, 2),
        "total_liabilities_and_equity": round(total_liabilities + total_equity, 2),
        "is_balanced": abs(total_assets - (total_liabilities + total_equity)) < 1.0
    }


@router.get("/cashflow-statement")
def cashflow_statement():
    """
    Feature Five: Operating, Investing, and Financing activities.
    """
    # Operating
    cash_from_customers = sum(t["amount"] for t in TRANSACTIONS if t["category"] == "Revenue")
    cash_to_suppliers = sum(t["amount"] for t in TRANSACTIONS if t["category"] == "Vendor Payment")
    cash_for_ops = sum(t["amount"] for t in TRANSACTIONS if t["category"] in ["Salary Expense", "Rent Expense", "Utility Expense", "Miscellaneous"])
    gst_tax_paid = sum(t["amount"] for t in TRANSACTIONS if t["category"] in ["GST Payment", "TDS Payment"])
    
    net_operating = cash_from_customers - (cash_to_suppliers + cash_for_ops + gst_tax_paid)

    # Financing
    loan_repayments = sum(t["amount"] for t in TRANSACTIONS if t["category"] == "Loan Repayment")
    bank_charges = sum(t["amount"] for t in TRANSACTIONS if t["category"] == "Bank Charges")
    
    net_financing = -(loan_repayments + bank_charges)

    return {
        "operating": {
            "Cash from Customers": cash_from_customers,
            "Cash to Suppliers": -cash_to_suppliers,
            "Operating Expenses": -cash_for_ops,
            "Tax & GST Paid": -gst_tax_paid,
            "subtotal": net_operating
        },
        "financing": {
            "Loan Repayments": -loan_repayments,
            "Bank Charges": -bank_charges,
            "subtotal": net_financing
        },
        "net_change": net_operating + net_financing,
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
