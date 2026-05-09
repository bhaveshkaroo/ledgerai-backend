"""
LedgerAI — routes/gst.py
Handles GST calculations and reporting.
"""

from fastapi import APIRouter
from pydantic import BaseModel
from routes.transactions import TRANSACTIONS

router = APIRouter()

class GSTCalcRequest(BaseModel):
    amount: float
    rate: int  # 5, 12, 18, 28
    type: str  # goods or services

@router.post("/calculate")
def calculate_gst(req: GSTCalcRequest):
    """
    Calculates CGST, SGST, IGST based on base amount and rate.
    """
    gst_amount = req.amount * (req.rate / 100)
    
    # Simple logic: Split into CGST and SGST (assuming intra-state for MVP)
    cgst = gst_amount / 2
    sgst = gst_amount / 2
    igst = 0.0  # Would be used for inter-state
    
    return {
        "base_amount": req.amount,
        "rate": req.rate,
        "cgst": round(cgst, 2),
        "sgst": round(sgst, 2),
        "igst": round(igst, 2),
        "total_gst": round(gst_amount, 2),
        "total_amount": round(req.amount + gst_amount, 2)
    }

@router.get("/summary")
def gst_summary():
    """
    Summarises GST paid and collected based on transaction history.
    """
    # Total GST paid is found in 'GST Payment' category transactions
    total_paid = sum(t["amount"] for t in TRANSACTIONS if t["category"] == "GST Payment")
    
    # Estimate GST collected (roughly 18% of revenue for calculation purposes)
    total_revenue = sum(t["amount"] for t in TRANSACTIONS if t["category"] == "Revenue")
    estimated_collected = total_revenue * 0.18
    
    net_liability = estimated_collected - total_paid

    return {
        "gst_paid": round(total_paid, 2),
        "gst_collected": round(estimated_collected, 2),
        "net_liability": round(net_liability, 2),
        "status": "Liability" if net_liability > 0 else "Refund"
    }
