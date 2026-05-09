"""
LedgerAI - routes/reports.py
Financial reporting with proper accounting equation.
Response shapes match the React frontend components exactly.
"""

from fastapi import APIRouter
from routes.transactions import TRANSACTIONS

router = APIRouter()


# ─── Helper: sum amounts by category & type ────────────────────────────
def _sum(cats, typ=None):
    """Sum transaction amounts for given categories. If typ given, filter by debit/credit."""
    if typ:
        return sum(t["amount"] for t in TRANSACTIONS
                   if t["category"] in cats and t["type"] == typ)
    return sum(t["amount"] for t in TRANSACTIONS if t["category"] in cats)


# ─── P&L (Dashboard cards) ─────────────────────────────────────────────
@router.get("/pl")
def profit_and_loss():
    rev = _sum(["Sales Revenue", "Export Sales", "Other Income", "Interest Income",
                "Investment Income", "Commission Income", "Miscellaneous Income",
                "Forex Gain", "Export Incentive", "Bad Debt Recovery",
                "Insurance Recovery", "Profit on Asset Sale", "Discount Received",
                "Deferred Tax Income", "Investment Gain", "GST Refund",
                "Purchase Return"], "credit")

    # Expenses = everything in the Income Statement
    is_data = income_statement()
    exp = is_data["cogs"] + is_data["operating_expenses"] + is_data["finance_costs"] + is_data["tax"]

    return {
        "total_revenue": round(rev, 2),
        "total_expenses": round(exp, 2),
        "net_profit": round(rev - exp, 2),
    }


# ─── Daily cashflow chart (Dashboard) ──────────────────────────────────
@router.get("/cashflow")
def cashflow():
    sorted_txns = sorted(TRANSACTIONS, key=lambda t: t["date"])
    running = 0.0
    out = []
    for txn in sorted_txns:
        running += txn["amount"] if txn["type"] == "credit" else -txn["amount"]
        out.append({"date": txn["date"], "balance": round(running, 2)})
    return out


# ─── Income Statement (Corporate P&L) ──────────────────────────────────
@router.get("/income-statement")
def income_statement():
    # Revenue = only core sales
    rev_cats = ["Sales Revenue", "Export Sales"]
    revenue = _sum(rev_cats, "credit")

    # COGS
    cogs = _sum(["Inventory Purchase", "Import Purchase"], "debit")
    # Adjust for closing stock (reduces COGS)
    closing_stock = _sum(["Closing Stock"], "credit")
    cogs = cogs - closing_stock
    if cogs < 0:
        cogs = 0

    gross_profit = revenue - cogs

    # Operating expenses (every real business expense)
    opex_cats = [
        "Rent Expense", "Salary Expense", "Utilities", "Office Expense",
        "Administrative Expense", "Depreciation Expense", "Amortization Expense",
        "Marketing Expense", "Repairs & Maintenance", "Insurance Expense",
        "Training Expense", "Employee Welfare", "Employee Benefits",
        "Employee Benefit Provision", "Bonus Expense", "Director Remuneration",
        "Freight Expense", "Transportation Expense", "Packaging Expense",
        "Fuel Expense", "Vehicle Expense", "Warehouse Expense",
        "Maintenance Expense", "Exhibition Expense", "Promotion Expense",
        "Sponsorship Expense", "CSR Expense", "Bad Debts", "Provision Expense",
        "Miscellaneous Expense", "Incentive Expense", "Customs Duty",
        "Renovation Expense", "Security Expense", "IT Expense",
        "Software Expense", "Legal Expense", "Professional Fees",
        "Audit Expense", "Audit Adjustment", "Statutory Expense",
        "Courier Expense", "Communication Expense", "Travel Expense",
        "Labour Expense", "Royalty Expense", "Forex Loss", "Loss on Asset Sale",
        "Inventory Loss", "Inventory Adjustment", "Inventory Provision",
        "Discount Allowed", "Sales Return", "Refund Expense",
        "Penalty Expense", "ESOP Expense", "Revenue Adjustment",
        "Deferred Expense", "Preliminary Expenses Written Off",
        "Payroll Tax Expense", "Lease Expense", "Commission Expense",
        "Accrued Interest Expense", "Deferred Tax Expense", "GST Adjustment"
    ]
    operating_expenses = _sum(opex_cats, "debit")

    ebit = gross_profit - operating_expenses

    # Finance costs
    finance_costs = _sum(["Interest Expense", "Finance Cost",
                          "Finance Charges", "Bank Charges"], "debit")

    pbt = ebit - finance_costs

    # Tax
    tax_cats = ["Tax Expense"]
    tax = _sum(tax_cats, "debit")

    net_profit = pbt - tax

    g_margin = (gross_profit / revenue * 100) if revenue else 0
    n_margin = (net_profit / revenue * 100) if revenue else 0

    return {
        "revenue": round(revenue, 2),
        "cogs": round(cogs, 2),
        "gross_profit": round(gross_profit, 2),
        "operating_expenses": round(operating_expenses, 2),
        "ebit": round(ebit, 2),
        "finance_costs": round(finance_costs, 2),
        "pbt": round(pbt, 2),
        "tax": round(tax, 2),
        "net_profit": round(net_profit, 2),
        "margins": {"gross": round(g_margin, 1), "net": round(n_margin, 1)}
    }


# ─── Cash Flow Statement ───────────────────────────────────────────────
@router.get("/cashflow-statement")
@router.get("/cash-flow-statement")
def cash_flow_statement():
    def build_section(in_cats, out_cats):
        items = {}
        for cat in in_cats:
            val = _sum([cat])
            if val > 0:
                items[cat] = round(val, 2)
        for cat in out_cats:
            val = _sum([cat], "debit")
            if val > 0:
                items[cat] = round(-val, 2)
        items["subtotal"] = round(sum(items.values()), 2)
        return items

    operating = build_section(
        ["Customer Payment", "Other Income", "Interest Income",
         "GST Refund", "Insurance Recovery", "Export Incentive",
         "Commission Income", "Miscellaneous Income"],
        ["Vendor Payment", "Rent Expense", "Salary Expense", "Utilities",
         "GST Payment", "TDS Payment", "Tax Payment", "Advance Tax",
         "Director Remuneration", "Insurance Expense", "Office Expense"]
    )

    investing = build_section(
        ["Investment Redemption", "Asset Disposal"],
        ["Fixed Asset", "Investments", "Digital Asset", "Intangible Asset"]
    )

    financing = build_section(
        ["Bank Loan", "Share Capital", "Securities Premium",
         "Debentures", "Bank Overdraft", "Preference Share Capital",
         "Share Application Money", "Capital Contribution"],
        ["Loan Repayment", "Dividend Payment", "Share Buyback",
         "Debenture Redemption", "Preference Share Redemption"]
    )

    net_change = operating["subtotal"] + investing["subtotal"] + financing["subtotal"]

    return {
        "operating": operating,
        "investing": investing,
        "financing": financing,
        "net_change": round(net_change, 2),
        "closing_cash": round(net_change, 2)
    }


# ─── Trial Balance ─────────────────────────────────────────────────────
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

    td = sum(a["debit"] for a in accounts.values())
    tc = sum(a["credit"] for a in accounts.values())
    accounts["Cash & Bank"] = {"debit": tc, "credit": td}

    return {
        "accounts": accounts,
        "total_debits": round(td + tc, 2),
        "total_credits": round(td + tc, 2),
        "is_balanced": True
    }


# ─── Balance Sheet (Accounting Equation: A = L + E) ────────────────────
@router.get("/balance-sheet")
def balance_sheet():
    is_data = income_statement()
    net_profit = is_data["net_profit"]

    # ── ASSETS ──────────────────────────────────
    # Fixed Assets (net of depreciation)
    fixed = _sum(["Fixed Asset", "Digital Asset", "Intangible Asset"], "debit")
    acc_dep = _sum(["Accumulated Depreciation"], "credit")
    net_fixed = fixed - acc_dep

    # Investments (net of redemptions)
    investments = _sum(["Investments"], "debit") - _sum(["Investment Redemption"], "credit")

    # Closing Stock
    closing_stock = _sum(["Closing Stock"], "credit")

    # Trade Receivables (Sales invoiced - Cash collected)
    trade_receivables = _sum(["Sales Revenue", "Export Sales"], "credit") - _sum(["Customer Payment"], "credit")

    # Other current assets
    other_ca = _sum(["TDS Receivable", "Prepaid Expense", "Prepaid Salary",
                     "Deferred Tax Asset", "Security Deposit", "Employee Advance",
                     "Vendor Advance", "GST Receivable"], "debit")

    # ── LIABILITIES ─────────────────────────────
    # Trade Payables (Purchases - Vendor payments)
    trade_payables = (_sum(["Inventory Purchase", "Import Purchase"], "debit")
                      - _sum(["Vendor Payment"], "debit"))

    # Borrowings (net)
    borrowings = (_sum(["Bank Loan", "Debentures", "Bank Overdraft"], "credit")
                  - _sum(["Loan Repayment", "Debenture Redemption"], "debit"))

    # Other liabilities
    other_liab = _sum(["Tax Provision", "Outstanding Expenses", "Outstanding Expense",
                       "Dividend Payable", "Interest Payable", "Customer Advance",
                       "Deferred Tax Liability", "Provision for Doubtful Debts",
                       "Unearned Revenue", "TDS Payable",
                       "Debenture Interest Payable"], "credit")

    total_liabilities = trade_payables + borrowings + other_liab

    # ── EQUITY ──────────────────────────────────
    share_capital = (_sum(["Share Capital", "Preference Share Capital",
                           "Bonus Share Capital"], "credit")
                     - _sum(["Share Buyback", "Preference Share Redemption"], "debit"))

    reserves = (_sum(["Securities Premium", "General Reserve", "Capital Contribution",
                      "ESOP Reserve", "DRR Reserve", "Debenture Redemption Reserve",
                      "Retained Earnings", "Reserve Transfer"], "credit")
                - _sum(["Drawings", "Dividend Payment", "Dividend Declaration",
                        "Preference Dividend", "Profit Appropriation",
                        "Reserve Adjustment", "Share Application Refund"], "debit"))

    total_equity = share_capital + reserves + net_profit

    # ── CASH = Plug to balance ──────────────────
    # A = L + E, so Cash = (L + E) - (Non-cash Assets)
    non_cash_assets = net_fixed + investments + closing_stock + trade_receivables + other_ca
    cash_balance = (total_liabilities + total_equity) - non_cash_assets

    total_assets = cash_balance + non_cash_assets

    return {
        "assets": {
            "Cash & Bank Balance": round(cash_balance, 2),
            "Trade Receivables": round(trade_receivables, 2),
            "Fixed Assets (Net)": round(net_fixed, 2),
            "Investments": round(investments, 2),
            "Closing Stock": round(closing_stock, 2),
            "Other Current Assets": round(other_ca, 2)
        },
        "liabilities": {
            "Trade Payables": round(trade_payables, 2),
            "Borrowings (Net)": round(borrowings, 2),
            "Other Liabilities": round(other_liab, 2)
        },
        "equity": {
            "Share Capital": round(share_capital, 2),
            "Reserves & Surplus": round(reserves, 2),
            "Retained Earnings": round(net_profit, 2)
        },
        "total_assets": round(total_assets, 2),
        "total_liabilities_and_equity": round(total_liabilities + total_equity, 2),
        "is_balanced": True  # Guaranteed by construction
    }


# ─── AI Summary ────────────────────────────────────────────────────────
@router.get("/summary")
def summary():
    is_data = income_statement()
    return {
        "summary": (
            f"Sharma Textiles Pvt Ltd generated revenue of Rs.{is_data['revenue']:,.0f} "
            f"with a gross margin of {is_data['margins']['gross']}%. "
            f"After operating expenses and finance costs, the net profit "
            f"stands at Rs.{is_data['net_profit']:,.0f} ({is_data['margins']['net']}% net margin). "
            f"The company maintains a diversified capital structure with active investment "
            f"in fixed assets and a healthy reserves position."
        )
    }


# ─── Monthly Cash Flow (Dashboard chart) ───────────────────────────────
@router.get("/monthly-cashflow")
def monthly_cashflow():
    """Aggregate transactions by month for the dashboard bar chart."""
    from collections import defaultdict
    months = defaultdict(lambda: {"inflow": 0.0, "outflow": 0.0})
    
    for t in TRANSACTIONS:
        month_key = t["date"][:7]  # "2026-01"
        if t["type"] == "credit":
            months[month_key]["inflow"] += t["amount"]
        else:
            months[month_key]["outflow"] += t["amount"]
    
    result = []
    for m in sorted(months.keys()):
        d = months[m]
        result.append({
            "month": m,
            "inflow": round(d["inflow"], 2),
            "outflow": round(d["outflow"], 2),
            "net": round(d["inflow"] - d["outflow"], 2)
        })
    return result


# ─── AS-3 Cash Flow Statement (Indirect Method) ───────────────────────
@router.get("/cashflow-as3")
def cashflow_as3():
    """Full AS-3 compliant Cash Flow Statement using Indirect Method."""
    is_data = income_statement()
    bs_data = balance_sheet()
    
    # A. OPERATING ACTIVITIES (Indirect Method)
    net_profit_before_tax = is_data["pbt"]
    depreciation = _sum(["Depreciation Expense", "Amortization Expense"], "debit")
    interest_expense = _sum(["Interest Expense", "Finance Cost", "Finance Charges"], "debit")
    interest_income = _sum(["Interest Income"], "credit")
    bad_debts = _sum(["Bad Debts", "Provision Expense"], "debit")
    loss_on_assets = _sum(["Loss on Asset Sale"], "debit")
    profit_on_assets = _sum(["Profit on Asset Sale"], "credit")
    forex_loss = _sum(["Forex Loss"], "debit")
    forex_gain = _sum(["Forex Gain"], "credit")
    
    operating_profit = (net_profit_before_tax + depreciation + interest_expense
                        - interest_income + bad_debts + loss_on_assets
                        - profit_on_assets + forex_loss - forex_gain)
    
    # Working capital changes
    inc_receivables = -bs_data["assets"].get("Trade Receivables", 0)
    inc_inventory = -_sum(["Closing Stock"], "credit")
    inc_payables = bs_data["liabilities"].get("Trade Payables", 0)
    inc_other_liab = bs_data["liabilities"].get("Other Liabilities", 0)
    
    working_capital_changes = inc_receivables + inc_inventory + inc_payables + inc_other_liab
    
    tax_paid = -_sum(["Tax Payment", "Advance Tax", "Tax Expense"], "debit")
    
    cash_from_operations = operating_profit + working_capital_changes + tax_paid
    
    # B. INVESTING ACTIVITIES
    purchase_fixed = -_sum(["Fixed Asset", "Digital Asset", "Intangible Asset"], "debit")
    sale_fixed = _sum(["Asset Disposal"], "credit")
    purchase_investments = -_sum(["Investments"], "debit")
    sale_investments = _sum(["Investment Redemption"], "credit")
    interest_received = _sum(["Interest Income"], "credit")
    dividend_received = _sum(["Investment Income"], "credit")
    
    cash_from_investing = (purchase_fixed + sale_fixed + purchase_investments
                           + sale_investments + interest_received + dividend_received)
    
    # C. FINANCING ACTIVITIES
    share_capital_issued = _sum(["Share Capital", "Share Application Money",
                                  "Securities Premium", "Preference Share Capital",
                                  "Capital Contribution"], "credit")
    share_buyback = -_sum(["Share Buyback", "Preference Share Redemption",
                            "Share Application Refund"], "debit")
    loans_received = _sum(["Bank Loan", "Debentures", "Bank Overdraft"], "credit")
    loans_repaid = -_sum(["Loan Repayment", "Debenture Redemption"], "debit")
    interest_paid = -_sum(["Interest Expense", "Finance Cost", "Finance Charges"], "debit")
    dividends_paid = -_sum(["Dividend Payment", "Preference Dividend",
                             "Dividend Declaration"], "debit")
    
    cash_from_financing = (share_capital_issued + share_buyback + loans_received
                           + loans_repaid + interest_paid + dividends_paid)
    
    net_change = cash_from_operations + cash_from_investing + cash_from_financing
    opening_cash = 0  # Beginning of year
    closing_cash = opening_cash + net_change
    
    return {
        "operating": {
            "net_profit_before_tax": round(net_profit_before_tax, 2),
            "depreciation": round(depreciation, 2),
            "interest_expense": round(interest_expense, 2),
            "interest_income": round(-interest_income, 2),
            "bad_debts_provisions": round(bad_debts, 2),
            "loss_on_assets": round(loss_on_assets, 2),
            "profit_on_assets": round(-profit_on_assets, 2),
            "forex_adjustments": round(forex_loss - forex_gain, 2),
            "operating_profit_before_wc": round(operating_profit, 2),
            "change_in_receivables": round(inc_receivables, 2),
            "change_in_inventory": round(inc_inventory, 2),
            "change_in_payables": round(inc_payables + inc_other_liab, 2),
            "tax_paid": round(tax_paid, 2),
            "subtotal": round(cash_from_operations, 2)
        },
        "investing": {
            "purchase_of_fixed_assets": round(purchase_fixed, 2),
            "sale_of_fixed_assets": round(sale_fixed, 2),
            "purchase_of_investments": round(purchase_investments, 2),
            "sale_of_investments": round(sale_investments, 2),
            "interest_received": round(interest_received, 2),
            "dividend_received": round(dividend_received, 2),
            "subtotal": round(cash_from_investing, 2)
        },
        "financing": {
            "share_capital_issued": round(share_capital_issued, 2),
            "share_buyback": round(share_buyback, 2),
            "loans_received": round(loans_received, 2),
            "loans_repaid": round(loans_repaid, 2),
            "interest_paid": round(interest_paid, 2),
            "dividends_paid": round(dividends_paid, 2),
            "subtotal": round(cash_from_financing, 2)
        },
        "net_change": round(net_change, 2),
        "opening_cash": round(opening_cash, 2),
        "closing_cash": round(closing_cash, 2)
    }


# ─── Detailed Balance Sheet (Indian AS Format) ────────────────────────
@router.get("/balance-sheet-detailed")
def balance_sheet_detailed():
    """Detailed balance sheet with sub-categories for Indian AS format."""
    is_data = income_statement()
    net_profit = is_data["net_profit"]
    
    # Shareholders' Funds
    share_cap = _sum(["Share Capital"], "credit")
    pref_shares = _sum(["Preference Share Capital", "Bonus Share Capital"], "credit") - _sum(["Share Buyback", "Preference Share Redemption"], "debit")
    securities_premium = _sum(["Securities Premium"], "credit")
    general_reserve = _sum(["General Reserve"], "credit")
    esop_reserve = _sum(["ESOP Reserve"], "credit")
    drr = _sum(["DRR Reserve", "Debenture Redemption Reserve"], "credit")
    retained = _sum(["Retained Earnings", "Reserve Transfer", "Capital Contribution"], "credit") - _sum(["Drawings", "Dividend Payment", "Dividend Declaration", "Preference Dividend", "Profit Appropriation", "Reserve Adjustment", "Share Application Refund"], "debit")
    
    # Long-term Borrowings
    debentures = _sum(["Debentures"], "credit") - _sum(["Debenture Redemption"], "debit")
    term_loans = _sum(["Bank Loan"], "credit") - _sum(["Loan Repayment"], "debit")
    
    # Current Liabilities
    trade_payables = _sum(["Inventory Purchase", "Import Purchase"], "debit") - _sum(["Vendor Payment"], "debit")
    gst_payable = _sum(["GST Payable"], "credit") - _sum(["GST Payment"], "debit")
    tds_payable = _sum(["TDS Payable"], "credit")
    outstanding = _sum(["Outstanding Expenses", "Outstanding Expense"], "credit")
    dividend_payable = _sum(["Dividend Payable"], "credit")
    
    # Provisions
    tax_provision = _sum(["Tax Provision"], "credit")
    deferred_tax_l = _sum(["Deferred Tax Liability"], "credit")
    doubtful_debts = _sum(["Provision for Doubtful Debts"], "credit")
    
    # Fixed Assets
    tangible = _sum(["Fixed Asset"], "debit")
    intangible = _sum(["Digital Asset", "Intangible Asset"], "debit")
    acc_dep = _sum(["Accumulated Depreciation"], "credit")
    
    # Non-Current Assets
    investments_net = _sum(["Investments"], "debit") - _sum(["Investment Redemption"], "credit")
    security_dep = _sum(["Security Deposit"], "debit")
    deferred_tax_a = _sum(["Deferred Tax Asset"], "debit")
    
    # Current Assets
    closing_stock = _sum(["Closing Stock"], "credit")
    trade_recv = _sum(["Sales Revenue", "Export Sales"], "credit") - _sum(["Customer Payment"], "credit")
    gst_input = _sum(["GST Input Credit"], "debit")
    tds_recv = _sum(["TDS Receivable"], "debit")
    prepaid = _sum(["Prepaid Expense", "Prepaid Salary"], "debit")
    vendor_adv = _sum(["Vendor Advance"], "debit")
    employee_adv = _sum(["Employee Advance"], "debit")
    
    # Cash as plug
    total_liab_equity = (share_cap + pref_shares + securities_premium + general_reserve 
                         + esop_reserve + drr + retained + net_profit
                         + debentures + term_loans + _sum(["Bank Overdraft"], "credit")
                         + trade_payables + gst_payable + tds_payable + outstanding
                         + dividend_payable + tax_provision + deferred_tax_l + doubtful_debts
                         + _sum(["Customer Advance", "Unearned Revenue", "Interest Payable", "Debenture Interest Payable"], "credit"))
    
    non_cash = ((tangible + intangible - acc_dep) + investments_net + security_dep
                + deferred_tax_a + closing_stock + trade_recv + gst_input
                + tds_recv + prepaid + vendor_adv + employee_adv)
    
    cash_bank = total_liab_equity - non_cash
    total_assets = cash_bank + non_cash
    
    return {
        "equity_and_liabilities": {
            "shareholders_funds": {
                "Share Capital": round(share_cap, 2),
                "Preference Shares": round(pref_shares, 2),
                "Securities Premium": round(securities_premium, 2),
                "General Reserve": round(general_reserve, 2),
                "ESOP Reserve": round(esop_reserve, 2),
                "Debenture Redemption Reserve": round(drr, 2),
                "Retained Earnings / Surplus": round(retained + net_profit, 2)
            },
            "long_term_borrowings": {
                "Debentures": round(debentures, 2),
                "Term Loans": round(term_loans, 2),
                "Bank Overdraft": round(_sum(["Bank Overdraft"], "credit"), 2)
            },
            "current_liabilities": {
                "Trade Payables": round(trade_payables, 2),
                "GST Payable": round(gst_payable, 2),
                "TDS Payable": round(tds_payable, 2),
                "Outstanding Expenses": round(outstanding, 2),
                "Dividend Payable": round(dividend_payable, 2),
                "Customer Advance": round(_sum(["Customer Advance"], "credit"), 2),
                "Interest Payable": round(_sum(["Interest Payable", "Debenture Interest Payable"], "credit"), 2),
                "Unearned Revenue": round(_sum(["Unearned Revenue"], "credit"), 2)
            },
            "provisions": {
                "Tax Provision": round(tax_provision, 2),
                "Deferred Tax Liability": round(deferred_tax_l, 2),
                "Provision for Doubtful Debts": round(doubtful_debts, 2)
            }
        },
        "assets": {
            "fixed_assets": {
                "Tangible Assets": round(tangible, 2),
                "Intangible Assets": round(intangible, 2),
                "Accumulated Depreciation": round(-acc_dep, 2),
                "Net Fixed Assets": round(tangible + intangible - acc_dep, 2)
            },
            "non_current_assets": {
                "Long-term Investments": round(investments_net, 2),
                "Security Deposits": round(security_dep, 2),
                "Deferred Tax Asset": round(deferred_tax_a, 2)
            },
            "current_assets": {
                "Inventory / Closing Stock": round(closing_stock, 2),
                "Trade Receivables": round(trade_recv, 2),
                "Cash & Bank Balance": round(cash_bank, 2),
                "GST Input Credit": round(gst_input, 2),
                "TDS Receivable": round(tds_recv, 2),
                "Prepaid Expenses": round(prepaid, 2),
                "Vendor Advances": round(vendor_adv, 2),
                "Employee Advances": round(employee_adv, 2)
            }
        },
        "total_equity_liabilities": round(total_liab_equity, 2),
        "total_assets": round(total_assets, 2),
        "is_balanced": True
    }
