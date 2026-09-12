"""
Backend Webhooks Test Suite (Part A Verification)
Tests:
1. Razorpay signature verification & payment.captured ledger posting with real measured latency.
2. HubSpot signature verification & deal won -> draft invoice creation.
3. Falsification: Missing/invalid signatures and malformed payloads rejected with 401/400.
"""

import os
import sys
import hmac
import hashlib
import json
import time
from fastapi.testclient import TestClient
from dotenv import load_dotenv

load_dotenv()

# Ensure dummy secrets exist for local testing if not in env
if not os.environ.get("RAZORPAY_WEBHOOK_SECRET"):
    os.environ["RAZORPAY_WEBHOOK_SECRET"] = "test_rzp_webhook_secret_998877"
if not os.environ.get("HUBSPOT_ACCESS_TOKEN"):
    os.environ["HUBSPOT_ACCESS_TOKEN"] = "test_hs_access_token_112233"

from main import app

client = TestClient(app)

passed = 0
failed = 0
results = []

def run_test(test_id, description, fn):
    global passed, failed
    try:
        fn()
        passed += 1
        results.append({"id": test_id, "desc": description, "verdict": "PASS"})
        print(f"  [PASS] [{test_id}] {description}")
    except Exception as e:
        failed += 1
        results.append({"id": test_id, "desc": description, "verdict": "FAIL", "error": str(e)})
        print(f"  [FAIL] [{test_id}] {description} -> {e}")

print("\n" + "=" * 76)
print("  MESO LEDGER AI -- BACKEND WEBHOOK INGESTION VERIFICATION (PART A)")
print("=" * 76 + "\n")

# ─────────────────────────────────────────────────────────────────────────────
# Test 1: Razorpay Signature Falsification (Invalid & Missing Signature)
# ─────────────────────────────────────────────────────────────────────────────
def test_rzp_missing_sig():
    resp = client.post("/api/webhooks/razorpay", json={"event": "payment.captured"})
    assert resp.status_code == 401, f"Expected 401, got {resp.status_code}"
    assert "Invalid or missing" in resp.json()["detail"]

run_test("RZP-01", "Razorpay webhook rejects missing X-Razorpay-Signature with 401", test_rzp_missing_sig)

def test_rzp_invalid_sig():
    body = json.dumps({"event": "payment.captured"}).encode("utf-8")
    resp = client.post(
        "/api/webhooks/razorpay",
        content=body,
        headers={"X-Razorpay-Signature": "bad_sig_12345", "Content-Type": "application/json"}
    )
    assert resp.status_code == 401, f"Expected 401, got {resp.status_code}"
    assert "Invalid or missing" in resp.json()["detail"]

run_test("RZP-02", "Razorpay webhook rejects invalid HMAC signature with 401", test_rzp_invalid_sig)

def test_rzp_malformed_json():
    secret = os.environ["RAZORPAY_WEBHOOK_SECRET"]
    bad_body = b"NOT_JSON_DATA{{{{"
    sig = hmac.new(secret.encode("utf-8"), bad_body, hashlib.sha256).hexdigest()
    resp = client.post(
        "/api/webhooks/razorpay",
        content=bad_body,
        headers={"X-Razorpay-Signature": sig, "Content-Type": "application/json"}
    )
    assert resp.status_code == 400, f"Expected 400, got {resp.status_code}"

run_test("RZP-03", "Razorpay webhook rejects malformed body with 400", test_rzp_malformed_json)

# ─────────────────────────────────────────────────────────────────────────────
# Test 2: Razorpay payment.captured -> Real Measured Latency & JV
# ─────────────────────────────────────────────────────────────────────────────
def test_rzp_payment_captured_success():
    secret = os.environ["RAZORPAY_WEBHOOK_SECRET"]
    payload = {
        "event": "payment.captured",
        "payload": {
            "payment": {
                "entity": {
                    "id": f"pay_test_{int(time.time())}",
                    "amount": 750000,  # Rs 7,500.00
                    "currency": "INR",
                    "status": "captured",
                    "description": "Consulting & Retainer Fees Q3",
                    "notes": {
                        "client": "Tata Consultancy Systems"
                    }
                }
            }
        }
    }
    body = json.dumps(payload).encode("utf-8")
    sig = hmac.new(secret.encode("utf-8"), body, hashlib.sha256).hexdigest()

    t0 = time.perf_counter()
    resp = client.post(
        "/api/webhooks/razorpay",
        content=body,
        headers={"X-Razorpay-Signature": sig, "Content-Type": "application/json"}
    )
    client_latency_ms = round((time.perf_counter() - t0) * 1000, 2)

    assert resp.status_code == 200, f"Expected 200, got {resp.status_code}: {resp.text}"
    data = resp.json()
    assert data["status"] == "success"
    assert data["amount"] == 7500.0
    assert data["currency"] == "INR"
    assert data["journal_ref"].startswith("RZP-pay_test_")
    print(f"    Server Latency: {data['latency_ms']}ms | Measured Round-Trip: {client_latency_ms}ms")
    print(f"    Journal Ref Created: {data['journal_ref']} (Amount: Rs {data['amount']})")

run_test("RZP-04", "Razorpay payment.captured posts double-entry JV with measured latency", test_rzp_payment_captured_success)

# ─────────────────────────────────────────────────────────────────────────────
# Test 3: HubSpot Signature Falsification & Deal Won -> Draft Invoice
# ─────────────────────────────────────────────────────────────────────────────
def test_hs_missing_sig():
    resp = client.post("/api/webhooks/hubspot", json=[{"eventType": "deal.propertyChange"}])
    assert resp.status_code == 401, f"Expected 401, got {resp.status_code}"

run_test("HS-01", "HubSpot webhook rejects missing signature header with 401", test_hs_missing_sig)

def test_hs_invalid_sig():
    body = json.dumps([{"eventType": "deal.propertyChange"}]).encode("utf-8")
    resp = client.post(
        "/api/webhooks/hubspot",
        content=body,
        headers={"X-HubSpot-Signature-v3": "invalid_sig_abc", "Content-Type": "application/json"}
    )
    assert resp.status_code == 401, f"Expected 401, got {resp.status_code}"

run_test("HS-02", "HubSpot webhook rejects invalid signature with 401", test_hs_invalid_sig)

def test_hs_deal_won_draft_invoice():
    secret = os.environ.get("HUBSPOT_CLIENT_SECRET") or os.environ["HUBSPOT_ACCESS_TOKEN"]
    deal_id = f"deal_{int(time.time())}"
    payload = [
        {
            "objectId": deal_id,
            "subscriptionType": "deal.propertyChange",
            "propertyName": "dealstage",
            "propertyValue": "closedwon",
            "dealname": "Enterprise AI Customization Contract",
            "amount": "250000",
            "hsn_sac": "9983"
        }
    ]
    body = json.dumps(payload).encode("utf-8")
    sig = hmac.new(secret.encode("utf-8"), body, hashlib.sha256).hexdigest()

    t0 = time.perf_counter()
    resp = client.post(
        "/api/webhooks/hubspot",
        content=body,
        headers={"X-HubSpot-Signature-v3": sig, "Content-Type": "application/json"}
    )
    client_latency_ms = round((time.perf_counter() - t0) * 1000, 2)

    assert resp.status_code == 200, f"Expected 200, got {resp.status_code}: {resp.text}"
    data = resp.json()
    assert data["status"] == "success"
    invoices = data.get("draft_invoices", [])
    assert len(invoices) == 1
    inv = invoices[0]
    assert inv["status"] == "Draft"
    assert inv["requires_review"] is True
    assert inv["total"] == 295000.0  # Rs 2,50,000 + 18% GST (45,000)
    print(f"    Server Latency: {data['latency_ms']}ms | Measured Round-Trip: {client_latency_ms}ms")
    print(f"    Draft Invoice Created: {inv['invoice_number']} (Total: Rs {inv['total']}, Status: {inv['status']})")

run_test("HS-03", "HubSpot Deal Won creates Draft invoice requiring human confirmation", test_hs_deal_won_draft_invoice)

print("\n" + "=" * 76)
print(f"  RESULTS: {passed} PASSED, {failed} FAILED out of {passed + failed} tests")
print("=" * 76 + "\n")

if failed > 0:
    sys.exit(1)
