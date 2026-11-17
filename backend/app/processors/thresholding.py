"""Image thresholding operations (Simple, Adaptive, Otsu)."""

from typing import Any
import cv2
import numpy as np

from app.processors.base import BaseProcessor


class SimpleThresholdProcessor(BaseProcessor):
    """Applies simple thresholding to an image using cv2.threshold."""

    id = "threshold_simple"
    name = "Simple Thresholding"
    category = "Thresholding"
    description = "Nhị phân hóa ảnh bằng ngưỡng cố định (cv2.THRESH_BINARY, BINARY_INV, TRUNC...)."
    doc_url = "https://docs.opencv.org/3.4.20/d7/d4d/tutorial_py_thresholding.html"

    def get_parameter_schema(self) -> list[dict[str, Any]]:
        """Return parameters for threshold value and type selection."""
        return [
            {"name": "thresh", "label": "Ngưỡng (Threshold)", "type": "slider", "min": 0, "max": 255, "step": 1, "default": 127},
            {"name": "maxval", "label": "Giá trị cực đại (Maxval)", "type": "slider", "min": 0, "max": 255, "step": 1, "default": 255},
            {
                "name": "type",
                "label": "Loại ngưỡng",
                "type": "select",
                "default": "BINARY",
                "options": ["BINARY", "BINARY_INV", "TRUNC", "TOZERO", "TOZERO_INV"],
            },
        ]

    def process(self, image: np.ndarray, params: dict[str, Any]) -> tuple[np.ndarray, dict[str, Any]]:
        """Apply simple thresholding."""
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) if len(image.shape) == 3 else image
        thresh_val = int(params.get("thresh", 127))
        max_val = int(params.get("maxval", 255))
        type_str = str(params.get("type", "BINARY")).upper()

        cv_type = getattr(cv2, f"THRESH_{type_str}", cv2.THRESH_BINARY)
        ret, thresh_img = cv2.threshold(gray, thresh_val, max_val, cv_type)

        return thresh_img, {
            "thresh_applied": float(ret),
            "white_pixels": int(np.count_nonzero(thresh_img)),
        }


class AdaptiveThresholdProcessor(BaseProcessor):
    """Applies adaptive thresholding where threshold is calculated per neighborhood block."""

    id = "threshold_adaptive"
    name = "Adaptive Thresholding"
    category = "Thresholding"
    description = "Nhị phân hóa thích nghi theo từng vùng lân cận (Mean hoặc Gaussian), xử lý tốt ảnh ánh sáng không đều."
    doc_url = "https://docs.opencv.org/3.4.20/d7/d4d/tutorial_py_thresholding.html"

    def get_parameter_schema(self) -> list[dict[str, Any]]:
        """Return adaptive method, block size and C constant."""
        return [
            {
                "name": "method",
                "label": "Phương pháp",
                "type": "select",
                "default": "GAUSSIAN_C",
                "options": ["MEAN_C", "GAUSSIAN_C"],
            },
            {"name": "blockSize", "label": "Kích thước khối (Lẻ)", "type": "slider", "min": 3, "max": 51, "step": 2, "default": 11},
            {"name": "C", "label": "Hằng số C", "type": "slider", "min": -20, "max": 20, "step": 1, "default": 2},
        ]

    def process(self, image: np.ndarray, params: dict[str, Any]) -> tuple[np.ndarray, dict[str, Any]]:
        """Apply adaptive thresholding."""
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) if len(image.shape) == 3 else image
        method_str = str(params.get("method", "GAUSSIAN_C"))
        adaptive_method = cv2.ADAPTIVE_THRESH_GAUSSIAN_C if method_str == "GAUSSIAN_C" else cv2.ADAPTIVE_THRESH_MEAN_C
        block_size = int(params.get("blockSize", 11))
        # Ensure block size is strictly odd and >= 3
        if block_size % 2 == 0:
            block_size += 1
        c_const = float(params.get("C", 2.0))

        thresh_img = cv2.adaptiveThreshold(
            gray, 255, adaptive_method, cv2.THRESH_BINARY, block_size, c_const
        )
        return thresh_img, {"block_size": block_size, "c_const": c_const}


class OtsuThresholdProcessor(BaseProcessor):
    """Applies automatic binarization using Otsu's thresholding algorithm."""

    id = "threshold_otsu"
    name = "Otsu's Binarization"
    category = "Thresholding"
    description = "Tự động tính ngưỡng tối ưu giảm phương sai giữa hai nhóm điểm ảnh bằng thuật toán Otsu."
    doc_url = "https://docs.opencv.org/3.4.20/d7/d4d/tutorial_py_thresholding.html"

    def get_parameter_schema(self) -> list[dict[str, Any]]:
        """Return optional Gaussian blur preprocessing parameter."""
        return [
            {"name": "blur", "label": "Làm mờ trước khi nhị phân (Gaussian)", "type": "checkbox", "default": True},
            {"name": "ksize", "label": "Cỡ Kernel làm mờ", "type": "slider", "min": 3, "max": 21, "step": 2, "default": 5},
        ]

    def process(self, image: np.ndarray, params: dict[str, Any]) -> tuple[np.ndarray, dict[str, Any]]:
        """Execute Otsu's thresholding."""
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) if len(image.shape) == 3 else image
        if params.get("blur", True):
            k = int(params.get("ksize", 5))
            if k % 2 == 0:
                k += 1
            gray = cv2.GaussianBlur(gray, (k, k), 0)

        ret, thresh_img = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
        return thresh_img, {"optimal_otsu_threshold": float(ret)}
