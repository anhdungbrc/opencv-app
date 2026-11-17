"""Smoothing and blurring processors (Gaussian, Median, Bilateral, 2D Box Filter)."""

from typing import Any
import cv2
import numpy as np

from app.processors.base import BaseProcessor


class GaussianBlurProcessor(BaseProcessor):
    """Gaussian filtering for image noise reduction."""

    id = "blur_gaussian"
    name = "Gaussian Blur"
    category = "Smoothing"
    description = "Làm mịn ảnh bằng bộ lọc Gauss, khử nhiễu tần số cao hiệu quả."
    doc_url = "https://docs.opencv.org/3.4.20/d4/d13/tutorial_py_filtering.html"

    def get_parameter_schema(self) -> list[dict[str, Any]]:
        """Return kernel size and sigma."""
        return [
            {"name": "ksize", "label": "Cỡ Kernel (Lẻ)", "type": "slider", "min": 3, "max": 31, "step": 2, "default": 5},
            {"name": "sigmaX", "label": "Độ lệch chuẩn (SigmaX)", "type": "slider", "min": 0.0, "max": 10.0, "step": 0.5, "default": 1.5},
        ]

    def process(self, image: np.ndarray, params: dict[str, Any]) -> tuple[np.ndarray, dict[str, Any]]:
        """Apply Gaussian blur."""
        k = int(params.get("ksize", 5))
        if k % 2 == 0:
            k += 1
        sigma = float(params.get("sigmaX", 1.5))
        blurred = cv2.GaussianBlur(image, (k, k), sigma)
        return blurred, {"ksize": k, "sigmaX": sigma}


class MedianBlurProcessor(BaseProcessor):
    """Median filtering for salt-and-pepper noise removal."""

    id = "blur_median"
    name = "Median Blur"
    category = "Smoothing"
    description = "Thay thế từng pixel bằng trung vị của các pixel lân cận, loại bỏ nhiễu hạt tiêu (muối tiêu) xuất sắc."
    doc_url = "https://docs.opencv.org/3.4.20/d4/d13/tutorial_py_filtering.html"

    def get_parameter_schema(self) -> list[dict[str, Any]]:
        """Return kernel aperture size."""
        return [
            {"name": "ksize", "label": "Cỡ Kernel (Lẻ)", "type": "slider", "min": 3, "max": 31, "step": 2, "default": 5},
        ]

    def process(self, image: np.ndarray, params: dict[str, Any]) -> tuple[np.ndarray, dict[str, Any]]:
        """Apply median blur."""
        k = int(params.get("ksize", 5))
        if k % 2 == 0:
            k += 1
        blurred = cv2.medianBlur(image, k)
        return blurred, {"ksize": k}


class BilateralFilterProcessor(BaseProcessor):
    """Bilateral filtering for edge-preserving smoothing."""

    id = "blur_bilateral"
    name = "Bilateral Filter"
    category = "Smoothing"
    description = "Làm mịn các vùng đồng nhất nhưng giữ nguyên độ sắc nét của các đường viền/cạnh (Edge-preserving)."
    doc_url = "https://docs.opencv.org/3.4.20/d4/d13/tutorial_py_filtering.html"

    def get_parameter_schema(self) -> list[dict[str, Any]]:
        """Return bilateral filter diameter and sigmas."""
        return [
            {"name": "d", "label": "Đường kính lân cận (Diameter d)", "type": "slider", "min": 3, "max": 25, "step": 2, "default": 9},
            {"name": "sigmaColor", "label": "Sigma Màu sắc", "type": "slider", "min": 10, "max": 200, "step": 5, "default": 75},
            {"name": "sigmaSpace", "label": "Sigma Không gian", "type": "slider", "min": 10, "max": 200, "step": 5, "default": 75},
        ]

    def process(self, image: np.ndarray, params: dict[str, Any]) -> tuple[np.ndarray, dict[str, Any]]:
        """Apply bilateral filtering."""
        d = int(params.get("d", 9))
        s_color = float(params.get("sigmaColor", 75))
        s_space = float(params.get("sigmaSpace", 75))
        filtered = cv2.bilateralFilter(image, d, s_color, s_space)
        return filtered, {"d": d, "sigmaColor": s_color, "sigmaSpace": s_space}
