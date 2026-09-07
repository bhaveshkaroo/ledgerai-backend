"""
LedgerAI - routes/settings.py
Global system settings including Currency (INR / USD) translation and preferences.
"""

from fastapi import APIRouter
from pydantic import BaseModel
from typing import Optional

router = APIRouter()

CURRENT_SETTINGS = {
    "currency": "INR",
    "usd_exchange_rate": 86.50,
    "theme": "light",
    "first_day": "Monday"
}

class CurrencyUpdateRequest(BaseModel):
    currency: str

class SettingsUpdateRequest(BaseModel):
    currency: Optional[str] = None
    theme: Optional[str] = None
    first_day: Optional[str] = None

@router.get("/")
def get_settings():
    return CURRENT_SETTINGS

@router.post("/")
def update_settings(req: SettingsUpdateRequest):
    if req.currency:
        code = req.currency.upper()
        CURRENT_SETTINGS["currency"] = "USD" if code == "USD" else "INR"
    if req.theme:
        CURRENT_SETTINGS["theme"] = req.theme
    if req.first_day:
        CURRENT_SETTINGS["first_day"] = req.first_day
    return CURRENT_SETTINGS

@router.get("/currency")
def get_currency():
    curr = CURRENT_SETTINGS["currency"]
    return {
        "currency": curr,
        "symbol": "$" if curr == "USD" else "₹",
        "rate": CURRENT_SETTINGS["usd_exchange_rate"]
    }

@router.post("/currency")
def set_currency(req: CurrencyUpdateRequest):
    code = req.currency.upper()
    CURRENT_SETTINGS["currency"] = "USD" if code == "USD" else "INR"
    curr = CURRENT_SETTINGS["currency"]
    return {
        "currency": curr,
        "symbol": "$" if curr == "USD" else "₹",
        "rate": CURRENT_SETTINGS["usd_exchange_rate"],
        "message": f"Global currency updated to {curr}"
    }
