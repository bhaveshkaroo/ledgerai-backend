import asyncio
import os
import sys
import json
sys.path.insert(0, '.')
from dotenv import load_dotenv
from routes.ai_audit import audit_query, AuditQuery

# Load the environment properly
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '.env'))

# The financial context payload
ctx = {
    "cashBalance": 6871600,
    "totalRevenue": 6600000,
    "totalExpenses": 4890000,
    "netProfit": 1260000,
    "totalAssets": 10927850,
    "totalEquityAndLiabilities": 10927850,
    "bsBalanced": True,
    "totalDebits": 15500000,
    "totalCredits": 15500000,
    "transactionCount": 48
}

queries = [
    "Why did my cash balance change this month?",
    "Check my ledger for any duplicate entries.",
    "Are my provisions AS 29 compliant?",
    "What is the weather today?"
]

async def run_tests():
    for i, q in enumerate(queries, 1):
        print(f"\n=== TEST {i} ===")
        print(f"Question: {q}")
        req = AuditQuery(question=q, financial_context=ctx)
        try:
            res = await audit_query(req)
            print(f"Response (Scope: {res.scope}):\n{res.answer}")
        except Exception as e:
            print(f"ERROR: {type(e).__name__}: {str(e)}")

# Ensure Windows ProactorEventLoop is used to avoid NotImplementedError with subprocess
if sys.platform == 'win32':
    asyncio.set_event_loop_policy(asyncio.WindowsProactorEventLoopPolicy())

asyncio.run(run_tests())
