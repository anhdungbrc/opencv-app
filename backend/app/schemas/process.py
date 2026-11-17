"""Pydantic schemas for API request and response data structures."""

from typing import Any
from pydantic import BaseModel, Field


class ProcessRequest(BaseModel):
    """Payload sent by client to request an image processing operation."""

    image_base64: str = Field(..., description="Base64 encoded string of input image")
    operation: str = Field(..., description="Unique ID of operation to apply")
    params: dict[str, Any] = Field(default_factory=dict, description="Parameters dictionary for operation")


class ProcessResponse(BaseModel):
    """Result payload returned to client after image processing."""

    success: bool
    operation: str
    result_image_base64: str = ""
    metadata: dict[str, Any] = Field(default_factory=dict)
    error: str | None = None
