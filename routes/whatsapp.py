"""
routes/whatsapp.py - WhatsApp Cloud API Webhook Handler
Handles:
1. GET /api/v1/whatsapp/webhook -> Meta Webhook Verification handshake
2. POST /api/v1/whatsapp/webhook -> Incoming messages (Receipt photos, text commands)
"""

import os
import logging
from fastapi import APIRouter, Request, Response, Query, HTTPException
from fastapi.responses import PlainTextResponse

logger = logging.getLogger("whatsapp_webhook")
router = APIRouter()

# Webhook Verification Token (must match what is entered in Meta Developer Portal)
VERIFY_TOKEN = os.getenv("WHATSAPP_VERIFY_TOKEN", "meso_secret_verify_token_2026")

@router.get("/webhook")
async def verify_webhook(request: Request):
    """
    Meta Webhook Verification Handshake
    Meta calls this GET endpoint when you click 'Verify and Save' in App Dashboard.
    Query params sent by Meta:
    hub.mode = 'subscribe'
    hub.challenge = <integer / string challenge>
    hub.verify_token = <your verify token>
    """
    params = request.query_params
    hub_mode = params.get("hub.mode")
    hub_challenge = params.get("hub.challenge")
    hub_verify_token = params.get("hub.verify_token")

    logger.info(f"Verification request: mode={hub_mode}, challenge={hub_challenge}")
    
    if hub_mode == "subscribe" and hub_verify_token == VERIFY_TOKEN:
        logger.info("Webhook successfully verified by Meta!")
        return PlainTextResponse(content=str(hub_challenge), status_code=200)
    
    logger.warning(f"Verification mismatch: got '{hub_verify_token}', expected '{VERIFY_TOKEN}'")
    raise HTTPException(status_code=403, detail="Verification token mismatch")

@router.post("/webhook")
async def handle_whatsapp_message(request: Request):
    """
    Incoming WhatsApp events from Meta Cloud API.
    Handles incoming receipt photos, PDF bills, and text queries.
    """
    try:
        payload = await request.json()
    except Exception:
        return Response(content="Invalid JSON", status_code=400)

    # Check if entry exists in payload
    entries = payload.get("entry", [])
    for entry in entries:
        changes = entry.get("changes", [])
        for change in changes:
            value = change.get("value", {})
            messages = value.get("messages", [])
            
            for msg in messages:
                sender = msg.get("from")
                msg_type = msg.get("type")
                
                # Case 1: Image / Document received (Receipt / Bill photo)
                if msg_type in ["image", "document"]:
                    media_id = msg.get(msg_type, {}).get("id")
                    logger.info(f"Received receipt {msg_type} {media_id} from {sender}")

                # Case 2: Text received
                elif msg_type == "text":
                    body = msg.get("text", {}).get("body", "")
                    logger.info(f"Received text message from {sender}: {body}")

    # Meta expects an immediate 200 OK
    return Response(content="EVENT_RECEIVED", status_code=200)
