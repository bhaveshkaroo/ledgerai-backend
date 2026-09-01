import sys
sys.stdout.reconfigure(encoding='utf-8')
import json
import os
import asyncio
from dotenv import load_dotenv
load_dotenv()

from routes.insights import analyze_level2_trend_forecast, analyze_level3_strategic_scenario, Level2Query, Level3Query

async def run_live_tests():
    # ── TEST CASE A: Unified 36-Month Dataset (2024-2026) ────────────────────────
    
    # 1. Level 2 Query
    l2_query = Level2Query(
        question="Provide a CFA-grounded trend and forecast analysis for our 36-month operational run-rate and explain the OLS linear regression projections.",
        computed_data={
            "financials": {
                "revenue": 20124000,
                "cogs": 13857500,
                "grossProfit": 6266500,
                "netProfit": -3388500,
                "totalAssets": 37319074,
                "totalEquity": 1611500,
                "cash": 5713750
            },
            "dupont": {
                "netProfitMarginPct": -16.84,
                "assetTurnover": 0.54,
                "equityMultiplier": 23.16,
                "roeResult": -210.27
            },
            "regression": {
                "slope": 1593.82,
                "intercept": 531108.11,
                "rSquared": 0.03,
                "method": "Ordinary Least Squares (OLS) Linear Regression (Trailing 36 Periods)"
            },
            "projections": [
                {"periodIndex": 36, "month": "Jan 2027 (P+1)", "projectedValue": 588486, "lowerBand": 541407, "upperBand": 635565},
                {"periodIndex": 37, "month": "Feb 2027 (P+2)", "projectedValue": 590080, "lowerBand": 542873, "upperBand": 637286},
                {"periodIndex": 38, "month": "Mar 2027 (P+3)", "projectedValue": 591673, "lowerBand": 544339, "upperBand": 639007}
            ]
        }
    )

    print("=== CALLING /api/insights/level2 ===")
    l2_res = await analyze_level2_trend_forecast(l2_query)
    print("=== RAW RESPONSE: /api/insights/level2 ===")
    print(json.dumps(l2_res.model_dump(), indent=2))

    # 2. Level 3 Query
    l3_query = Level3Query(
        question="Evaluate our liquidity stress and concentration risks if expense inflation rises by 12% and customer collections slip by 45 days.",
        scenario_params={
            "revenueDeltaPct": 0,
            "expenseDeltaPct": 12,
            "dsoSlipDays": 45,
            "baselineRevenue": 20124000,
            "baselineExpenses": 22507500,
            "baselineCash": 5713750,
            "baselineRunwayMonths": 3.0,
            "recalculatedRevenue": 20124000,
            "recalculatedExpenses": 25208400,
            "delayedCashCollection": 2481041,
            "recalculatedCash": 531809,
            "recalculatedRunwayMonths": 0.3
        },
        computed_risk_data={
            "concentration": {
                "top4Customers": [
                    {"name": "Rajan Fabrics", "pct": 27.9},
                    {"name": "Bombay Fashion House", "pct": 27.5},
                    {"name": "Lucky Hosiery", "pct": 22.3},
                    {"name": "Mehta Garments", "pct": 22.2}
                ],
                "top4CustomerRevenueSharePct": 99.9,
                "top5VendorPayableSharePct": 80.8
            },
            "volatility": {
                "cvPct": 8.99,
                "stdDev": 196372
            },
            "activeRedFlags": [
                {
                    "id": "RED_FLAG_DSO",
                    "severity": "High",
                    "title": "Receivable Collection Lag",
                    "metric": "45-day collection slip traps Rs. 24,81,041 in Working Capital."
                },
                {
                    "id": "RED_FLAG_RUNWAY",
                    "severity": "Critical",
                    "title": "Severe Cash Runway Contraction",
                    "metric": "Liquid cash drops from Rs. 57,13,750 to Rs. 5,31,809 (0.3 months runway)."
                }
            ]
        }
    )

    print("\n=== CALLING /api/insights/level3 ===")
    l3_res = await analyze_level3_strategic_scenario(l3_query)
    print("=== RAW RESPONSE: /api/insights/level3 ===")
    print(json.dumps(l3_res.model_dump(), indent=2))

if __name__ == "__main__":
    asyncio.run(run_live_tests())
