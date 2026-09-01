import os
import json
import logging
import asyncio
from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel
from typing import Dict, Any, Optional, List
from routes.transactions import TRANSACTIONS

logger = logging.getLogger(__name__)

router = APIRouter()

class InsightsQuery(BaseModel):
    question: str
    financial_context: Optional[Dict[str, Any]] = None

class InsightsResponse(BaseModel):
    answer: str
    framework: str = 'CFA Level 1 Analysis'

class Level2Query(BaseModel):
    question: str
    computed_data: Optional[Dict[str, Any]] = None

class Level2Response(BaseModel):
    answer: str
    framework: str = 'CFA Level 2 Deep Trend & Forecast Engine'
    methodology: str = 'Ordinary Least Squares (OLS) Linear Regression & 3M-SMA'

class Level3Query(BaseModel):
    question: str
    scenario_params: Optional[Dict[str, Any]] = None
    computed_risk_data: Optional[Dict[str, Any]] = None

class Level3Response(BaseModel):
    answer: str
    framework: str = 'CFA Level 3 Strategic & FRM Risk Analysis'

# ── SYSTEM PROMPTS ─────────────────────────────────────────────────────────────

SYSTEM_INSTRUCTION_L1 = """You are a senior financial analyst and CFO for an Indian MSME.
Your role is to analyze the user's financial context and provide strategic, actionable insights answering their question.
Format your answer clearly using bullet points and appropriate financial terminology.
Always use the financial data provided in the context to support your analysis.
Always format currency figures in Indian Rupees with the standard ₹ symbol and INR numbering (e.g. ₹2,01,24,000 or ₹2.01 Cr). Never use dollar signs ($) or USD references.
Always append this exact disclaimer at the very end of your response: "⚠️ This is an AI-generated analysis based on current ledger data. Please consult a qualified financial advisor before making strategic decisions."
"""

SYSTEM_INSTRUCTION_L2 = """You are the Meso Level 2 Deep Trend & Forecasting Specialist — an expert CFA Level II Quantitative Methods & Financial Statement Modeling Advisor.

Your capabilities & rules:
1. **Explain Computed Trends**: Interpret pre-computed time-series metrics (Month-over-Month / Quarter-over-Quarter growth rates, 3-Month Simple Moving Averages, and Ordinary Least Squares Linear Regression projections).
2. **Zero Fabrication**: Ground every single number in the pre-computed data provided in the context. Never invent figures or guess shapes.
3. **Explicit Methodology**: Explicitly state the computation method used for projections (e.g., "Based on Ordinary Least Squares (OLS) Linear Regression over trailing historical series...").
4. **Non-Guaranteed Estimates**: Projections must always be labeled as statistical estimates based on historical run-rates, not guarantees.
5. **Data Limitation Guardrail**: If historical data is insufficient for a window, explicitly highlight the data boundary rather than extrapolating blindly.
6. **Strictly Advisory-Only**: Never offer, trigger, or suggest modifying or posting to the ledger.
7. **Strict INR Currency Formatting**: Always use Indian Rupees (₹) and Indian numbering format (e.g. ₹2,01,24,000, ₹33.88 Lakh, ₹2.01 Cr). NEVER use dollar signs ($) or USD terms.

Format with clean markdown headers and bullet points.
Always append this exact disclaimer at the very end of your response: "⚠️ This is an AI-generated analysis based on current ledger data. Please consult a qualified financial advisor before making strategic decisions."
"""

SYSTEM_INSTRUCTION_L3 = """You are the Meso Level 3 Strategic & Risk Advisory Lead — an expert Senior Corporate Strategist, CFA Charterholder, and Certified Financial Risk Manager (FRM).

Your capabilities & rules:
1. **Strategic & Scenario Interpretation**: Analyze pre-computed What-If scenarios (e.g. revenue shocks, expense inflation, receivable collection delays) using the recalculated figures provided in the context.
2. **FRM Risk Framing**:
   - **Concentration Risk**: Evaluate top-customer revenue dependency and top-vendor payable exposure.
   - **Liquidity Stress-Testing**: Frame potential vulnerabilities if receivables slip or credit tightens, citing exact stress-tested cash figures.
   - **Volatility & Stability**: Evaluate historical revenue/cash flow dispersion using the pre-computed Coefficient of Variation (CV) and Standard Deviation.
   - **Runway & Coverage**: Explain months of operational burn coverage provided by current liquid reserves.
3. **Automated Red-Flag Diagnostics**: Review active red flags (e.g., DSO expansion, margin compression, leverage spikes) and explain the root cause chain.
4. **Contextual Benchmarks**: Provide clearly-labeled generic SME benchmarks for perspective.
5. **Strictly Advisory-Only**: Never offer, trigger, or suggest modifying or posting to the ledger.
6. **Strict INR Currency Formatting**: Always use Indian Rupees (₹) and Indian numbering format (e.g. ₹2,01,24,000, ₹33.88 Lakh, ₹2.01 Cr). NEVER use dollar signs ($) or USD terms.

Format with structured executive sections.
Always append this exact disclaimer at the very end of your response: "⚠️ This is an AI-generated analysis based on current ledger data. Please consult a qualified financial advisor before making strategic decisions."
"""


PRIMARY_MODEL = "gemini-3.6-flash"
FALLBACK_MODEL = "gemini-3.5-flash"

async def call_gemini_generic(prompt: str, system_instruction: str, api_key: str) -> str:
    """
    Calls Gemini API using curl.exe with temp payload file and automatic fallback across models.
    """
    import tempfile
    import uuid

    payload = {
        "contents": [{"parts": [{"text": prompt}]}],
        "systemInstruction": {"parts": [{"text": system_instruction}]},
        "generationConfig": {"responseMimeType": "text/plain", "temperature": 0.3}
    }
    
    # Use unique temp file to avoid race conditions and handle any payload size/escaping
    temp_dir = os.path.dirname(__file__)
    temp_path = os.path.join(temp_dir, f"_req_{uuid.uuid4().hex}.json")
    with open(temp_path, "w", encoding="utf-8") as f:
        json.dump(payload, f)

    try:
        for model in [PRIMARY_MODEL, FALLBACK_MODEL]:
            url = f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent?key={api_key}"

            proc = await asyncio.create_subprocess_exec(
                "curl.exe", "-s", "-X", "POST", url,
                "-H", "Content-Type: application/json",
                "-d", f"@{temp_path}",
                stdout=asyncio.subprocess.PIPE,
                stderr=asyncio.subprocess.PIPE
            )

            try:
                stdout, stderr = await asyncio.wait_for(proc.communicate(), timeout=25.0)
            except asyncio.TimeoutError:
                proc.kill()
                continue

            if not stdout:
                continue

            try:
                res_data = json.loads(stdout.decode("utf-8"))
            except Exception:
                continue

            if "error" in res_data:
                err = res_data["error"]
                code = err.get("code", 500)
                # On 429 or 503, continue loop to fallback model
                continue

            candidates = res_data.get("candidates", [])
            if candidates and "content" in candidates[0]:
                parts = candidates[0]["content"].get("parts", [])
                if parts and "text" in parts[0]:
                    return parts[0]["text"]
    finally:
        if os.path.exists(temp_path):
            try:
                os.remove(temp_path)
            except Exception:
                pass

    raise HTTPException(
        status_code=status.HTTP_502_BAD_GATEWAY,
        detail="AI Insights service unavailable — please try again."
    )


# ── ROUTES ──────────────────────────────────────────────────────────────────

@router.get('/health')
def health_check():
    return {'status': 'healthy', 'module': 'insights', 'levels': ['level1', 'level2', 'level3']}

@router.post('/analyze', response_model=InsightsResponse)
async def analyze_financials(query: InsightsQuery):
    """Level 1: Financial Health (Preserved Baseline)"""
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail="AI Insights unavailable — GEMINI_API_KEY is not configured."
        )

    context_str = ""
    if query.financial_context:
        context_str = "\n\nFinancial Context:\n" + json.dumps(query.financial_context, indent=2)
        
    prompt = f"User Question: {query.question}{context_str}"
    
    try:
        answer = await call_gemini_generic(prompt, SYSTEM_INSTRUCTION_L1, api_key)
        return InsightsResponse(
            answer=answer,
            framework='CFA Level 1 Analysis'
        )
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error in analyze_financials: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="AI Insights failed to generate analysis."
        )

@router.post('/level2', response_model=Level2Response)
async def analyze_level2_trend_forecast(query: Level2Query):
    """
    Level 2: Deep Trend & Forecast Engine (CFA Quantitative Methods).
    Grounded in pre-computed series, moving averages, growth rates, and regression projections.
    """
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail="AI Insights unavailable — GEMINI_API_KEY is not configured."
        )

    context_str = ""
    if query.computed_data:
        context_str = "\n\n--- PRE-COMPUTED DETERMINISTIC TREND & FORECAST DATA ---\n" + json.dumps(query.computed_data, indent=2) + "\n--- END COMPUTED DATA ---\n"

    prompt = f"User Question: \"{query.question}\"{context_str}\n\nPlease provide an in-depth, CFA-grounded quantitative trend and forecast analysis based on the computed metrics."

    try:
        answer = await call_gemini_generic(prompt, SYSTEM_INSTRUCTION_L2, api_key)
        return Level2Response(
            answer=answer,
            framework='CFA Level 2 Deep Trend & Forecast Engine',
            methodology='Ordinary Least Squares (OLS) Linear Regression & 3M-SMA'
        )
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error in analyze_level2_trend_forecast: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="AI Level 2 Insights failed to generate analysis."
        )

@router.post('/level3', response_model=Level3Response)
async def analyze_level3_strategic_scenario(query: Level3Query):
    """
    Level 3: Strategic & Scenario Analysis (CFA + FRM Risk Framing).
    Grounded in pre-computed What-If scenarios, red flags, concentration metrics, and volatility data.
    """
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail="AI Insights unavailable — GEMINI_API_KEY is not configured."
        )

    context_parts = []
    if query.scenario_params:
        context_parts.append("--- SCENARIO SIMULATION PARAMETERS ---\n" + json.dumps(query.scenario_params, indent=2))
    if query.computed_risk_data:
        context_parts.append("--- COMPUTED RISK, CONCENTRATION & RED-FLAG METRICS ---\n" + json.dumps(query.computed_risk_data, indent=2))

    context_str = "\n\n" + "\n\n".join(context_parts) if context_parts else ""
    prompt = f"User Question: \"{query.question}\"{context_str}\n\nPlease provide a strategic CFA/FRM-grounded executive risk diagnosis and scenario interpretation."

    try:
        answer = await call_gemini_generic(prompt, SYSTEM_INSTRUCTION_L3, api_key)
        return Level3Response(
            answer=answer,
            framework='CFA Level 3 Strategic & FRM Risk Analysis'
        )
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error in analyze_level3_strategic_scenario: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="AI Level 3 Insights failed to generate analysis."
        )

@router.get('/compute-engine')
def get_computed_engine_data():
    """
    Server-side deterministic computation over the 1,728 transactions.
    Calculates monthly series, linear regressions, moving averages, concentration, and red flags.
    """
    from collections import defaultdict
    import math

    monthly = defaultdict(lambda: {"revenue": 0.0, "expenses": 0.0, "inflow": 0.0, "outflow": 0.0, "cogs": 0.0})
    customer_rev = defaultdict(float)
    vendor_exp = defaultdict(float)
    total_rev = 0.0
    total_exp = 0.0

    for t in TRANSACTIONS:
        month_key = t["date"][:7] # e.g. '2024-05'
        amt = float(t["amount"])
        cat = t["category"]
        desc = t["description"]

        if t["type"] == "credit":
            monthly[month_key]["inflow"] += amt
            if cat in ["Sales Revenue", "Export Sales", "Other Income"]:
                monthly[month_key]["revenue"] += amt
                total_rev += amt
                # Extract party from description if present
                if "Sales to " in desc:
                    party = desc.split("Sales to ")[-1].strip()
                    customer_rev[party] += amt
                elif "Payment received from " in desc:
                    party = desc.split("Payment received from ")[-1].strip()
                    customer_rev[party] += amt
        else:
            monthly[month_key]["outflow"] += amt
            if cat in ["Inventory Purchase", "Import Purchase"]:
                monthly[month_key]["cogs"] += amt
                monthly[month_key]["expenses"] += amt
                total_exp += amt
                if "from " in desc:
                    party = desc.split("from ")[-1].strip()
                    vendor_exp[party] += amt
            elif "Expense" in cat or cat in ["Utilities", "Fixed Asset", "Tax Expense", "Customs Duty"]:
                monthly[month_key]["expenses"] += amt
                total_exp += amt
                if "to " in desc:
                    party = desc.split("to ")[-1].strip()
                    vendor_exp[party] += amt

    sorted_months = sorted(monthly.keys())
    series = []
    running_cash = 1500000.0 # Initial equity baseline

    for m in sorted_months:
        d = monthly[m]
        net_cf = d["inflow"] - d["outflow"]
        running_cash += net_cf
        gross_prof = d["revenue"] - d["cogs"]
        gm_pct = round((gross_prof / d["revenue"] * 100), 2) if d["revenue"] > 0 else 0.0
        
        series.append({
            "month": m,
            "revenue": round(d["revenue"], 2),
            "expenses": round(d["expenses"], 2),
            "cogs": round(d["cogs"], 2),
            "grossProfit": round(gross_prof, 2),
            "grossMargin": gm_pct,
            "cashInflow": round(d["inflow"], 2),
            "cashOutflow": round(d["outflow"], 2),
            "netCashFlow": round(net_cf, 2),
            "closingCash": round(running_cash, 2)
        })

    # 3-Month Moving Average on Revenue & Cash
    for i in range(len(series)):
        start_idx = max(0, i - 2)
        window = series[start_idx:i+1]
        series[i]["revenue_3M_SMA"] = round(sum(w["revenue"] for w in window) / len(window), 2)
        series[i]["cash_3M_SMA"] = round(sum(w["closingCash"] for w in window) / len(window), 2)
        if i > 0:
            prev_rev = series[i-1]["revenue"]
            series[i]["momGrowthPct"] = round(((series[i]["revenue"] - prev_rev) / prev_rev * 100), 2) if prev_rev > 0 else 0.0
        else:
            series[i]["momGrowthPct"] = 0.0

    # OLS Linear Regression over historical revenue
    n = len(series)
    if n >= 2:
        x_vals = list(range(n))
        y_rev = [s["revenue"] for s in series]
        y_cash = [s["closingCash"] for s in series]

        x_mean = sum(x_vals) / n
        y_rev_mean = sum(y_rev) / n
        y_cash_mean = sum(y_cash) / n

        num_rev = sum((x_vals[i] - x_mean) * (y_rev[i] - y_rev_mean) for i in range(n))
        num_cash = sum((x_vals[i] - x_mean) * (y_cash[i] - y_cash_mean) for i in range(n))
        denom = sum((x_vals[i] - x_mean) ** 2 for i in range(n)) or 1.0

        slope_rev = num_rev / denom
        intercept_rev = y_rev_mean - (slope_rev * x_mean)

        slope_cash = num_cash / denom
        intercept_cash = y_cash_mean - (slope_cash * x_mean)

        # Generate Next 3 Projections (e.g. Month n, n+1, n+2)
        last_year = int(sorted_months[-1][:4])
        last_m = int(sorted_months[-1][5:7])

        projections = []
        for p in range(1, 4):
            pm = last_m + p
            py = last_year
            if pm > 12:
                pm -= 12
                py += 1
            p_month_key = f"{py}-{str(pm).padStart(2, '0') if hasattr(str(pm), 'padStart') else f'{pm:02d}'}"
            x_proj = n - 1 + p
            proj_rev = max(0, round(intercept_rev + slope_rev * x_proj, 2))
            proj_cash = round(intercept_cash + slope_cash * x_proj, 2)
            projections.append({
                "month": p_month_key,
                "projectedRevenue": proj_rev,
                "projectedCash": proj_cash,
                "isProjection": True,
                "method": f"OLS Linear Regression (Trailing {n} Months)"
            })
    else:
        projections = []

    # Concentration Metrics
    top_customers = sorted([{"name": k, "amount": round(v, 2), "pct": round(v/total_rev*100, 1) if total_rev else 0} for k, v in customer_rev.items()], key=lambda x: x["amount"], reverse=True)[:5]
    top_vendors = sorted([{"name": k, "amount": round(v, 2), "pct": round(v/total_exp*100, 1) if total_exp else 0} for k, v in vendor_exp.items()], key=lambda x: x["amount"], reverse=True)[:5]

    # Volatility & Runway
    rev_vals = [s["revenue"] for s in series if s["revenue"] > 0]
    mean_rev = sum(rev_vals) / len(rev_vals) if rev_vals else 1.0
    std_rev = math.sqrt(sum((r - mean_rev) ** 2 for r in rev_vals) / len(rev_vals)) if len(rev_vals) > 1 else 0.0
    cv_rev = round((std_rev / mean_rev * 100), 2)

    avg_monthly_exp = total_exp / n if n > 0 else 1.0
    runway_months = round(running_cash / avg_monthly_exp, 1) if avg_monthly_exp > 0 else 999.0

    return {
        "historicalSeries": series,
        "projections": projections,
        "regression": {
            "periodsAnalyzed": n,
            "revenueMonthlyTrendSlope": round(slope_rev, 2) if n >= 2 else 0,
            "cashMonthlyTrendSlope": round(slope_cash, 2) if n >= 2 else 0,
            "methodology": f"Ordinary Least Squares (OLS) Linear Regression over {n} operational months"
        },
        "concentration": {
            "topCustomers": top_customers,
            "topVendors": top_vendors,
            "top5CustomerRevenueSharePct": round(sum(c["pct"] for c in top_customers), 1),
            "top5VendorPayableSharePct": round(sum(v["pct"] for v in top_vendors), 1)
        },
        "riskMetrics": {
            "revenueVolatilityCV": cv_rev,
            "revenueStdDev": round(std_rev, 2),
            "cashRunwayMonths": runway_months,
            "currentCash": round(running_cash, 2),
            "avgMonthlyBurn": round(avg_monthly_exp, 2)
        }
    }

