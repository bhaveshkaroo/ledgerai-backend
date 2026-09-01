import os
import json
import logging
import asyncio
from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel
from typing import Dict, Any, Optional

logger = logging.getLogger(__name__)

router = APIRouter()

class InsightsQuery(BaseModel):
    question: str
    financial_context: Optional[Dict[str, Any]] = None

class InsightsResponse(BaseModel):
    answer: str
    framework: str = 'CFA Level 1 Analysis'

SYSTEM_INSTRUCTION = """You are a senior financial analyst and CFO for an Indian MSME.
Your role is to analyze the user's financial context and provide strategic, actionable insights answering their question.
Format your answer clearly using bullet points and appropriate financial terminology.
Always use the financial data provided in the context to support your analysis.
Always append this exact disclaimer at the very end of your response: "⚠️ This is an AI-generated analysis based on current ledger data. Please consult a qualified financial advisor before making strategic decisions."
"""

PRIMARY_MODEL = "gemini-3.6-flash"
FALLBACK_MODEL = "gemini-3.5-flash"

async def call_gemini_insights(prompt: str, api_key: str) -> str:
    """
    Calls Gemini API using curl.exe subprocess for insights generation.
    """
    payload = {
        "contents": [
            {
                "parts": [
                    {"text": prompt}
                ]
            }
        ],
        "systemInstruction": {
            "parts": [
                {"text": SYSTEM_INSTRUCTION}
            ]
        },
        "generationConfig": {
            "responseMimeType": "text/plain",
            "temperature": 0.4
        }
    }

    payload_json = json.dumps(payload)

    for model in [PRIMARY_MODEL, FALLBACK_MODEL]:
        url = f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent?key={api_key}"

        proc = await asyncio.create_subprocess_exec(
            "curl.exe", "-s", "-X", "POST", url,
            "-H", "Content-Type: application/json",
            "-d", payload_json,
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
            if code == 429:
                raise HTTPException(
                    status_code=status.HTTP_429_TOO_MANY_REQUESTS,
                    detail="AI Insights rate limit reached — please try again shortly."
                )
            elif code in [400, 401, 403]:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="AI Insights authentication error — please verify API key."
                )
            continue

        candidates = res_data.get("candidates", [])
        if candidates and "content" in candidates[0]:
            parts = candidates[0]["content"].get("parts", [])
            if parts and "text" in parts[0]:
                return parts[0]["text"]

    raise HTTPException(
        status_code=status.HTTP_502_BAD_GATEWAY,
        detail="AI Insights unavailable — please try again."
    )

@router.get('/health')
def health_check():
    return {'status': 'healthy', 'module': 'insights'}

@router.post('/analyze', response_model=InsightsResponse)
async def analyze_financials(query: InsightsQuery):
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
        answer = await call_gemini_insights(prompt, api_key)
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
