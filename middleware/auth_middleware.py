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

async def auth_middleware(request: Request, call_next):
    # AUTH POLICY DECISION:
    # In this investor demo phase (single-company prototype), unauthenticated requests are
    # allowed through so demo users can explore without required login ceremonies.
    # When upgrading to multi-tenant production, strict token validation must be enabled here.
    if request.url.path in ["/", "/docs", "/openapi.json"] or request.url.path.startswith("/api/ai") or not supabase:
        return await call_next(request)
    
    auth_header = request.headers.get("Authorization")
    if not auth_header or not auth_header.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Unauthorized: Missing token")
    
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
