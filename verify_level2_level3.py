import sys
sys.stdout.reconfigure(encoding='utf-8')
import os
import json
from dotenv import load_dotenv
load_dotenv()

from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_engine_computation():
    print("=" * 60)
    print("CHECK 1: Deterministic Engine Computation (/compute-engine)")
    print("=" * 60)
    res = client.get("/api/insights/compute-engine")
    assert res.status_code == 200, f"Error: {res.text}"
    data = res.json()
    
    print(f"[✓] Periods Analyzed: {data['regression']['periodsAnalyzed']} months")
    print(f"[✓] Methodology: {data['regression']['methodology']}")
    print(f"[✓] Historical Series Length: {len(data['historicalSeries'])}")
    print(f"[✓] 3M-SMA Sample (Month 3): {data['historicalSeries'][2]['revenue_3M_SMA']}")
    print(f"[✓] Projections Generated: {len(data['projections'])}")
    for p in data['projections']:
        print(f"    -> {p['month']}: Revenue Rs. {p['projectedRevenue']:,.2f} | Cash Rs. {p['projectedCash']:,.2f} ({p['method']})")
    
    print(f"[✓] Top 5 Customer Revenue Share: {data['concentration']['top5CustomerRevenueSharePct']}%")
    print(f"[✓] Top 5 Vendor Payable Share: {data['concentration']['top5VendorPayableSharePct']}%")
    print(f"[✓] Revenue Volatility (CV): {data['riskMetrics']['revenueVolatilityCV']}%")
    print(f"[✓] Cash Runway: {data['riskMetrics']['cashRunwayMonths']} months")
    return data

def test_level2_gemini(engine_data):
    print("\n" + "=" * 60)
    print("CHECK 2: Level 2 Trend & Forecast AI Interpretation (/level2)")
    print("=" * 60)
    payload = {
        "question": "What is the structural trend in revenue and cash runway over the 3-year historical window, and what are the key inflection points in our OLS projections?",
        "computed_data": {
            "regression": engine_data["regression"],
            "recentSeries": engine_data["historicalSeries"][-6:],
            "projections": engine_data["projections"],
            "riskMetrics": engine_data["riskMetrics"]
        }
    }
    res = client.post("/api/insights/level2", json=payload)
    if res.status_code != 200:
        print(f"[!] Level 2 Error: {res.status_code} - {res.text}")
        return
    
    ans = res.json()
    print(f"[✓] Framework: {ans.get('framework')}")
    print(f"[✓] Methodology: {ans.get('methodology')}")
    print("\n--- LEVEL 2 GENUINE GEMINI MODEL OUTPUT ---")
    print(ans.get("answer"))
    print("-------------------------------------------\n")

def test_level3_gemini(engine_data):
    print("\n" + "=" * 60)
    print("CHECK 3: Level 3 Strategic & Scenario Risk AI Interpretation (/level3)")
    print("=" * 60)
    payload = {
        "question": "Assess our concentration vulnerabilities and stress-test our liquidity if our top customer delays payments by 45 days while SG&A expenses inflate by 12%.",
        "scenario_params": {
            "revenueGrowthShockPct": -5.0,
            "expenseInflationPct": 12.0,
            "dsoCollectionDelayDays": 45,
            "stressTestedCashRunwayMonths": 4.2,
            "recalculatedCashImpact": -350000.0
        },
        "computed_risk_data": {
            "concentration": engine_data["concentration"],
            "riskMetrics": engine_data["riskMetrics"],
            "activeRedFlags": [
                {
                    "id": "CONC_RISK",
                    "title": "Customer Concentration Vulnerability",
                    "severity": "High",
                    "metric": f"Top 5 customers represent {engine_data['concentration']['top5CustomerRevenueSharePct']}% of total revenue."
                },
                {
                    "id": "VOL_RISK",
                    "title": "Revenue Volatility",
                    "severity": "Medium",
                    "metric": f"Historical revenue coefficient of variation is {engine_data['riskMetrics']['revenueVolatilityCV']}%."
                }
            ]
        }
    }
    res = client.post("/api/insights/level3", json=payload)
    if res.status_code != 200:
        print(f"[!] Level 3 Error: {res.status_code} - {res.text}")
        return
    
    ans = res.json()
    print(f"[✓] Framework: {ans.get('framework')}")
    print("\n--- LEVEL 3 GENUINE GEMINI MODEL OUTPUT (FRM RISK FRAMING) ---")
    print(ans.get("answer"))
    print("-------------------------------------------------------------\n")

if __name__ == "__main__":
    data = test_engine_computation()
    test_level2_gemini(data)
    test_level3_gemini(data)
