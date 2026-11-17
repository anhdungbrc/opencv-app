"""Healthcheck endpoint."""

from fastapi import APIRouter
from app.core.config import settings

router = APIRouter()


@router.get("/health")
def get_health() -> dict[str, str]:
    """Check service health and version."""
    return {"status": "ok", "version": settings.VERSION}
