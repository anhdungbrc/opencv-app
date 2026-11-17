"""Contour detection, feature extraction and geometric overlay processors."""

from typing import Any
import cv2
import numpy as np

from app.processors.base import BaseProcessor


class ContoursProcessor(BaseProcessor):
    """Detects contours and renders visual geometric overlays (outlines, bounding boxes)."""

    id = "contours_detection"
    name = "Contours Detection & Features"
    category = "Contours"
    description = "Tìm kiếm đường bao khép kín (cv2.findContours), tính diện tích, chu vi và vẽ khung bao chữ nhật/đa giác."
    doc_url = "https://docs.opencv.org/3.4.20/d4/d73/tutorial_py_contours_begin.html"

    def get_parameter_schema(self) -> list[dict[str, Any]]:
        """Return parameters for thresholding, min area filter, and bounding box toggle."""
        return [
            {"name": "threshold", "label": "Ngưỡng nhị phân tách vật thể", "type": "slider", "min": 10, "max": 250, "step": 5, "default": 127},
            {"name": "min_area", "label": "Lọc diện tích tối thiểu (px²)", "type": "slider", "min": 20, "max": 2000, "step": 20, "default": 100},
            {"name": "draw_bbox", "label": "Vẽ Bounding Box (Khung chữ nhật)", "type": "checkbox", "default": True},
            {"name": "draw_contours", "label": "Vẽ đường viền Contours", "type": "checkbox", "default": True},
        ]

    def process(self, image: np.ndarray, params: dict[str, Any]) -> tuple[np.ndarray, dict[str, Any]]:
        """Extract and visualize contours on top of the original image."""
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) if len(image.shape) == 3 else image
        thresh_val = int(params.get("threshold", 127))
        min_area = float(params.get("min_area", 100))
        draw_bbox = bool(params.get("draw_bbox", True))
        draw_contour = bool(params.get("draw_contours", True))

        # Binary thresholding before contour retrieval
        _, binary = cv2.threshold(gray, thresh_val, 255, cv2.THRESH_BINARY)
        contours, _ = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        # Create output canvas
        output = image.copy() if len(image.shape) == 3 else cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)

        valid_contours = []
        total_area = 0.0

        for cnt in contours:
            area = cv2.contourArea(cnt)
            if area >= min_area:
                valid_contours.append(cnt)
                total_area += area
                if draw_contour:
                    # Draw green contour line (thickness 2)
                    cv2.drawContours(output, [cnt], -1, (0, 255, 0), 2)
                if draw_bbox:
                    x, y, w, h = cv2.boundingRect(cnt)
                    # Draw blue rectangle (thickness 2)
                    cv2.rectangle(output, (x, y), (x + w, y + h), (255, 100, 0), 2)
                    # Label bounding box size
                    cv2.putText(
                        output,
                        f"{w}x{h}",
                        (x, max(15, y - 5)),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        0.4,
                        (255, 100, 0),
                        1,
                    )

        return output, {
            "total_contours_found": len(contours),
            "valid_contours_count": len(valid_contours),
            "total_area_px": round(total_area, 1),
        }
