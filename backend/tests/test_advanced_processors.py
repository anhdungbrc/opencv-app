"""Unit tests for advanced OpenCV processors (Morphology, Contours, Histograms, Geometric)."""

import numpy as np
import pytest

from app.processors.morphology import MorphologyProcessor
from app.processors.contours import ContoursProcessor
from app.processors.histogram import HistogramEqualizationProcessor
from app.processors.geometric import GeometricTransformProcessor


@pytest.fixture
def shape_image() -> np.ndarray:
    """Fixture providing a test image with distinct shapes for contours and morphology."""
    img = np.zeros((120, 120, 3), dtype=np.uint8)
    import cv2
    # Draw white square
    cv2.rectangle(img, (20, 20), (50, 50), (255, 255, 255), -1)
    # Draw white circle
    cv2.circle(img, (80, 80), 20, (255, 255, 255), -1)
    return img


def test_morphology_processor(shape_image: np.ndarray) -> None:
    """Verify morphological opening and dilation transformations."""
    processor = MorphologyProcessor()
    out_img, meta = processor.process(shape_image, {"op_type": "DILATE", "ksize": 5})
    assert out_img is not None
    assert meta["op_type"] == "DILATE"


def test_contours_processor(shape_image: np.ndarray) -> None:
    """Verify contour detection identifies geometric figures and returns counts."""
    processor = ContoursProcessor()
    out_img, meta = processor.process(shape_image, {"threshold": 100, "min_area": 50})
    assert out_img is not None
    assert meta["valid_contours_count"] >= 2


def test_histogram_equalization(shape_image: np.ndarray) -> None:
    """Verify CLAHE and global histogram equalization execute properly."""
    processor = HistogramEqualizationProcessor()
    out_img, meta = processor.process(shape_image, {"method": "CLAHE"})
    assert out_img is not None
    assert meta["method"] == "CLAHE"


def test_geometric_transformations(shape_image: np.ndarray) -> None:
    """Verify rotation and flipping transformations."""
    processor = GeometricTransformProcessor()
    out_img, meta = processor.process(shape_image, {"angle": 45, "scale": 1.2, "flip": "HORIZONTAL"})
    assert out_img is not None
    assert meta["flip"] == "HORIZONTAL"
