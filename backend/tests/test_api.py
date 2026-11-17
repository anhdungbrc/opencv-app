"""Integration tests for FastAPI endpoints."""

from fastapi.testclient import TestClient
import numpy as np
import pytest

from app.main import app
from app.processors.base import encode_image_base64


@pytest.fixture
def client() -> TestClient:
    """Fixture providing an HTTP test client for the FastAPI app."""
    return TestClient(app)


@pytest.fixture
def sample_base64_image() -> str:
    """Fixture creating a simple synthetic image as base64 string."""
    img = np.zeros((80, 80, 3), dtype=np.uint8)
    img[20:60, 20:60] = (255, 255, 255)
    return encode_image_base64(img)


def test_health_check_endpoint(client: TestClient) -> None:
    """Verify that GET /api/v1/health returns status ok."""
    response = client.get("/api/v1/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "ok"


def test_list_operations_endpoint(client: TestClient) -> None:
    """Verify that GET /api/v1/operations returns available OpenCV operations."""
    response = client.get("/api/v1/operations")
    assert response.status_code == 200
    ops = response.json()
    assert isinstance(ops, list)
    assert len(ops) > 0
    assert any(op["id"] == "canny_edge" for op in ops)


def test_process_image_endpoint(client: TestClient, sample_base64_image: str) -> None:
    """Verify that POST /api/v1/process processes an image and returns base64 output."""
    payload = {
        "image_base64": sample_base64_image,
        "operation": "bgr_to_gray",
        "params": {},
    }
    response = client.post("/api/v1/process", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["success"] is True
    assert data["operation"] == "bgr_to_gray"
    assert "result_image_base64" in data
    assert len(data["result_image_base64"]) > 50


def test_process_invalid_operation(client: TestClient, sample_base64_image: str) -> None:
    """Verify that an unknown operation returns a proper 400 or 404 error response."""
    payload = {
        "image_base64": sample_base64_image,
        "operation": "non_existent_op",
        "params": {},
    }
    response = client.post("/api/v1/process", json=payload)
    assert response.status_code == 400
