"""Morphological image transformation processors (Erosion, Dilation, Opening, Closing, etc.)."""

from typing import Any
import cv2
import numpy as np

from app.processors.base import BaseProcessor


class MorphologyProcessor(BaseProcessor):
    """Applies mathematical morphology operations using a structural element kernel."""

    id = "morphology"
    name = "Morphological Operations"
    category = "Morphology"
    description = "Các phép toán hình thái học (Erode, Dilate, Open, Close, Gradient, Tophat, Blackhat) để làm sạch và bóc tách cấu trúc vật thể."
    doc_url = "https://docs.opencv.org/3.4.20/d9/d61/tutorial_py_morphological_ops.html"

    def get_parameter_schema(self) -> list[dict[str, Any]]:
        """Return operation type, kernel size, shape, and iterations."""
        return [
            {
                "name": "op_type",
                "label": "Phép toán",
                "type": "select",
                "default": "OPEN",
                "options": ["ERODE", "DILATE", "OPEN", "CLOSE", "GRADIENT", "TOPHAT", "BLACKHAT"],
            },
            {
                "name": "kernel_shape",
                "label": "Hình dạng Kernel",
                "type": "select",
                "default": "RECT",
                "options": ["RECT", "CROSS", "ELLIPSE"],
            },
            {"name": "ksize", "label": "Cỡ Kernel (Lẻ)", "type": "slider", "min": 3, "max": 25, "step": 2, "default": 5},
            {"name": "iterations", "label": "Số lần lặp (Iterations)", "type": "slider", "min": 1, "max": 10, "step": 1, "default": 1},
        ]

    def process(self, image: np.ndarray, params: dict[str, Any]) -> tuple[np.ndarray, dict[str, Any]]:
        """Execute morphological transformation."""
        op_type = str(params.get("op_type", "OPEN")).upper()
        k_shape_str = str(params.get("kernel_shape", "RECT")).upper()
        ksize = int(params.get("ksize", 5))
        if ksize % 2 == 0:
            ksize += 1
        iterations = int(params.get("iterations", 1))

        # Map kernel shape
        shape_map = {
            "RECT": cv2.MORPH_RECT,
            "CROSS": cv2.MORPH_CROSS,
            "ELLIPSE": cv2.MORPH_ELLIPSE,
        }
        shape = shape_map.get(k_shape_str, cv2.MORPH_RECT)
        kernel = cv2.getStructuringElement(shape, (ksize, ksize))

        if op_type == "ERODE":
            result = cv2.erode(image, kernel, iterations=iterations)
        elif op_type == "DILATE":
            result = cv2.dilate(image, kernel, iterations=iterations)
        else:
            op_map = {
                "OPEN": cv2.MORPH_OPEN,
                "CLOSE": cv2.MORPH_CLOSE,
                "GRADIENT": cv2.MORPH_GRADIENT,
                "TOPHAT": cv2.MORPH_TOPHAT,
                "BLACKHAT": cv2.MORPH_BLACKHAT,
            }
            morph_op = op_map.get(op_type, cv2.MORPH_OPEN)
            result = cv2.morphologyEx(image, morph_op, kernel, iterations=iterations)

        return result, {
            "op_type": op_type,
            "kernel_shape": k_shape_str,
            "ksize": ksize,
            "iterations": iterations,
        }
