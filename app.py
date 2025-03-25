"""
AI News Website - Main Application

This is the main entry point for the AI-driven news platform that:
- Uses Bayesian probability to synthesize non-biased news articles
- Finds connections between global events
- Makes market predictions using fractal market theory
"""

import os
import logging
from fastapi import FastAPI # type: ignore
from fastapi.staticfiles import StaticFiles # type: ignore
from fastapi.middleware.cors import CORSMiddleware # type: ignore

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler("app.log")
    ]
)
logger = logging.getLogger(__name__)

# Initialize FastAPI app
app = FastAPI(
    title="AI News Platform",
    description="An AI-driven news platform with Bayesian analysis and fractal market predictions",
    version="0.1.0"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Update this with specific origins in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mount static files (for frontend)
app.mount("/static", StaticFiles(directory="static"), name="static")

# Root endpoint
@app.get("/")
async def root():
    return {
        "message": "Welcome to the AI News Platform API",
        "status": "online",
        "version": "0.1.0"
    }

# Health check endpoint
@app.get("/health")
async def health_check():
    return {"status": "healthy"}

if __name__ == "__main__":
    import uvicorn # type: ignore
    logger.info("Starting AI News Platform API")
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)
