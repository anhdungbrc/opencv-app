"""Endpoint listing available operations and their parameter schemas."""

from typing import Any
from fastapi import APIRouter
from app.processors.registry import list_operations

router = APIRouter()


@router.get("/operations")
def get_operations() -> list[dict[str, Any]]:
    """Retrieve full catalog of registered OpenCV operations and parameter metadata."""
    return list_operations()
