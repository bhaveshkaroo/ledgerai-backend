import os
from fastapi import Request, HTTPException
from supabase import create_client, Client
from dotenv import load_dotenv

load_dotenv()

url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_SERVICE_ROLE_KEY")
supabase: Client = create_client(url, key)

async def auth_middleware(request: Request, call_next):
    # Exempt routes
    if request.url.path in ["/", "/docs", "/openapi.json"]:
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
