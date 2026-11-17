"""Base class and image encoding/decoding utilities for OpenCV processors."""

from abc import ABC, abstractmethod
import base64
from typing import Any
import cv2
import numpy as np


def decode_image_base64(base64_str: str) -> np.ndarray:
    """Decode a base64 encoded image string into an OpenCV BGR numpy array.

    Args:
        base64_str: Base64 data string (with or without 'data:image/...;base64,' prefix).

    Returns:
        3-channel BGR numpy array (uint8).

    Raises:
        ValueError: If base64 decoding fails or image data is corrupted.
    """
    if "," in base64_str:
        # Strip data URL prefix if present (e.g. data:image/png;base64,...)
        base64_str = base64_str.split(",", 1)[1]

    try:
        raw_bytes = base64.b64decode(base64_str)
    except Exception as exc:
        raise ValueError(f"Invalid base64 payload: {exc}") from exc

    nparr = np.frombuffer(raw_bytes, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    if img is None:
        raise ValueError("Decoded image buffer could not be parsed by OpenCV.")
    return img


def encode_image_base64(image: np.ndarray, ext: str = ".png") -> str:
    """Encode an OpenCV numpy array into a base64 PNG/JPEG string.

    Args:
        image: Numpy array image (1-channel or 3-channel uint8).
        ext: Target image extension for encoding (.png or .jpg).

    Returns:
        Base64 encoded string.

    Raises:
        ValueError: If cv2.imencode fails.
    """
    success, buffer = cv2.imencode(ext, image)
    if not success:
        raise ValueError("Failed to encode image array to buffer.")
    return base64.b64encode(buffer).decode("utf-8")


class BaseProcessor(ABC):
    """Abstract base class for all OpenCV image processing operations."""

    id: str = "base"
    name: str = "Base Operation"
    category: str = "General"
    description: str = ""
    doc_url: str = "https://docs.opencv.org/3.4.20/d2/d96/tutorial_py_table_of_contents_imgproc.html"

    @abstractmethod
    def get_parameter_schema(self) -> list[dict[str, Any]]:
        """Return schema descriptors for operation parameters (used by UI to render controls).

        Returns:
            List of dictionaries containing parameter definitions (name, type, default, min, max, options).
        """
        pass

    @abstractmethod
    def process(self, image: np.ndarray, params: dict[str, Any]) -> tuple[np.ndarray, dict[str, Any]]:
        """Execute the OpenCV algorithm on the input image.

        Args:
            image: Input image array in BGR format (H, W, 3) or Grayscale (H, W).
            params: Dictionary of parameter values matching the schema.

        Returns:
            Tuple of (processed_image, metadata_dict).
        """
        pass
