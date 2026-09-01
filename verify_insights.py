import sys
sys.stdout.reconfigure(encoding='utf-8')
import asyncio
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_query(question):
    print(f"\n--- Testing Query: {question} ---")
    response = client.post("/api/insights/analyze", json={
        "question": question,
        "financial_context": {
            "cashBalance": 150000,
            "monthlyBurn": 25000,
            "revenue": 500000
        }
    })
    
    if response.status_code == 200:
        data = response.json()
        print("Response Answer:")
        print(data.get("answer"))
    else:
        print(f"Error {response.status_code}: {response.text}")

if __name__ == "__main__":
    from dotenv import load_dotenv
    load_dotenv()
    
    test_query("What's my likely cash position next month?")
    test_query("Show me a 5-year trend")
