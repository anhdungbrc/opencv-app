# Graph Report - opencv-app  (2026-11-17)

## Corpus Check
- 47 files · ~13,359 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 336 nodes · 576 edges · 24 communities (10 shown, 14 thin omitted)
- Extraction: 98% EXTRACTED · 2% INFERRED · 0% AMBIGUOUS · INFERRED: 14 edges (avg confidence: 0.87)
- Token cost: 1,200 input · 800 output

## Community Hubs (Navigation)
- Community 0 (abc)
- Community 1 (backend_app_processors_contours_contoursprocessor)
- Community 2 (backend_app_api_v1_endpoints_health)
- Community 3 (frontend_package_dependencies)
- Community 4 (backend_app_processors_smoothing_bilateralfilterprocessor)
- Community 5 (frontend_package)
- Community 6 (backend_app_processors_colorspace_bgr2grayprocessor_get_parameter_schema)
- Community 7 (backend_app_processors_thresholding_adaptivethresholdprocessor_get_parameter_schema)
- Community 8 (backend_tests_test_api)
- Community 9 (backend_app_processors_edges_cannyedgeprocessor_get_parameter_schema)
- Community 10 (coding_rules)
- Community 11 (backend_app_schemas_process)
- Community 12 (readme)
- Community 14 (backend_requirements_deps)
- Community 16 (agents_mandatory_rules)
- Community 20 (claude)
- Community 21 (claude_claude)
- Community 22 (claude_workflow_rules)
- Community 23 (pkg_opencv_web_backend)

## God Nodes (most connected - your core abstractions)
1. `BaseProcessor` - 32 edges
2. `encode_image_base64()` - 11 edges
3. `App()` - 11 edges
4. `decode_image_base64()` - 10 edges
5. `CannyEdgeProcessor` - 9 edges
6. `process_image()` - 8 edges
7. `BGR2GrayProcessor` - 8 edges
8. `ContoursProcessor` - 8 edges
9. `GeometricTransformProcessor` - 8 edges
10. `HistogramEqualizationProcessor` - 8 edges

## Surprising Connections (you probably didn't know these)
- `OpenCV Studio Overview & Documentation` --conceptually_related_to--> `Frontend HTML Application Shell`  [INFERRED]
  README.md → frontend/index.html
- `Frontend HTML Application Shell` --conceptually_related_to--> `Frontend Visual Assets & Branding`  [INFERRED]
  frontend/index.html → frontend/src/assets/hero.png
- `process_image()` --uses--> `ProcessRequest`  [INFERRED]
  backend/app/api/v1/endpoints/process.py → backend/app/schemas/process.py
- `OpenCV Studio Overview & Documentation` --references--> `Backend Python Dependencies`  [EXTRACTED]
  README.md → backend/requirements.txt
- `Root Requirements Pointer` --references--> `Backend Python Dependencies`  [EXTRACTED]
  requirements.txt → backend/requirements.txt

## Import Cycles
- None detected.

## Communities (24 total, 14 thin omitted)

### Community 0 - "Community 0 (abc)"
Cohesion: 0.07
Nodes (19): process_image(), BaseProcessor, decode_image_base64(), encode_image_base64(), BGR2GrayProcessor, ColorFilterInRangeProcessor, CannyEdgeProcessor, LaplacianProcessor (+11 more)

### Community 1 - "Community 1 (backend_app_processors_contours_contoursprocessor)"
Cohesion: 0.06
Nodes (9): ContoursProcessor, GeometricTransformProcessor, HistogramEqualizationProcessor, MorphologyProcessor, shape_image(), test_contours_processor(), test_geometric_transformations(), test_histogram_equalization() (+1 more)

### Community 2 - "Community 2 (backend_app_api_v1_endpoints_health)"
Cohesion: 0.07
Nodes (6): get_health(), get_operations(), Settings, root_index(), list_operations(), start_backend()

### Community 3 - "Community 3 (frontend_package_dependencies)"
Cohesion: 0.16
Nodes (19): dependencies, lucide-react@^1.16.0, react@^19.0.0, react-dom@^19.0.0, App(), init(), ControlPanel(), ImageWorkspace() (+11 more)

### Community 4 - "Community 4 (backend_app_processors_smoothing_bilateralfilterprocessor)"
Cohesion: 0.10
Nodes (4): BilateralFilterProcessor, synthetic_bgr_image(), test_bgr2gray_processor(), test_gaussian_blur_processor()

### Community 5 - "Community 5 (frontend_package)"
Cohesion: 0.14
Nodes (17): devDependencies, tailwindcss@^4.3.5, @tailwindcss/vite@^4.3.5, vite@^6.2.0, @vitejs/plugin-react@^5.1.0, name, private, scripts (+9 more)

### Community 8 - "Community 8 (backend_tests_test_api)"
Cohesion: 0.16
Nodes (5): client(), test_health_check_endpoint(), test_list_operations_endpoint(), test_process_image_endpoint(), test_process_invalid_operation()

### Community 10 - "Community 10 (coding_rules)"
Cohesion: 0.14
Nodes (12): Dấu hiệu cảnh báo: dừng và đọc lại luật, Luật 10. Giao tiếp trung thực, ngắn gọn, Luật 1. Nạp ngữ cảnh, hiểu yêu cầu, Luật 2. Plan mode và thiết kế trước khi xây, Luật 3. Đơn giản trước, Luật 4. Sửa phẫu thuật, Luật 5. Test trước, Luật 6. Bằng chứng trước khi tuyên bố (+4 more)

### Community 12 - "Community 12 (readme)"
Cohesion: 0.29
Nodes (6): 1. Cấu trúc Dự án (Architecture), 2. Hướng dẫn Khởi chạy (Quick Start), 3. Chạy Kiểm thử Tự động (Unit Tests), Bước 1: Khởi động Backend (FastAPI), Bước 2: Khởi động Frontend (React), OpenCV Studio - Computer Vision Interactive Web App

### Community 14 - "Community 14 (backend_requirements_deps)"
Cohesion: 0.40
Nodes (5): Backend Python Dependencies, Frontend Visual Assets & Branding, Frontend HTML Application Shell, OpenCV Studio Overview & Documentation, Root Requirements Pointer

## Knowledge Gaps
- **6 isolated node(s):** `opencv-web-backend`, `Coding Rules & Guidelines`, `Agents Mandatory Rules`, `Claude Graphify & Behavioral Rules`, `Root Requirements Pointer` (+1 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 162 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **14 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `BaseProcessor` connect `Community 0 (abc)` to `Community 1 (backend_app_processors_contours_contoursprocessor)`, `Community 4 (backend_app_processors_smoothing_bilateralfilterprocessor)`, `Community 13 (backend_app_processors_base_baseprocessor_get_parameter_schema)`, `Community 6 (backend_app_processors_colorspace_bgr2grayprocessor_get_parameter_schema)`?**
  _High betweenness centrality (0.109) - this node is a cross-community bridge._
- **Are the 2 inferred relationships involving `BaseProcessor` (e.g. with `get_processor()` and `register_processor()`) actually correct?**
  _`BaseProcessor` has 2 INFERRED edges - model-reasoned connections that need verification._
- **What connects `opencv-web-backend`, `Coding Rules & Guidelines`, `Agents Mandatory Rules` to the rest of the system?**
  _6 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `Community 0 (abc)` be split into smaller, more focused modules?**
  _Cohesion score 0.07287093942054433 - nodes in this community are weakly interconnected._
- **Why does `MorphologyProcessor` connect `Community 1 (backend_app_processors_contours_contoursprocessor)` to `Community 0 (abc)`?**
  _High betweenness centrality (0.034) - this node is a cross-community bridge._
- **Should `Community 1 (backend_app_processors_contours_contoursprocessor)` be split into smaller, more focused modules?**
  _Cohesion score 0.05893719806763285 - nodes in this community are weakly interconnected._
- **Why does `HistogramEqualizationProcessor` connect `Community 1 (backend_app_processors_contours_contoursprocessor)` to `Community 0 (abc)`?**
  _High betweenness centrality (0.034) - this node is a cross-community bridge._