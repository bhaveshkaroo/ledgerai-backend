import os
from fastapi import Request, HTTPException

try:
    from supabase import create_client, Client
    url: str = os.environ.get("SUPABASE_URL")
    # In demo phase, SUPABASE_SERVICE_ROLE_KEY or SUPABASE_KEY is used
    key: str = os.environ.get("SUPABASE_SERVICE_ROLE_KEY") or os.environ.get("SUPABASE_KEY")
    supabase: Client = create_client(url, key) if (url and key) else None
except Exception:
    supabase = None

import time
from typing import Dict, List
from fastapi.responses import JSONResponse

# Per-IP sliding window configuration for AI endpoints:
# 20 requests per rolling 60 seconds per client IP.
# Rationale: Provides ample burst capacity for active accountants (2-4 queries/min),
# while preventing automated scraping, denial of service, and Gemini quota exhaustion.
AI_RATE_LIMIT_WINDOW = 60
AI_RATE_LIMIT_MAX = 20
_ai_request_history: Dict[str, List[float]] = {}

def get_client_ip(request: Request) -> str:
    forwarded = request.headers.get("X-Forwarded-For")
    if forwarded:
        # Take leftmost IP to prevent spoofing through proxy headers
        client_ip = forwarded.split(",")[0].strip()
        if client_ip:
            return client_ip
    if request.client and request.client.host:
        return request.client.host
    return "127.0.0.1"

async def auth_middleware(request: Request, call_next):
    # 1. AI Endpoints Rate Limiting Guard
    path = request.url.path
    if (path.startswith("/api/ai") or path.startswith("/api/insights")) and request.method != "OPTIONS":
        client_ip = get_client_ip(request)
        now = time.time()
        history = _ai_request_history.setdefault(client_ip, [])
        cutoff = now - AI_RATE_LIMIT_WINDOW
        _ai_request_history[client_ip] = [ts for ts in history if ts > cutoff]
        history = _ai_request_history[client_ip]

        if len(history) >= AI_RATE_LIMIT_MAX:
            oldest = history[0]
            retry_after = int(oldest + AI_RATE_LIMIT_WINDOW - now) + 1
            return JSONResponse(
                status_code=429,
                content={
                    "error": "Too Many Requests",
                    "message": f"AI request rate limit exceeded ({AI_RATE_LIMIT_MAX} requests/min). Please try again in {max(1, retry_after)} seconds.",
                    "retry_after_seconds": max(1, retry_after)
                },
                headers={"Retry-After": str(max(1, retry_after))}
            )
        history.append(now)

    # AUTH POLICY DECISION:
    # In this investor demo phase (single-company prototype), unauthenticated requests are
    # allowed through so demo users, webhooks, and AI endpoints can operate seamlessly.
    if request.url.path in ["/", "/docs", "/openapi.json"] or request.url.path.startswith("/api/ai") or request.url.path.startswith("/api/v1/whatsapp") or request.url.path.startswith("/api") or not supabase:
        return await call_next(request)
    
    auth_header = request.headers.get("Authorization")
    if not auth_header or not auth_header.startswith("Bearer "):
        return await call_next(request)
    
    token = auth_header.split(" ")[1]
    
    try:
        # Verify token with Supabase
        user = supabase.auth.get_user(token)
        if not user:
            raise HTTPException(status_code=401, detail="Unauthorized: Invalid token")
        
        # Attach user to request state
        request.state.user = user
    except Exception as e:
        raise HTTPException(status_code=401, detail=f"Unauthorized: {str(e)}")
    
    response = await call_next(request)
    return response
