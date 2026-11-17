# OpenCV Studio - Computer Vision Interactive Web App

Hệ thống web tương tác trực quan cho các thuật toán xử lý ảnh số của OpenCV theo tài liệu chuẩn [OpenCV Image Processing](https://docs.opencv.org/3.4.20/d2/d96/tutorial_py_table_of_contents_imgproc.html).

Kiến trúc chuẩn quốc tế: **React (Frontend)** + **FastAPI & OpenCV (Backend)**.

---

## 1. Cấu trúc Dự án (Architecture)

Dự án được tổ chức theo mô hình **Modular Monorepo** áp dụng triết lý **Clean Architecture**:

```text
opencv-app/
├── backend/                              # [BACKEND] Python FastAPI + OpenCV Engine
│   ├── app/
│   │   ├── api/v1/                       # REST API endpoints (health, operations, process)
│   │   ├── core/                         # Cấu hình CORS & Settings (config.py)
│   │   ├── processors/                   # 8 module thuật toán OpenCV thuần túy + Registry
│   │   │   ├── base.py                   # BaseProcessor abstract class & Tiện ích Base64
│   │   │   ├── colorspace.py             # BGR to Gray, HSV, Lọc màu inRange
│   │   │   ├── thresholding.py           # Simple, Adaptive, Otsu
│   │   │   ├── smoothing.py              # Gaussian, Median, Bilateral
│   │   │   ├── edges.py                  # Canny Edge, Sobel Gradient, Laplacian
│   │   │   ├── morphology.py             # Erode, Dilate, Open, Close, Gradient, Tophat
│   │   │   ├── contours.py               # findContours, Bounding Box, Diện tích
│   │   │   ├── histogram.py              # Histogram Equalization (CLAHE/Global)
│   │   │   ├── geometric.py              # Xoay, lật, thu phóng
│   │   │   └── registry.py               # Quản lý danh mục & schema tham số tự sinh UI
│   │   ├── schemas/                      # Pydantic Schemas (ProcessRequest, ProcessResponse)
│   │   └── main.py                       # FastAPI Application Factory & Lifespan
│   ├── tests/                            # 14 Unit & Integration Tests (Pytest - 100% Pass)
│   ├── Dockerfile                        # Dockerfile đóng gói backend Python 3.12 + OpenCV
│   ├── pyproject.toml                    # Cấu hình kiểm thử và gói Python
│   └── requirements.txt                  # Python dependencies cho backend
│
├── frontend/                             # [FRONTEND] React 19 + Vite + Tailwind CSS
│   ├── public/                           # Static assets & icons
│   ├── src/
│   │   ├── assets/                       # Ảnh minh họa (hero.png)
│   │   ├── components/                   # UI Components (Navbar, Sidebar, ControlPanel, ImageWorkspace)
│   │   ├── services/api.js               # API Client giao tiếp với FastAPI
│   │   ├── utils/sampleImages.js         # Bộ sinh ảnh mẫu Canvas không cần upload
│   │   ├── App.jsx                       # Điều phối trạng thái & tự động chạy có debounce
│   │   ├── index.css                     # Tailwind CSS styles
│   │   └── main.jsx                      # React mounting point
│   ├── Dockerfile                        # Multi-stage Dockerfile (Vite build -> Nginx Alpine)
│   ├── nginx.conf                        # Cấu hình Nginx reverse proxy /api/ & SPA routing
│   ├── index.html                        # HTML application shell
│   ├── package.json                      # Node dependencies & npm scripts
│   └── vite.config.js                    # Vite config + Proxy /api tới port 8000
│
├── data/                                 # Lưu trữ dữ liệu ảnh mẫu test cục bộ (.gitkeep)
├── docker-compose.yml                    # Điều phối chạy toàn bộ hệ thống bằng 1 lệnh Docker
├── .dockerignore                         # Loại trừ file rác khi build Docker images
├── start.ps1                             # Script 1-Click khởi động cả Backend và Frontend (PowerShell)
├── start.bat                             # Script 1-Click click đúp chuột trên Windows
├── main.py                               # Script khởi động nhanh backend từ thư mục gốc
├── README.md                             # Tài liệu hướng dẫn sử dụng & kiến trúc
├── requirements.txt                      # Alias trỏ về backend/requirements.txt
└── .gitignore                            # Quy tắc Git ignore toàn diện (Python & Node)
```

**Nguyên lý Thiết kế Cốt lõi:**
- **Tách biệt ranh giới (Clean Architecture):** Tầng thuật toán OpenCV (`backend/app/processors/`) chỉ xử lý ma trận `numpy.ndarray`, hoàn toàn độc lập với web framework (có thể tái sử dụng trực tiếp cho CLI, notebook hoặc script độc lập).
- **Giao diện sinh động (Metadata-driven UI):** Backend tự động cung cấp schema tham số qua `/api/v1/operations`, React Frontend tự động kết xuất các thanh trượt và điều khiển tương ứng mà không cần code cứng giao diện.
- **Tính độc lập phát triển:** Backend và Frontend có thể phát triển, kiểm thử và đóng gói triển khai độc lập.

---

## 2. Hướng dẫn Khởi chạy (Quick Start)

### Cách 1: Khởi động 1-Click (Khuyến nghị cho Lập trình hàng ngày)

Chỉ cần chạy file kịch bản tự động, hệ thống sẽ tự bật Backend, Frontend và mở trình duyệt:

- **Bằng PowerShell:**
  ```powershell
  .\start.ps1
  ```
- **Hoặc Click đúp chuột:** Chạy trực tiếp file `start.bat` trong Windows File Explorer.

👉 Trình duyệt sẽ tự động mở tại: **http://localhost:5173** (Backend API: `http://127.0.0.1:8000`).

---

### Cách 2: Chạy bằng Docker (Khuyến nghị cho Bàn giao & Triển khai)

Nếu máy tính đã cài đặt **Docker** & **Docker Compose**, bạn không cần cài Python hay Node:
```powershell
docker compose up --build
```
👉 Truy cập ứng dụng tại: **http://localhost:3000**, Backend Swagger Docs tại: `http://localhost:8000/docs`.

---

### Cách 3: Khởi chạy thủ công từng Terminal (Truyền thống)

**Terminal 1 (Backend FastAPI):**
```powershell
.\.venv\Scripts\activate
pip install -r backend/requirements.txt
python main.py
```

**Terminal 2 (Frontend React):**
```powershell
cd frontend
npm install
npm run dev
```
👉 Mở trình duyệt truy cập: **http://localhost:5173**

---

## 3. Chạy Kiểm thử Tự động (Unit Tests)

Toàn bộ 14 bài kiểm thử thuật toán xử lý ảnh và API endpoints:
```powershell
cd backend
..\.venv\Scripts\pytest -v
```
*(Tất cả 14 test đều đạt kết quả PASS).*

---

## 4. Bản đồ Kiến trúc & Đồ thị Tri thức (Knowledge Graph)

Dự án tích hợp sẵn công cụ **Graphify** để trực quan hóa toàn bộ mối quan hệ giữa các module, class, thuật toán OpenCV và API endpoints:
- **Xem biểu đồ tương tác:** Mở trực tiếp file [graphify-out/graph.html](file:///d:/AI/src/opencv-app/graphify-out/graph.html) trên trình duyệt (hoàn toàn chạy ở client-side, không cần dựng web server).
- **Đọc báo cáo cấu trúc:** Xem file [graphify-out/GRAPH_REPORT.md](file:///d:/AI/src/opencv-app/graphify-out/GRAPH_REPORT.md) để nắm danh sách "God Nodes", cộng đồng liên kết module (Community Hubs) và chỉ số gắn kết kiến trúc.
- **Cập nhật lại đồ thị:** Khi có thay đổi mã nguồn, chạy lệnh sau để cập nhật đồ thị AST:
  ```powershell
  graphify update .
  ```

