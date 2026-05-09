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
