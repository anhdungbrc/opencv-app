"""Aggregation of API v1 routers."""

from fastapi import APIRouter
from app.api.v1.endpoints import health, operations, process

api_router = APIRouter()
api_router.include_router(health.router, tags=["System"])
api_router.include_router(operations.router, tags=["Operations"])
api_router.include_router(process.router, tags=["Processing"])
