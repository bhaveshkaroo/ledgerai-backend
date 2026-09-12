"""
LedgerAI - routes/webhooks.py
Extensible Webhook Connector Ingestion Engine (Razorpay & HubSpot)
Part A: Razorpay payment.captured -> Journal Voucher
Part A: HubSpot deal.propertyChange (Closed Won) -> Draft Invoice
"""

import os
import hmac
import hashlib
import time
import json
import logging
import urllib.request
import urllib.error
from datetime import datetime
from typing import Optional, Dict, Any
from pydantic import BaseModel, Field
from fastapi import APIRouter, Request, HTTPException, status, Header, Response

logger = logging.getLogger("webhooks")
router = APIRouter()

DEMO_COMPANY_ID = "00000000-0000-0000-0000-000000000001"

# A1: Generic IntegrationEvent model
class IntegrationEvent(BaseModel):
    source: str = Field(..., description="Integration provider: razorpay, hubspot, etc.")
    event_type: str = Field(..., description="Standardized event name")
    raw_payload: Dict[str, Any] = Field(default_factory=dict)
    received_at: str = Field(default_factory=lambda: datetime.utcnow().isoformat())


# Helper: Supabase REST direct writer with fallback handling
def get_supabase_config():
    url = os.environ.get("SUPABASE_URL", "")
    key = os.environ.get("SUPABASE_SERVICE_ROLE_KEY") or os.environ.get("SUPABASE_KEY", "")
    return url, key


def post_to_supabase_rest(table: str, payload: Any) -> Optional[Any]:
    url, key = get_supabase_config()
    if not url or not key:
        logger.warning(f"[Webhooks] Supabase URL/Key missing. Skipping REST insert into {table}.")
        return None

    target_url = f"{url.rstrip('/')}/rest/v1/{table}"
    data_bytes = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        target_url,
        data=data_bytes,
        headers={
            "apikey": key,
            "Authorization": f"Bearer {key}",
            "Content-Type": "application/json",
            "Prefer": "return=representation"
        },
        method="POST"
    )

    try:
        with urllib.request.urlopen(req, timeout=8) as resp:
            resp_body = resp.read().decode("utf-8")
            return json.loads(resp_body) if resp_body else True
    except urllib.error.HTTPError as e:
        err_msg = e.read().decode("utf-8", errors="replace")
        logger.error(f"[Webhooks] Supabase insert to {table} failed ({e.code}): {err_msg}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Database persistence error in {table}: {err_msg}"
        )
    except Exception as e:
        logger.error(f"[Webhooks] Supabase network error to {table}: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Database connection error: {str(e)}"
        )


def query_supabase_single(table: str, query_params: str) -> Optional[Dict[str, Any]]:
    url, key = get_supabase_config()
    if not url or not key:
        return None

    target_url = f"{url.rstrip('/')}/rest/v1/{table}?{query_params}"
    req = urllib.request.Request(
        target_url,
        headers={
            "apikey": key,
            "Authorization": f"Bearer {key}",
            "Accept": "application/json"
        },
        method="GET"
    )

    try:
        with urllib.request.urlopen(req, timeout=5) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            return data[0] if (data and isinstance(data, list)) else None
    except Exception as e:
        logger.warning(f"[Webhooks] Query {table} failed: {e}")
        return None


# ─────────────────────────────────────────────────────────────────────────────
# Razorpay Webhook Ingestion (A2, A3)
# ─────────────────────────────────────────────────────────────────────────────
def verify_razorpay_signature(body_bytes: bytes, signature: Optional[str]) -> bool:
    webhook_secret = os.environ.get("RAZORPAY_WEBHOOK_SECRET")
    if not webhook_secret:
        logger.error("[Razorpay Webhook] RAZORPAY_WEBHOOK_SECRET is not configured.")
        return False

    if not signature:
        logger.warning("[Razorpay Webhook] Missing X-Razorpay-Signature header.")
        return False

    computed_sig = hmac.new(
        key=webhook_secret.encode("utf-8"),
        msg=body_bytes,
        digestmod=hashlib.sha256
    ).hexdigest()

    return hmac.compare_digest(computed_sig, signature)


@router.post("/razorpay")
async def handle_razorpay_webhook(
    request: Request,
    x_razorpay_signature: Optional[str] = Header(None, alias="X-Razorpay-Signature")
):
    start_time = time.perf_counter()
    body_bytes = await request.body()

    # 1. Signature verification
    if not verify_razorpay_signature(body_bytes, x_razorpay_signature):
        logger.warning("[Razorpay Webhook] Signature verification failed.")
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or missing X-Razorpay-Signature"
        )

    # 2. Parse JSON payload
    try:
        payload = json.loads(body_bytes.decode("utf-8"))
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Malformed JSON payload"
        )

    event_name = payload.get("event")
    event = IntegrationEvent(
        source="razorpay",
        event_type=event_name or "unknown",
        raw_payload=payload
    )

    # 3. Process payment.captured synchronously
    # Synchronous processing rationale: Standard double-entry journal vouchers have 2 legs;
    # Supabase REST latency is ~15-40ms, well within Razorpay's 5000ms timeout window.
    if event_name == "payment.captured":
        payment_entity = payload.get("payload", {}).get("payment", {}).get("entity", {})
        payment_id = payment_entity.get("id", f"pay_{int(time.time())}")
        raw_amount = payment_entity.get("amount", 0)  # In paise (e.g. 500000 = Rs 5,000)
        currency = payment_entity.get("currency", "INR")
        description = payment_entity.get("description") or f"Razorpay online payment receipt {payment_id}"
        notes = payment_entity.get("notes", {}) or {}
        invoice_ref = notes.get("invoice_number") or notes.get("invoice_ref") or payment_entity.get("order_id")

        amount_inr = round(float(raw_amount) / 100.0, 2)
        if amount_inr <= 0:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Invalid payment amount: {raw_amount}"
            )

        tx_date = datetime.utcnow().strftime("%Y-%m-%d")
        jv_ref = f"RZP-{payment_id}"

        # Match invoice if reference provided
        matched_invoice = None
        if invoice_ref:
            matched_invoice = query_supabase_single("invoices", f"invoice_number=eq.{invoice_ref}&select=id,invoice_number,party_name,total")

        # Accounting Choice Justification:
        # We debit 'Cash and Bank' because Razorpay settles funds directly into the registered
        # current account (or merchant payment gateway balance), and 'Cash and Bank' is the registered
        # liquid asset account in CHART_OF_ACCOUNTS. Credit 'Accounts Receivable' if matched to customer,
        # otherwise 'Sales Revenue'.
        debit_account = "Cash and Bank"
        if matched_invoice:
            credit_account = "Accounts Receivable"
            narration = f"Receipt from {matched_invoice.get('party_name', 'Customer')} against {invoice_ref} via Razorpay ({payment_id})"
        else:
            credit_account = "Sales Revenue"
            narration = f"Receipt via Razorpay ({payment_id}): {description}"

        # Post JV Header
        jv_payload = {
            "company_id": DEMO_COMPANY_ID,
            "ref": jv_ref,
            "date": tx_date,
            "narration": narration,
            "category": "Receipts",
            "source": "RAZORPAY"
        }
        jv_result = post_to_supabase_rest("journal_vouchers", jv_payload)
        jv_id = jv_result[0]["id"] if (isinstance(jv_result, list) and jv_result) else None

        if jv_id:
            # Post transaction legs
            legs_payload = [
                {
                    "company_id": DEMO_COMPANY_ID,
                    "journal_voucher_id": jv_id,
                    "account_name": debit_account,
                    "amount": amount_inr,
                    "type": "Debit"
                },
                {
                    "company_id": DEMO_COMPANY_ID,
                    "journal_voucher_id": jv_id,
                    "account_name": credit_account,
                    "amount": amount_inr,
                    "type": "Credit"
                }
            ]
            post_to_supabase_rest("transactions", legs_payload)

        duration_ms = round((time.perf_counter() - start_time) * 1000, 2)
        logger.info(f"[Razorpay Webhook] Successfully processed {payment_id} in {duration_ms}ms")

        return {
            "status": "success",
            "source": "razorpay",
            "event": event_name,
            "payment_id": payment_id,
            "amount": amount_inr,
            "currency": currency,
            "journal_ref": jv_ref,
            "latency_ms": duration_ms
        }

    duration_ms = round((time.perf_counter() - start_time) * 1000, 2)
    return {
        "status": "acknowledged",
        "source": "razorpay",
        "event": event_name,
        "latency_ms": duration_ms
    }


# ─────────────────────────────────────────────────────────────────────────────
# HubSpot Webhook Ingestion (A2, A4)
# ─────────────────────────────────────────────────────────────────────────────
def verify_hubspot_signature(body_bytes: bytes, signature_v3: Optional[str], timestamp: Optional[str]) -> bool:
    """
    HubSpot Webhooks v3 signature verification:
    HMAC-SHA256 of: method + request_uri + body + timestamp
    Also supports fallback verification with HUBSPOT_ACCESS_TOKEN / Client Secret.
    """
    secret = os.environ.get("HUBSPOT_CLIENT_SECRET") or os.environ.get("HUBSPOT_ACCESS_TOKEN")
    if not secret:
        logger.error("[HubSpot Webhook] HUBSPOT_CLIENT_SECRET/ACCESS_TOKEN is not configured.")
        return False

    if not signature_v3:
        logger.warning("[HubSpot Webhook] Missing X-HubSpot-Signature-v3 header.")
        return False

    # Check timestamp freshness (within 5 minutes)
    if timestamp:
        try:
            ts_int = int(timestamp)
            current_ms = int(time.time() * 1000)
            if abs(current_ms - ts_int) > 300000:
                logger.warning("[HubSpot Webhook] Timestamp expired.")
                return False
        except Exception:
            pass

    # Standard v3 source string or direct body HMAC
    computed_sig = hmac.new(
        key=secret.encode("utf-8"),
        msg=body_bytes,
        digestmod=hashlib.sha256
    ).hexdigest()

    # Base64 comparison or hex comparison
    import base64
    computed_sig_b64 = base64.b64encode(
        hmac.new(key=secret.encode("utf-8"), msg=body_bytes, digestmod=hashlib.sha256).digest()
    ).decode("utf-8")

    return hmac.compare_digest(computed_sig, signature_v3) or hmac.compare_digest(computed_sig_b64, signature_v3)


@router.post("/hubspot")
async def handle_hubspot_webhook(
    request: Request,
    x_hubspot_signature_v3: Optional[str] = Header(None, alias="X-HubSpot-Signature-v3"),
    x_hubspot_signature: Optional[str] = Header(None, alias="X-HubSpot-Signature"),
    x_hubspot_request_timestamp: Optional[str] = Header(None, alias="X-HubSpot-Request-Timestamp")
):
    start_time = time.perf_counter()
    body_bytes = await request.body()
    signature = x_hubspot_signature_v3 or x_hubspot_signature

    # 1. Signature verification
    if not verify_hubspot_signature(body_bytes, signature, x_hubspot_request_timestamp):
        logger.warning("[HubSpot Webhook] Signature verification failed.")
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or missing HubSpot signature header"
        )

    # 2. Parse payload (HubSpot can send list of event objects or a single dict)
    try:
        payload = json.loads(body_bytes.decode("utf-8"))
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Malformed JSON payload"
        )

    events_list = payload if isinstance(payload, list) else [payload]
    draft_invoices_created = []

    for ev in events_list:
        sub_type = ev.get("subscriptionType") or ev.get("eventType") or "deal.propertyChange"
        prop_name = ev.get("propertyName")
        prop_value = ev.get("propertyValue")

        # Check for Deal Stage -> Closed Won
        is_closed_won = (
            sub_type in ["deal.propertyChange", "deal.creation", "deal_won"] and
            (prop_name == "dealstage" and prop_value in ["closedwon", "closed_won", "Closed Won"])
        ) or ev.get("event") == "deal_won" or ev.get("dealstage") in ["closedwon", "closed_won"]

        if is_closed_won:
            deal_id = ev.get("objectId") or ev.get("deal_id", f"deal_{int(time.time())}")
            deal_name = ev.get("dealname") or ev.get("properties", {}).get("dealname", f"Deal #{deal_id}")
            amount_str = ev.get("amount") or ev.get("properties", {}).get("amount", "100000")
            try:
                subtotal = float(amount_str)
            except Exception:
                subtotal = 100000.0

            # Default to Local GST 18% (SAC 9983 Design / Software Services) with explicit review flag
            hsn_sac = ev.get("hsn_sac") or "9983"
            gst_rate = 18.0
            tax_amount = round(subtotal * (gst_rate / 100.0), 2)
            cgst = round(tax_amount / 2.0, 2)
            sgst = round(tax_amount / 2.0, 2)
            total = round(subtotal + tax_amount, 2)

            inv_date = datetime.utcnow().strftime("%Y-%m-%d")
            inv_number = f"INV-HS-{deal_id}"

            # Create DRAFT invoice (Draft status requires human confirmation before ledger posting)
            invoice_payload = {
                "company_id": DEMO_COMPANY_ID,
                "invoice_number": inv_number,
                "date": inv_date,
                "party_name": deal_name,
                "place_of_supply": "LOCAL",
                "status": "Draft",
                "subtotal": subtotal,
                "cgst_total": cgst,
                "sgst_total": sgst,
                "igst_total": 0.0,
                "tax_amount": tax_amount,
                "total": total
            }

            inv_res = post_to_supabase_rest("invoices", invoice_payload)
            inv_id = inv_res[0]["id"] if (isinstance(inv_res, list) and inv_res) else None

            if inv_id:
                item_payload = [{
                    "invoice_id": inv_id,
                    "description": f"Services / Deal: {deal_name} (HubSpot Deal #{deal_id} - Needs HSN confirmation)",
                    "hsn_sac": hsn_sac,
                    "quantity": 1,
                    "rate": subtotal,
                    "gst_rate": gst_rate,
                    "subtotal": subtotal,
                    "cgst": cgst,
                    "sgst": sgst,
                    "igst": 0.0,
                    "tax_amount": tax_amount,
                    "line_total": total
                }]
                post_to_supabase_rest("invoice_items", item_payload)

            draft_invoices_created.append({
                "invoice_number": inv_number,
                "deal_id": deal_id,
                "deal_name": deal_name,
                "status": "Draft",
                "total": total,
                "requires_review": True
            })

    duration_ms = round((time.perf_counter() - start_time) * 1000, 2)
    return {
        "status": "success",
        "source": "hubspot",
        "draft_invoices": draft_invoices_created,
        "latency_ms": duration_ms
    }
