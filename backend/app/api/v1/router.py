from fastapi import APIRouter
from datetime import datetime, timezone
from app.core.config import settings
from app.schemas.common import HealthResponse

api_router = APIRouter()


@api_router.get("/health", response_model=HealthResponse, tags=["Health"])
def health_check():
    """Service health check endpoint."""
    return HealthResponse(
        status="ok",
        version="0.1.0",
        environment=settings.ENVIRONMENT,
        timestamp=datetime.now(timezone.utc),
    )
