"""
LedgerAI Backend - main.py
Entry point for the FastAPI application.
Sets up CORS, loads environment variables, and mounts route files.
"""

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
from middleware.auth_middleware import auth_middleware

# Load environment variables from .env file
load_dotenv()

# Import route modules
from routes import transactions
from routes import reports
from routes import ledger
from routes import gst
from routes import compliance
from routes import ai_entry
from routes import ai_audit

# Create the FastAPI application
app = FastAPI(
    title="LedgerAI",
    description="AI-powered accounting platform for Indian MSMEs",
    version="1.0.0",
)

# Enable CORS so the frontend can communicate with this backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],       # Allow all origins (frontend URLs)
    allow_credentials=True,
    allow_methods=["*"],       # Allow all HTTP methods
    allow_headers=["*"],       # Allow all headers
)

# Register Auth Middleware
@app.middleware("http")
async def add_auth_middleware(request: Request, call_next):
    return await auth_middleware(request, call_next)

# Mount the route files
app.include_router(transactions.router, prefix="/api/transactions", tags=["Transactions"])
app.include_router(reports.router, prefix="/api/reports", tags=["Reports"])
app.include_router(compliance.router, prefix="/api/compliance", tags=["Compliance"])
app.include_router(gst.router, prefix="/api/gst", tags=["GST"])
app.include_router(ledger.router, prefix="/api/ledger", tags=["Ledger"])
app.include_router(ai_entry.router, prefix="/api/ai", tags=["AI"])
app.include_router(ai_audit.router, prefix="/api/ai", tags=["AI"])

@app.get("/")
def root():
    """Health-check endpoint"""
    return {"message": "LedgerAI is running"}
