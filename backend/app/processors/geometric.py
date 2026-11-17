"""Geometric transformation processors (Resize, Rotate, Flip)."""

from typing import Any
import cv2
import numpy as np

from app.processors.base import BaseProcessor


class GeometricTransformProcessor(BaseProcessor):
    """Applies scaling, flipping, and rotation transformations."""

    id = "geometric_transform"
    name = "Geometric Transformations"
    category = "Geometric"
    description = "Biến đổi hình học ảnh: Xoay tự do theo góc, Lật ngang/dọc (Flip), Thu phóng tỉ lệ."
    doc_url = "https://docs.opencv.org/3.4.20/da/d6e/tutorial_py_geometric_transformations.html"

    def get_parameter_schema(self) -> list[dict[str, Any]]:
        """Return parameters for angle, scale, and flip."""
        return [
            {"name": "angle", "label": "Góc xoay (Độ)", "type": "slider", "min": -180, "max": 180, "step": 5, "default": 0},
            {"name": "scale", "label": "Tỉ lệ thu phóng (Scale)", "type": "slider", "min": 0.2, "max": 2.0, "step": 0.1, "default": 1.0},
            {
                "name": "flip",
                "label": "Lật ảnh (Flip)",
                "type": "select",
                "default": "NONE",
                "options": ["NONE", "HORIZONTAL", "VERTICAL", "BOTH"],
            },
        ]

    def process(self, image: np.ndarray, params: dict[str, Any]) -> tuple[np.ndarray, dict[str, Any]]:
        """Execute geometric transformations."""
        h, w = image.shape[:2]
        angle = float(params.get("angle", 0))
        scale = float(params.get("scale", 1.0))
        flip_mode = str(params.get("flip", "NONE")).upper()

        result = image.copy()

        # 1. Flip
        if flip_mode == "HORIZONTAL":
            result = cv2.flip(result, 1)
        elif flip_mode == "VERTICAL":
            result = cv2.flip(result, 0)
        elif flip_mode == "BOTH":
            result = cv2.flip(result, -1)

        # 2. Rotation & Scaling
        if angle != 0 or scale != 1.0:
            center = (w // 2, h // 2)
            rot_mat = cv2.getRotationMatrix2D(center, angle, scale)
            result = cv2.warpAffine(result, rot_mat, (w, h), borderMode=cv2.BORDER_CONSTANT, borderValue=(0, 0, 0))

        return result, {"angle": angle, "scale": scale, "flip": flip_mode}
