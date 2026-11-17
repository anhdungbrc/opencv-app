"""Edge detection and image gradient processors (Canny, Sobel, Laplacian)."""

from typing import Any
import cv2
import numpy as np

from app.processors.base import BaseProcessor


class CannyEdgeProcessor(BaseProcessor):
    """Canny edge detector with hysteresis thresholding."""

    id = "canny_edge"
    name = "Canny Edge Detection"
    category = "Edges & Gradients"
    description = "Thuật toán phát hiện cạnh kinh điển của John F. Canny với lọc Gauss, gradient và phân ngưỡng trễ."
    doc_url = "https://docs.opencv.org/3.4.20/da/d22/tutorial_py_canny.html"

    def get_parameter_schema(self) -> list[dict[str, Any]]:
        """Return Canny thresholds and aperture size."""
        return [
            {"name": "threshold1", "label": "Ngưỡng dưới (Min Val)", "type": "slider", "min": 0, "max": 255, "step": 5, "default": 100},
            {"name": "threshold2", "label": "Ngưỡng trên (Max Val)", "type": "slider", "min": 0, "max": 255, "step": 5, "default": 200},
            {"name": "apertureSize", "label": "Cỡ Sobel Aperture", "type": "select", "default": 3, "options": [3, 5, 7]},
            {"name": "L2gradient", "label": "Chuẩn L2 chính xác hơn", "type": "checkbox", "default": False},
        ]

    def process(self, image: np.ndarray, params: dict[str, Any]) -> tuple[np.ndarray, dict[str, Any]]:
        """Apply Canny edge detector."""
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) if len(image.shape) == 3 else image
        t1 = int(params.get("threshold1", 100))
        t2 = int(params.get("threshold2", 200))
        aperture = int(params.get("apertureSize", 3))
        l2 = bool(params.get("L2gradient", False))

        edges = cv2.Canny(gray, t1, t2, apertureSize=aperture, L2gradient=l2)
        edge_count = int(np.count_nonzero(edges))
        total_pixels = int(gray.shape[0] * gray.shape[1])

        return edges, {
            "edge_pixels_count": edge_count,
            "edge_density": round(edge_count / total_pixels, 4),
        }


class SobelProcessor(BaseProcessor):
    """Sobel derivative gradient detector along X, Y or combined."""

    id = "sobel_gradient"
    name = "Sobel Gradient"
    category = "Edges & Gradients"
    description = "Tính đạo hàm không gian bậc nhất theo trục X, Y hoặc hợp nhất độ lớn gradient."
    doc_url = "https://docs.opencv.org/3.4.20/d5/d0f/tutorial_py_gradients.html"

    def get_parameter_schema(self) -> list[dict[str, Any]]:
        """Return directional derivative and kernel size."""
        return [
            {
                "name": "direction",
                "label": "Hướng gradient",
                "type": "select",
                "default": "COMBINED",
                "options": ["X", "Y", "COMBINED"],
            },
            {"name": "ksize", "label": "Cỡ Kernel (1, 3, 5, 7)", "type": "select", "default": 3, "options": [1, 3, 5, 7]},
        ]

    def process(self, image: np.ndarray, params: dict[str, Any]) -> tuple[np.ndarray, dict[str, Any]]:
        """Compute Sobel edge gradient."""
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) if len(image.shape) == 3 else image
        direction = str(params.get("direction", "COMBINED")).upper()
        ksize = int(params.get("ksize", 3))

        if direction == "X":
            grad = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=ksize)
            abs_grad = np.uint8(np.absolute(grad))
        elif direction == "Y":
            grad = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=ksize)
            abs_grad = np.uint8(np.absolute(grad))
        else:
            grad_x = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=ksize)
            grad_y = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=ksize)
            mag = cv2.magnitude(grad_x, grad_y)
            abs_grad = np.uint8(np.clip(mag, 0, 255))

        return abs_grad, {"direction": direction, "ksize": ksize}


class LaplacianProcessor(BaseProcessor):
    """Laplacian second derivative edge detector."""

    id = "laplacian_gradient"
    name = "Laplacian Operator"
    category = "Edges & Gradients"
    description = "Tính đạo hàm bậc hai để phát hiện các vùng có sự thay đổi cường độ sáng đột ngột."
    doc_url = "https://docs.opencv.org/3.4.20/d5/d0f/tutorial_py_gradients.html"

    def get_parameter_schema(self) -> list[dict[str, Any]]:
        """Return kernel size."""
        return [
            {"name": "ksize", "label": "Cỡ Kernel", "type": "select", "default": 3, "options": [1, 3, 5, 7]},
        ]

    def process(self, image: np.ndarray, params: dict[str, Any]) -> tuple[np.ndarray, dict[str, Any]]:
        """Compute Laplacian edge detector."""
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) if len(image.shape) == 3 else image
        ksize = int(params.get("ksize", 3))
        lap = cv2.Laplacian(gray, cv2.CV_64F, ksize=ksize)
        abs_lap = np.uint8(np.absolute(lap))
        return abs_lap, {"ksize": ksize}
