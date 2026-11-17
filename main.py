"""Root entrypoint to launch the OpenCV Studio FastAPI backend server."""

import os
import sys
import uvicorn

# Ensure backend directory is in sys.path
backend_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "backend"))
if backend_path not in sys.path:
    sys.path.insert(0, backend_path)


def start_backend() -> None:
    """Start Uvicorn web server serving the OpenCV FastAPI application."""
    print("=" * 60)
    print("  🚀 OpenCV Studio - Computer Vision Interactive Web App")
    print("=" * 60)
    print("  - Backend API: http://127.0.0.1:8000")
    print("  - Swagger Docs: http://127.0.0.1:8000/docs")
    print("  - Frontend Dev: cd frontend && npm run dev (http://localhost:5173)")
    print("=" * 60)
    uvicorn.run("app.main:app", host="127.0.0.1", port=8000, reload=True, app_dir=backend_path)


if __name__ == "__main__":
    start_backend()
