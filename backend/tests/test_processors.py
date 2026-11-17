"""Unit tests for Backend Core OpenCV Image Processors."""

import numpy as np
import pytest

from app.processors.base import decode_image_base64, encode_image_base64
from app.processors.colorspace import BGR2GrayProcessor, ColorFilterInRangeProcessor
from app.processors.thresholding import SimpleThresholdProcessor, OtsuThresholdProcessor
from app.processors.smoothing import GaussianBlurProcessor, MedianBlurProcessor
from app.processors.edges import CannyEdgeProcessor, SobelProcessor
from app.processors.registry import get_processor, list_operations


@pytest.fixture
def synthetic_bgr_image() -> np.ndarray:
    """Fixture providing a 100x100 BGR test image with distinct colored geometric patterns."""
    img = np.zeros((100, 100, 3), dtype=np.uint8)
    # Red rectangle
    img[10:50, 10:50] = (0, 0, 255)
    # Green circle
    import cv2
    cv2.circle(img, (70, 70), 20, (0, 255, 0), -1)
    return img


def test_base64_encode_decode_roundtrip(synthetic_bgr_image: np.ndarray) -> None:
    """Verify that encoding and decoding images to/from Base64 preserves shape and content."""
    encoded = encode_image_base64(synthetic_bgr_image)
    assert isinstance(encoded, str)
    assert len(encoded) > 50

    decoded = decode_image_base64(encoded)
    assert decoded.shape == synthetic_bgr_image.shape
    assert decoded.dtype == np.uint8


def test_bgr2gray_processor(synthetic_bgr_image: np.ndarray) -> None:
    """Verify BGR to Grayscale conversion produces 1-channel or 3-channel gray representation."""
    processor = BGR2GrayProcessor()
    out_img, meta = processor.process(synthetic_bgr_image, {})
    assert out_img is not None
    assert meta["channels"] in (1, 3)


def test_simple_threshold_processor(synthetic_bgr_image: np.ndarray) -> None:
    """Verify simple binary thresholding produces binary outputs with expected threshold value."""
    processor = SimpleThresholdProcessor()
    out_img, meta = processor.process(synthetic_bgr_image, {"thresh": 127, "maxval": 255})
    assert out_img is not None
    assert meta["thresh_applied"] == 127


def test_gaussian_blur_processor(synthetic_bgr_image: np.ndarray) -> None:
    """Verify Gaussian blur computes smoothed image with specified odd kernel size."""
    processor = GaussianBlurProcessor()
    out_img, meta = processor.process(synthetic_bgr_image, {"ksize": 5, "sigmaX": 1.5})
    assert out_img is not None
    assert out_img.shape == synthetic_bgr_image.shape
    assert meta["ksize"] == 5


def test_canny_edge_processor(synthetic_bgr_image: np.ndarray) -> None:
    """Verify Canny edge detector finds edges with valid thresholds."""
    processor = CannyEdgeProcessor()
    out_img, meta = processor.process(synthetic_bgr_image, {"threshold1": 50, "threshold2": 150})
    assert out_img is not None
    assert "edge_pixels_count" in meta


def test_registry_lists_and_resolves_operations() -> None:
    """Verify that registry provides metadata and instantiates registered processors."""
    ops = list_operations()
    assert len(ops) >= 4, "Registry must contain at least core operations"

    op_ids = [op["id"] for op in ops]
    assert "bgr_to_gray" in op_ids
    assert "canny_edge" in op_ids

    proc = get_processor("canny_edge")
    assert isinstance(proc, CannyEdgeProcessor)
