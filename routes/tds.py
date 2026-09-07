"""
LedgerAI - routes/tds.py
Instant Auto-TDS Engine:
- Classifies vendor payments under Indian Income Tax Act 1961 Chapter XVII-B
- Splits into 3-leg double entry: Debit Expense, Credit TDS Payable, Credit Vendor Payable
- Generates Challan 281 monthly summaries and Form 26Q quarterly reports
"""

import os
import json
from datetime import datetime
from typing import Optional, List
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter()

# Load TDS rules
RULES_FILE = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "tds_rules.json")

def load_tds_rules():
    if os.path.exists(RULES_FILE):
        with open(RULES_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

# In-memory store of processed TDS transactions for session tracking
PROCESSED_TDS_ENTRIES = []

class TDSProcessRequest(BaseModel):
    vendor_name: str
    description: str
    amount: float
    vendor_type: Optional[str] = "company"  # individual or company
    invoice_date: Optional[str] = None

class TDSRuleResponse(BaseModel):
    section_code: str
    description: str
    nature: str
    rate_individual: float
    rate_company: float
    threshold_single: float
    threshold_aggregate: float
    challan_code: str
    keywords: List[str]

def classify_vendor_payment(vendor_name: str, description: str, rules: list):
    """
    Classifies vendor payment against TDS rules using keyword heuristics.
    """
    text = f"{vendor_name} {description}".lower()
    
    best_rule = None
    best_score = 0
    
    for rule in rules:
        score = 0
        for kw in rule.get("keywords", []):
            if kw in text:
                score += len(kw)  # longer keyword matches are higher confidence
        if score > best_score:
            best_score = score
            best_rule = rule

    # Default fallback: 194C (Works / Services) if amount > threshold, or 194J(a)
    if not best_rule:
        for r in rules:
            if r["section_code"] == "194C":
                best_rule = r
                break
                
    return best_rule

def determine_expense_account(section_code: str, description: str):
    desc = description.lower()
    if section_code.startswith("194I"):
        return "Rent Expense"
    if section_code == "194H":
        return "Commission Expense"
    if section_code == "194Q":
        return "Purchase Expense"
    if "legal" in desc or "lawyer" in desc:
        return "Legal & Professional Expense"
    if "audit" in desc or "ca" in desc:
        return "Audit Fees"
    if "aws" in desc or "software" in desc or "cloud" in desc or "technical" in desc:
        return "Software & Technical Expense"
    if "contractor" in desc or "labour" in desc:
        return "Contract Labour Expense"
    return "Professional & Technical Expense"

@router.get("/rules")
def get_rules():
    """Returns available Indian TDS sections and thresholds"""
    return load_tds_rules()

@router.post("/process")
def process_tds(req: TDSProcessRequest):
    """
    Processes vendor transaction:
    - Identifies applicable TDS section
    - Calculates TDS and Net Payable
    - Generates 3-leg Journal Entry:
      1. Debit: Expense Account (Gross)
      2. Credit: TDS Payable (TDS deduction)
      3. Credit: Vendor Payable (Net payable)
    """
    if req.amount <= 0:
        raise HTTPException(status_code=400, detail="Amount must be positive")

    rules = load_tds_rules()
    rule = classify_vendor_payment(req.vendor_name, req.description, rules)
    
    is_company = (req.vendor_type or "company").lower() == "company"
    rate = rule["rate_company"] if is_company else rule["rate_individual"]
    
    tds_amount = round(req.amount * (rate / 100.0), 2)
    net_payable = round(req.amount - tds_amount, 2)
    expense_account = determine_expense_account(rule["section_code"], req.description)
    date_str = req.invoice_date or datetime.now().strftime("%Y-%m-%d")

    split_entry = {
        "debit_expense": {
            "account": expense_account,
            "type": "Debit",
            "amount": req.amount
        },
        "credit_tds_payable": {
            "account": f"TDS Payable u/s {rule['section_code']}",
            "type": "Credit",
            "amount": tds_amount
        },
        "credit_vendor_payable": {
            "account": f"{req.vendor_name} Payable",
            "type": "Credit",
            "amount": net_payable
        },
        "narration": f"Being {req.description} provided by {req.vendor_name}, TDS deducted u/s {rule['section_code']} @ {rate}%",
        "section_code": rule["section_code"],
        "nature": rule["nature"],
        "challan_code": rule["challan_code"],
        "tds_rate": rate,
        "date": date_str,
        "vendor_name": req.vendor_name,
        "gross_amount": req.amount,
        "tds_amount": tds_amount,
        "net_payable": net_payable
    }

    # Track in session
    PROCESSED_TDS_ENTRIES.append(split_entry)

    return split_entry

@router.get("/challan")
def get_challan_summary(month: Optional[int] = None, year: Optional[int] = None):
    """
    Returns monthly Challan 281 aggregation by TDS section.
    """
    now = datetime.now()
    target_month = month if month is not None else now.month
    target_year = year if year is not None else now.year

    entries = [
        e for e in PROCESSED_TDS_ENTRIES 
        if datetime.strptime(e["date"], "%Y-%m-%d").month == target_month 
        and datetime.strptime(e["date"], "%Y-%m-%d").year == target_year
    ]

    breakdown = {}
    for e in entries:
        sec = e["section_code"]
        if sec not in breakdown:
            breakdown[sec] = {
                "section_code": sec,
                "nature": e["nature"],
                "challan_code": e["challan_code"],
                "total_tds": 0.0,
                "count": 0
            }
        breakdown[sec]["total_tds"] = round(breakdown[sec]["total_tds"] + e["tds_amount"], 2)
        breakdown[sec]["count"] += 1

    total_tds = sum(b["total_tds"] for b in breakdown.values())
    
    # Next month's 7th is due date
    due_month = target_month + 1 if target_month < 12 else 1
    due_year = target_year if target_month < 12 else target_year + 1
    due_date = f"{due_year}-{due_month:02d}-07"

    return {
        "challan_no": "ITNS 281",
        "month": target_month,
        "year": target_year,
        "due_date": due_date,
        "total_tds": round(total_tds, 2),
        "sections": list(breakdown.values()),
        "total_deductions": len(entries)
    }

@router.get("/form26q")
def get_form26q(quarter: Optional[int] = 2, financial_year: Optional[str] = "2026-27"):
    """
    Returns quarterly Form 26Q summary (Payments other than Salary).
    """
    quarter_months = {
        1: [4, 5, 6],
        2: [7, 8, 9],
        3: [10, 11, 12],
        4: [1, 2, 3]
    }
    target_months = quarter_months.get(quarter, [7, 8, 9])
    
    filtered_entries = [
        e for e in PROCESSED_TDS_ENTRIES
        if datetime.strptime(e["date"], "%Y-%m-%d").month in target_months
    ]

    records = []
    for idx, e in enumerate(filtered_entries, 1):
        records.append({
            "record_no": idx,
            "deductee_name": e["vendor_name"],
            "pan": "PANNOTREQ1" if "aws" in e["vendor_name"].lower() else "ABCDE1234F",
            "section_code": e["section_code"],
            "invoice_date": e["date"],
            "amount_paid": e["gross_amount"],
            "tds_rate": e["tds_rate"],
            "tds_deducted": e["tds_amount"],
            "challan_code": e["challan_code"]
        })

    return {
        "form": "Form 26Q",
        "financial_year": financial_year,
        "quarter": f"Q{quarter}",
        "total_records": len(records),
        "total_tds_deducted": round(sum(r["tds_deducted"] for r in records), 2),
        "records": records
    }
