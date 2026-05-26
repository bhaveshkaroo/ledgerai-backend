from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import anthropic
import os
from dotenv import load_dotenv

load_dotenv()

router = APIRouter()

client = anthropic.Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))

class ComplianceRequest(BaseModel):
    question: str

@router.post("/ask")
async def ask_compliance(req: ComplianceRequest):
    if not os.environ.get("ANTHROPIC_API_KEY"):
        # Mock response if key is missing (for local testing without key)
        return {"answer": "Indian Accounting Standards (Ind AS) 115 governs revenue recognition. It requires a 5-step model. Example: If you sell textiles, record revenue when control passes to the buyer. Standard: Ind AS 115."}

    try:
        system_prompt = (
            "You are an expert Indian Chartered Accountant and compliance advisor with deep knowledge of all "
            "Indian Accounting Standards including Ind AS issued by the Institute of Chartered Accountants of India, "
            "all ICAI pronouncements and guidance notes, GST laws including the Central Goods and Services Tax Act 2017 "
            "and all subsequent circulars and notifications, the Companies Act 2013 and its rules, Income Tax Act 1961 "
            "especially provisions relevant to businesses, and TDS provisions under the Income Tax Act. When answering "
            "questions always cite the specific standard number, section number, or circular number that applies. "
            "Structure your answer clearly with the applicable standard first, then the explanation, then a practical "
            "example relevant to Indian MSMEs. If the question involves GST calculations show the working step by step. "
            "If the question involves accounting treatment show the journal entry. Always answer in the context of "
            "Indian law and Indian accounting standards, not international standards unless specifically asked."
        )
        
        response = client.messages.create(
            model="claude-3-5-sonnet-20241022",
            max_tokens=1024,
            system=system_prompt,
            messages=[
                {"role": "user", "content": req.question}
            ]
        )
        
        return {"answer": response.content[0].text}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
