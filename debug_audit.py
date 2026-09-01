import asyncio
import json
import os
import sys
sys.path.insert(0, '.')
from dotenv import load_dotenv
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '.env'))

async def test():
    api_key = os.getenv('GEMINI_API_KEY')
    print('Key present:', bool(api_key))

    payload = {
        "contents": [{"parts": [{"text": "User question: \"Why did my cash balance change this month?\"\n\n--- CURRENT FINANCIAL DATA ---\nCash & Bank Balance: 6,871,600\nTotal Revenue: 6,600,000\nNet Profit: 1,260,000\n--- END FINANCIAL DATA ---"}]}],
        "systemInstruction": {"parts": [{"text": "You are Meso AI Audit Assistant. Return ONLY a valid JSON object: {\"answer\": \"string\", \"scope\": \"in_scope\"}"}]},
        "generationConfig": {"responseMimeType": "application/json", "temperature": 0.3}
    }
    payload_json = json.dumps(payload)
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-3.6-flash:generateContent?key={api_key}"

    proc = await asyncio.create_subprocess_exec(
        "curl.exe", "-s", "-X", "POST", url,
        "-H", "Content-Type: application/json",
        "-d", payload_json,
        stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
    )
    stdout, stderr = await proc.communicate()
    raw = stdout.decode("utf-8")
    print("Raw response:", raw[:2000])

asyncio.run(test())
