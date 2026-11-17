"""Image processing execution endpoint."""

from fastapi import APIRouter, HTTPException, status
from app.processors.base import decode_image_base64, encode_image_base64
from app.processors.registry import get_processor
from app.schemas.process import ProcessRequest, ProcessResponse

router = APIRouter()


@router.post("/process", response_model=ProcessResponse)
def process_image(request: ProcessRequest) -> ProcessResponse:
    """Execute an image processing operation with custom parameters."""
    try:
        processor = get_processor(request.operation)
    except KeyError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Unknown operation: '{request.operation}'",
        )

    try:
        img = decode_image_base64(request.image_base64)
    except ValueError as exc:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail=f"Invalid image data: {exc}",
        ) from exc

    try:
        out_img, meta = processor.process(img, request.params)
        result_b64 = encode_image_base64(out_img)
        return ProcessResponse(
            success=True,
            operation=request.operation,
            result_image_base64=result_b64,
            metadata=meta,
        )
    except Exception as exc:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Processing failed: {exc}",
        ) from exc
