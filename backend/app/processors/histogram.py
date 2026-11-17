"""Histogram calculation and equalization processors."""

from typing import Any
import cv2
import numpy as np

from app.processors.base import BaseProcessor


class HistogramEqualizationProcessor(BaseProcessor):
    """Histogram equalization for dynamic range enhancement."""

    id = "histogram_equalize"
    name = "Histogram Equalization"
    category = "Histograms"
    description = "Cân bằng biểu đồ sáng (Histogram Equalization) để tăng cường độ tương phản tự nhiên của ảnh mờ hoặc tối."
    doc_url = "https://docs.opencv.org/3.4.20/d4/d1b/tutorial_py_histograms_equalization.html"

    def get_parameter_schema(self) -> list[dict[str, Any]]:
        """Return CLAHE or Global Equalization selector."""
        return [
            {
                "name": "method",
                "label": "Phương pháp cân bằng",
                "type": "select",
                "default": "CLAHE",
                "options": ["GLOBAL", "CLAHE"],
            },
            {"name": "clipLimit", "label": "CLAHE Clip Limit", "type": "slider", "min": 1.0, "max": 10.0, "step": 0.5, "default": 2.0},
            {"name": "tileGridSize", "label": "Cỡ ô lưới CLAHE", "type": "slider", "min": 2, "max": 16, "step": 2, "default": 8},
        ]

    def process(self, image: np.ndarray, params: dict[str, Any]) -> tuple[np.ndarray, dict[str, Any]]:
        """Execute histogram equalization."""
        method = str(params.get("method", "CLAHE")).upper()

        if len(image.shape) == 3:
            # For color image, equalize V channel in HSV space to preserve original hue and saturation
            hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
            h, s, v = cv2.split(hsv)

            if method == "GLOBAL":
                v_eq = cv2.equalizeHist(v)
            else:
                clip = float(params.get("clipLimit", 2.0))
                grid = int(params.get("tileGridSize", 8))
                clahe = cv2.createCLAHE(clipLimit=clip, tileGridSize=(grid, grid))
                v_eq = clahe.apply(v)

            result = cv2.cvtColor(cv2.merge([h, s, v_eq]), cv2.COLOR_HSV2BGR)
        else:
            if method == "GLOBAL":
                result = cv2.equalizeHist(image)
            else:
                clip = float(params.get("clipLimit", 2.0))
                grid = int(params.get("tileGridSize", 8))
                clahe = cv2.createCLAHE(clipLimit=clip, tileGridSize=(grid, grid))
                result = clahe.apply(image)

        return result, {"method": method}
