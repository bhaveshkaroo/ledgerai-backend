"""
LedgerAI Backend — main.py
Entry point for the FastAPI application.
Sets up CORS, loads environment variables, and mounts route files.
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Import route modules
from routes.transactions import router as transactions_router
from routes.reports import router as reports_router
from routes.ledger import router as ledger_router
from routes.gst import router as gst_router

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

# Mount the route files
app.include_router(transactions_router, prefix="/transactions")
app.include_router(reports_router, prefix="/reports")
app.include_router(ledger_router, prefix="/ledger")
app.include_router(gst_router, prefix="/gst")


@app.get("/")
def root():
    """Health-check endpoint — confirms the server is running."""
    return {"message": "LedgerAI is running"}
