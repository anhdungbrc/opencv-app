"""Colorspace conversion and color-filtering processors."""

from typing import Any
import cv2
import numpy as np

from app.processors.base import BaseProcessor


class BGR2GrayProcessor(BaseProcessor):
    """Converts a BGR image to Grayscale."""

    id = "bgr_to_gray"
    name = "BGR to Grayscale"
    category = "Colorspaces"
    description = "Chuyển đổi ảnh màu BGR sang ảnh xám 1 kênh bằng cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)."
    doc_url = "https://docs.opencv.org/3.4.20/df/d9d/tutorial_py_colorspaces.html"

    def get_parameter_schema(self) -> list[dict[str, Any]]:
        """No adjustable parameters needed for standard grayscale conversion."""
        return []

    def process(self, image: np.ndarray, params: dict[str, Any]) -> tuple[np.ndarray, dict[str, Any]]:
        """Convert BGR image to Grayscale."""
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        return gray, {"channels": 1, "mean_intensity": float(np.mean(gray))}


class BGR2HSVProcessor(BaseProcessor):
    """Converts a BGR image to HSV colorspace."""

    id = "bgr_to_hsv"
    name = "BGR to HSV"
    category = "Colorspaces"
    description = "Chuyển ảnh sang không gian màu HSV (Hue, Saturation, Value) để phân đoạn màu dễ dàng."
    doc_url = "https://docs.opencv.org/3.4.20/df/d9d/tutorial_py_colorspaces.html"

    def get_parameter_schema(self) -> list[dict[str, Any]]:
        """No adjustable parameters for direct conversion."""
        return []

    def process(self, image: np.ndarray, params: dict[str, Any]) -> tuple[np.ndarray, dict[str, Any]]:
        """Convert BGR image to HSV format."""
        hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        return hsv, {"channels": 3, "format": "HSV"}


class ColorFilterInRangeProcessor(BaseProcessor):
    """Filters colors using cv2.inRange thresholding in HSV space."""

    id = "color_filter_hsv"
    name = "Color Filter (HSV inRange)"
    category = "Colorspaces"
    description = "Lọc giữ lại một dải màu nhất định (ví dụ: đỏ, xanh, vàng) bằng cv2.inRange."
    doc_url = "https://docs.opencv.org/3.4.20/df/d9d/tutorial_py_colorspaces.html"

    def get_parameter_schema(self) -> list[dict[str, Any]]:
        """Return HSV range boundary sliders."""
        return [
            {"name": "h_min", "label": "Hue Min", "type": "slider", "min": 0, "max": 179, "step": 1, "default": 0},
            {"name": "h_max", "label": "Hue Max", "type": "slider", "min": 0, "max": 179, "step": 1, "default": 179},
            {"name": "s_min", "label": "Sat Min", "type": "slider", "min": 0, "max": 255, "step": 1, "default": 50},
            {"name": "s_max", "label": "Sat Max", "type": "slider", "min": 0, "max": 255, "step": 1, "default": 255},
            {"name": "v_min", "label": "Val Min", "type": "slider", "min": 0, "max": 255, "step": 1, "default": 50},
            {"name": "v_max", "label": "Val Max", "type": "slider", "min": 0, "max": 255, "step": 1, "default": 255},
        ]

    def process(self, image: np.ndarray, params: dict[str, Any]) -> tuple[np.ndarray, dict[str, Any]]:
        """Extract binary mask of pixels within specified HSV range."""
        hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        lower = np.array([
            int(params.get("h_min", 0)),
            int(params.get("s_min", 50)),
            int(params.get("v_min", 50)),
        ], dtype=np.uint8)
        upper = np.array([
            int(params.get("h_max", 179)),
            int(params.get("s_max", 255)),
            int(params.get("v_max", 255)),
        ], dtype=np.uint8)

        mask = cv2.inRange(hsv, lower, upper)
        # Apply mask on original image to highlight filtered color
        result = cv2.bitwise_and(image, image, mask=mask)
        matched_pixels = int(np.count_nonzero(mask))
        total_pixels = int(image.shape[0] * image.shape[1])

        return result, {
            "matched_pixels": matched_pixels,
            "matched_ratio": round(matched_pixels / total_pixels, 4),
        }
