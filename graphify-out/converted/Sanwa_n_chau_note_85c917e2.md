<!-- converted from Sanwa_n_chau_note.xlsx -->

## Sheet: Overview
|  |  | Danh sách các mục  tìm hiểu dự án Sanwa |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
|  | No | Mục lớn | Mục nhỏ | Nội dung | Ghi chú | Sheet |
|  | 1 | Document |  | Thư mục dự án |  | Document |
|  | 2 | Python |  | Tìm hiểu python |  | Python |
|  | 3 | DXF File |  | Tìm hiểu DXF file |  | DXF_File |
|  | 4 | OpenCV |  | OpenCV |  | OpenCV |
|  | 5 | Glossary |  | Các thuật ngữ trong dự án |  | Glossary |
|  | 6 | SteelDoor |  | Hình ảnh cửa thép SteelDoor |  | SteelDoor |
|  | 7 | BenchMark |  | Tesseract nhị phân |  | Tesseract |
|  | 8 | OCR |  | OCR |  | OCR |
|  | 9 |  |  |  |  |  |
|  | 10 |  |  |  |  |  |
|  | 11 |  |  |  |  |  |
|  | 12 |  |  |  |  |  |
|  | 13 |  |  |  |  |  |
|  | 14 |  |  |  |  |  |
|  | 15 |  |  |  |  |  |
|  | 16 |  |  |  |  |  |
|  | 17 |  |  |  |  |  |
|  | 18 |  |  |  |  |  |
|  | 19 |  |  |  |  |  |
|  | 20 |  |  |  |  |  |
|  | 21 |  |  |  |  |  |
|  | 22 |  |  |  |  |  |
|  | 23 |  |  |  |  |  |
|  | 24 |  |  |  |  |  |
|  | 25 |  |  |  |  |  |
|  | 26 |  |  |  |  |  |
## Sheet: Document
| <<Overview |  |  |
| --- | --- | --- |
|  | Thư mục dự án |  |
|  | Đường dẫn thư mục dự án |  |
|  |  | \\192.168.4.242\Share\Project\ブライセン\#02_OPEN_PROJECT\基幹宝飾・ForJewery |
|  | Link github |  |
|  | Link cài đặt |  |
|  |  | opencv-python · PyPI |
|  | Link tài liệu |  |
|  |  | OpenCV: Image Processing in OpenCV |
## Sheet: Python
| <<Overview |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | Tìm hiểu Python |  |  |  |  |  |  |  |  |  |  |  |
|  | Một số câu lệnh cơ bản trong python |  |  |  |  |  |  |  |  |  |  |  |
|  |  | #3. For loop |  |  |  |  |  |  |  |  |  |  |
|  |  |     drawings = ["drawing_01.pdf", "drawing_02.pdf"] |  |  |  |  |  |  |  |  |  |  |
|  |  |     for dwg in drawings: |  |  |  |  |  |  |  |  | for index, dwg in enumerate(drawings, start = 1): |  |
|  |  |         print(f"Đang xử lí: {dwg}") |  |  |  |  |  |  |  |  |         print(f"{index} : {dwg}") |  |
|  |  | Kết quả |  |  |  |  |  |  |  |  | Kết quả |  |
|  |  |  | PS ..\python-hello-world> python main.py |  |  |  |  |  |  |  |  | PS ..\python-hello-world> python main.py |
|  |  |  | Đang xử lí: drawing_01.pdf |  |  |  |  |  |  |  |  | 1 : drawing_01.pdf |
|  |  |  | Đang xử lí: drawing_02.pdf |  |  |  |  |  |  |  |  | 2 : drawing_02.pdf |
|  |  | Còn nếu sử dụng không có "f" thì không lấy ra giá trị, chỉ lấy text nguyên xi |  |  |  |  |  |  |  |  |  |  |
|  |  |         print("Đang xử lí: {dwg}") |  |  |  |  |  |  |  |  |  |  |
|  |  | Kết quả |  |  |  |  |  |  |  |  |  |  |
|  |  |  | ..\python-hello-world> python main.py |  |  |  |  |  |  |  |  |  |
|  |  |  | Đang xử lí: {dwg} |  |  |  |  |  |  |  |  |  |
|  |  |  | Đang xử lí: {dwg} |  |  |  |  |  |  |  |  |  |
|  |  |  #4. List |  |  |  |  |  |  |  |  |  |  |
|  |  |     lines = [100, 250, 400, 520] |  |  |  |  |  |  |  |  |  |  |
|  |  |     lines.append(610) |  |  |  |  |  |  |  |  |  |  |
|  |  |     print(lines[0]) |  |  | # lấy phần tử đầu tiên |  |  |  |  |  |  |  |
|  |  |     print(lines[-1]) |  |  | # lấy phần tử cuối cùng |  |  |  |  |  |  |  |
|  |  |     print(lines[1:3] |  |  | # lines[start, stop]: sẽ lấy từ phần tử start tới trước phần tử stop: tức là lấy phần tử số 1 và số 2, không lấy phần tử số 3--> kết quả là [250, 400] |  |  |  |  |  |  |  |
|  |  | Kết quả |  |  |  |  |  |  |  |  |  |  |
|  |  |  | ..\python-hello-world> python main.py |  |  |  |  |  |  |  |  |  |
|  |  |  | 100 |  |  |  |  |  |  |  |  |  |
|  |  |  | 610 |  |  |  |  |  |  |  |  |  |
|  |  |  | [250, 400] |  |  |  |  |  |  |  |  |  |
|  |  | #5. Dictionary |  |  |  |  |  |  |  |  |  |  |
|  |  |     drawing_info = { |  |  |  |  |  |  |  |  |  |  |
|  |  |         "id": "CAD-001", |  |  |  |  |  |  |  |  |  |  |
|  |  |         "name": "Bản vẽ tầng 1", |  |  |  |  |  |  |  |  |  |  |
|  |  |         "status": "pending", |  |  |  |  |  |  |  |  |  |  |
|  |  |         "dimensions": (1920, 1080) |  |  |  |  |  |  |  |  |  |  |
|  |  |     } |  |  |  |  |  |  |  |  |  |  |
|  |  |     print(drawing_info["id"], drawing_info["name"]) |  |  |  |  |  |  |  |  |  |  |
|  |  |     print(f"Detail: {drawing_info["id"]}, {drawing_info["name"]}") |  |  |  |  |  |  |  |  |  |  |
|  |  |     drawing_info["status"] = "completed" |  |  |  |  |  |  |  |  |  |  |
|  |  |     print(drawing_info["status"]) |  |  |  |  |  |  |  |  |  |  |
|  |  | Kết quả |  |  |  |  |  |  |  |  |  |  |
|  |  |  | ..\python-hello-world> python main.py |  |  |  |  |  |  |  |  |  |
|  |  |  | CAD-001 Bản vẽ tầng 1 |  |  |  |  |  |  |  |  |  |
|  |  |  | Detail: CAD-001, Bản vẽ tầng 1 |  |  |  |  |  |  |  |  |  |
|  |  |  | completed |  |  |  |  |  |  |  |  |  |
|  |  | #6. Tuple & Set |  |  |  |  |  |  |  |  |  |  |
|  |  |     point = (100, 200) |  |  |  |  |  |  |  |  |  |  |
|  |  |     print(point[0], point[1]) |  |  |  |  |  |  |  |  |  |  |
|  |  | Kết quả |  |  |  |  |  |  |  |  |  |  |
|  |  |  | ..\python-hello-world> python main.py |  |  |  |  |  |  |  |  |  |
|  |  |  | 100 200 |  |  |  |  |  |  |  |  |  |
|  |  |  #7. Function |  |  |  |  |  |  |  |  |  |  |
|  |  | def validate_file(filename: str, allowed_extensions: list) -> bool: |  |  |  |  |  |  |  |  |  |  |
|  |  |     """ Kiểm tra file có thuộc danh sách mở rộng cho phép hay không.""" |  |  |  |  |  |  |  |  |  |  |
|  |  |     ext = filename.split(".")[-1].lower() |  |  |  |  |  |  |  |  |  |  |
|  |  |     return ext in allowed_extensions |  |  |  |  |  |  |  |  |  |  |
|  |  | def main(): |  |  |  |  |  |  |  |  |  |  |
|  |  |     #7. Function |  |  |  |  |  |  |  |  |  |  |
|  |  |     is_valid = validate_file("drawing.pdf", ["csv", "xlsx"]) |  |  |  |  |  |  |  |  |  |  |
|  |  |     print(f"File valid: {is_valid}") |  |  |  |  |  |  |  |  |  |  |
|  |  | Kết quả |  |  |  |  |  |  |  |  |  |  |
|  |  |  | ..\python-hello-world> python main.py |  |  |  |  |  |  |  |  |  |
|  |  |  | File valid: False |  |  |  |  |  |  |  |  |  |
|  |  |  #8. PathLib |  |  |  |  |  |  |  |  |  |  |
|  |  | from pathlib import Path |  |  |  |  |  |  |  |  |  |  |
|  |  | def main(): |  |  |  |  |  |  |  |  |  |  |
|  |  |     #8. PathLib |  |  |  |  |  |  |  |  |  |  |
|  |  |     # Tạo object đường dẫn |  |  |  |  |  |  |  |  |  |  |
|  |  |     data_dir = Path("./drawings_data") |  |  |  |  |  |  |  |  |  |  |
|  |  |     # Tìm tất cả các file pdf |  |  |  |  |  |  |  |  |  |  |
|  |  |     pdf_files = list(data_dir.glob("*.pdf")) |  |  |  |  |  |  |  |  |  |  |
|  |  |     # Lấy danh sách tất cả file PDF trong thư mục |  |  |  |  |  |  |  |  |  |  |
|  |  |     for pdf in pdf_files: |  |  |  |  |  |  |  |  |  |  |
|  |  |         print(f"Tìm thấy file: {pdf.name} . Đường dẫn tuyệt đối: {pdf.resolve()}") |  |  |  |  |  |  |  |  |  |  |
|  |  | Kết quả |  |  |  |  |  |  |  |  |  |  |
|  |  |  | ..\python-hello-world> python main.py |  |  |  |  |  |  |  |  |  |
|  |  |  | Tìm thấy file: draw01.pdf . Đường dẫn tuyệt đối: C:\work\Projects\Sanwa\02.SourceCode\python-hello-world\drawings_data\draw01.pdf |  |  |  |  |  |  |  |  |  |
|  |  |  | Tìm thấy file: draw02.pdf . Đường dẫn tuyệt đối: C:\work\Projects\Sanwa\02.SourceCode\python-hello-world\drawings_data\draw02.pdf |  |  |  |  |  |  |  |  |  |
|  |  |  | Tìm thấy file: draw03.pdf . Đường dẫn tuyệt đối: C:\work\Projects\Sanwa\02.SourceCode\python-hello-world\drawings_data\draw03.pdf |  |  |  |  |  |  |  |  |  |
|  |  |  #9. json Ghi dữ liệu ra file JSON( trả về kết quả cho FE) |  |  |  |  |  |  |  |  |  |  |
|  |  | import json |  |  |  |  |  |  |  |  |  |  |
|  |  | def main(): |  |  |  |  |  |  |  |  |  |  |
|  |  |     #9. json Ghi dữ liệu ra file JSON( trả về kết quả cho FE) |  |  |  |  |  |  |  |  |  |  |
|  |  |     result = {"drawing":"A102", "contours_found": 15} |  |  |  |  |  |  |  |  |  |  |
|  |  |     with open("result.json", "w", encoding="utf-8") as f: |  |  |  |  |  |  |  |  |  |  |
|  |  |         json.dump(result, f, ensure_ascii=False, indent=4) |  |  |  |  |  |  |  |  |  |  |
|  |  |         print("Đã ghi kết quả ra file json") |  |  |  |  |  |  |  |  |  |  |
|  |  |      |  |  |  |  |  |  |  |  |  |  |
|  |  |     # Đọc file json |  |  |  |  |  |  |  |  |  |  |
|  |  |     with open("result.json", "r", encoding="utf-8") as f: |  |  |  |  |  |  |  |  |  |  |
|  |  |         data = json.load(f) |  |  |  |  |  |  |  |  |  |  |
|  |  |         print(f"Đã đọc file json: {data}") |  |  |  |  |  |  |  |  |  |  |
|  |  | Kết quả |  |  |  |  |  |  |  |  |  |  |
|  |  |  | ..\python-hello-world> python main.py |  |  |  |  |  |  |  |  |  |
|  |  |  | Đã ghi kết quả ra file json |  |  |  |  |  |  |  |  |  |
|  |  |  | Đã đọc file json: {'drawing': 'A102', 'contours_found': 15} |  |  |  |  |  |  |  |  |  |
|  |  | import numpy as np |  |  |  |  |  |  |  |  |  |  |
|  |  | def main(): |  |  |  |  |  |  |  |  |  |  |
|  |  |     #10. Numpy |  |  |  |  |  |  |  |  |  |  |
|  |  |     # Khởi tạo và thao tác với mảng Numpy |  |  |  |  |  |  |  |  |  |  |
|  |  |     # Tạo ảnh xám giả lập kích thướng 100x100 pixel(toàn màu đen = 0) |  |  |  |  |  |  |  |  |  |  |
|  |  |     dummy_image = np.zeros((100, 100), dtype=np.uint8) |  |  |  |  |  |  |  |  |  |  |
|  |  |     # Đổi vùng giữa(20:80, 20:80) thành màu trắng (255) |  |  |  |  |  |  |  |  |  |  |
|  |  |     dummy_image[20:80, 20:80] = 255 |  |  |  |  |  |  |  |  |  |  |
|  |  |     print(f"Hình dạng ảnh (Height, Width) : {dummy_image.shape}") |  |  |  |  |  |  |  |  |  |  |
|  |  |     print(f"Kiểu dữ liệu pixel : {dummy_image.dtype}") |  |  |  |  |  |  |  |  |  |  |
|  |  | Kết quả |  |  |  |  |  |  |  |  |  |  |
|  |  |  | ..\python-hello-world> python main.py |  |  |  |  |  |  |  |  |  |
|  |  |  | Hình dạng ảnh (Height, Width) : (100, 100) |  |  |  |  |  |  |  |  |  |
|  |  |  | Kiểu dữ liệu pixel : uint8 |  |  |  |  |  |  |  |  |  |
## Sheet: Glossary
| <<Overview |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  | Thuật ngữ dự án |  |  |  |  |  |  |
|  | 1. Thuật ngữ nghiệp vụ bản vẽ & sản phẩm |  |  |  |  |  |  |
|  |  | 1.1. Panel(Tấm ốp/ Wall Panel/ Siding Panel) |  |  |  |  |  |
|  |  |  | Là tấm vật liệu ngoại thất đúc sẵn dùng để ốp tường nhà hoặc các công trình xây dựng |  |  |  |  |
|  |  |  | Có dạng hình chữ nhật hoặc hình dạng đặc thù |  |  |  |  |
|  |  |  | Mặt ngoài có các đường hoạt tiết/vân sọc, mặt mép có cấu trúc ngàm âm dương nối các tấm lại với nhau |  |  |  |  |
|  |  |  | Mỗi tấm Panel có một mã quản lí riêng(70A, 70E) |  |  |  |  |
|  |  | 1.2 Kích thước(Dimensions & Tolerances) |  |  |  |  |  |
|  |  |  | Chiều rộng, chiều cao, chiều dào: kích thước phủ bì tổng thể của tấm Panel |  |  |  |  |
|  |  |  | Độ dày(Thickness): độ sâu/bề dày thực tế của tấm ốp |  |  |  |  |
|  |  |  | Chuỗi đường kích thước(Dimension Lines): các đường gióng chứa con số kèm mũi tên hoặc vạch gạch chéo thể hiện chiều dài từng phân đoạn trên bản vẽ |  |  |  |  |
|  |  |  | Dung sai(Tolerance): độ sai lệch khoảng cách cho phép giữa thực tế đo được trên bản vẽ và thông số đặt hàng trong Database |  |  |  |  |
|  |  |  |  | Ví dụ: nếu DB yêu cầu 1800mm và dung sao cho phép là ±10mm thì bản vẽ vẽ trong khoảng 1790mm đến 1810mm vẫn được tính là PASSSED(đúng) |  |  |  |
|  |  | 1.3 Số Lỗ và Vị trí Đột Lỗ(Holes &Hole Geometry) |  |  |  |  |  |
|  |  |  | Các lỗ tròn hoặc lỗ elip được khoét/đột sẵn trên tấm Panel phục vụ việc bắt vít, luồng ống dẫn, ngàm gài hoặc thi công lắp đặt tại công trường. |  |  |  |  |
|  |  |  | Số lượng lỗ(Hole count): Tổng số lỗ tròn khoét trên tấm Panel( ví dụ: 3 lỗ, 5 lỗ) |  |  |  |  |
|  |  |  | Đường kính lỗ(Hole Diameter/ DIA): Kích thước thực tế của lỗ( ví dụ ϕ 120mm) |  |  |  |  |
|  |  |  | Tọa độ tâm lỗ( Hole Coorinates X, Y): vị trí khoảng cách từ tâm lỗ đến mép trái/mép dưới của tấm Panel |  |  |  |  |
|  |  | 1.4. Góc L-Shape(L-shaped Corner/ L-notch/ Cấu trúc góc L) |  |  |  |  |  |
|  |  |  | Là dạng hình học của tấm Panel có góc bị vát hoặc khuyết một phần hình chữ L |  |  |  |  |
|  |  |  | Tấm panel cần khuyết góc L để ôm sát vào khung cột kết cấu, ô cửa sổ, dầm nhà hoặc vị trí giao nhau giữa các mảng tường góc |  |  |  |  |
|  |  |  | Panel tiêu chuẩn hình chữ nhật có 4 đỉnh(90∘) |  |  |  |  |
|  |  |  | Panel có góc L-Shape sẽ có 6 đỉnh hình học(do có 1 góc bị khoét vuông vào trong) |  |  |  |  |
|  | 2. Thuật ngữ định dạng File & Luồng dự án SANWA |  |  |  |  |  |  |
|  |  | 2.1. DBAccess |  |  |  |  |  |
|  |  |  | Là tập tin Database lưu trữ toàn bộ yêu cầu, thông số đặt hàng trực tiếp từ khách hàng hoặc nhân viên đi khảo sát công trình |  |  |  |  |
|  |  |  | Dữ liệu: bản lưu mã sản phẩm, chiều rộng, chiều cao, số lỗ tròn, có hay không có L-Shape, tọa độ các chi tiết đặc biệt |  |  |  |  |
|  |  | 2.2. Bản vẽ CAD(Computer - Aided Design/PDF/PNG/DWG) |  |  |  |  |  |
|  |  |  | Bản vẽ kĩ thuật do nhân viên thiết kế(Designers) dùng phần mềm CAD vẽ ra dựa trên dữ liệu yêu cầu từ DB Access |  |  |  |  |
|  |  | 2.3. Bản vẽ HPGL(Hewlett-Packard Graphics Language) |  |  |  |  |  |
|  |  |  | Tệp tin chứa tập hợp lệnh điều khiển máy cắt/máy gia công tự động tại xưởng sản xuất |  |  |  |  |
|  |  | 2.4. Khung tên(Title Block) & Khung lịch sử(Revision Block) |  |  |  |  |  |
|  |  |  | Khung tên(Title Block): Bảng nằm ở góc dưới bên phải bản vẽ, chứa thông tin mã bản vẽ(DWG NO), tên sản phẩm(TITLE), tỉ lệ(SCALE), ngày vẽ và người vẽ |  |  |  |  |
|  |  |  | Khung lịch sử(Revision Block): Bảng nằm ở mép trên bản vẽ, lưu lịch sử các lần chỉnh sửa bản vẽ(Revision Date, Person in charge, Content) |  |  |  |  |
|  | 3. Thuật ngữ Thuật Toán Xử lí ảnh(Open CV/ Computer Vision) |  |  |  |  |  |  |
|  |  | Thuật ngữ OpenCV |  |  |  |  | Khái niệm |
|  |  | Contour(Đường viền) |  |  |  |  | Tập hợp các điểm liên tục tạp thành ranh giới khép kín. Dùng để phát hiện khung Panel, lỗ tròn, hoặc khung tên. |
|  |  | Bounding Box(Khung bao chữ nhật) |  |  |  |  | Khung hình chữ nhật nhỏ nhất bao quanh đối tượng. Dùng để do chiều rộng W và chiều cao H của Panel |
|  |  | HoughLinesP(Phát hiện đường thẳng) |  |  |  |  | Thuật toán tìm các đoạn thẳng. Dùng để phát hiện đường gióng kích thước, đường biên Panel, hoặc trục lưới. |
|  |  | HoughCircles(Phát hiện đường tròn) |  |  |  |  | Thuật toán chuyên định vị các hình tròn. Dùng để đếm chính xác số lỗ tròn và đo bán kính lỗ |
|  |  | Thining/Skeletonization(làm mảnh nét) |  |  |  |  | Thuật toán Zhang-Suen biến các nét vẽ dày thành đường đơn 1-pixel để dễ tìm giao điểm và phân tích cấu trúc |
|  |  | Dilation & Erosion(Làm dày và Co nét) |  |  |  |  | Phép toán hình thái học(Morphology) giúp nối liền các đường nét bị đứt gãy hoặc xóa đốm nhiễu li ti |
|  |  | Thresholding(nhị phân hóa) |  |  |  |  | Biến ảnh màu xám thành ảnh đen trắng hoàn toàn để phân tách đường nét vẽ khỏi nền giấy |
|  | # Cẩm Nang Thuật Ngữ Đầy Đủ Dự Án SANWA (Cửa Thép SD & Xử Lý Bản Vẽ OpenCV) |  |  |  |  |  |  |
|  | Tài liệu này tổng hợp và giải thích toàn bộ thuật ngữ nghiệp vụ (Business Domain),  |  |  |  |  |  |  |
|  | định dạng dữ liệu và kỹ thuật xử lý ảnh (OpenCV) cốt lõi dành cho dự án **SANWA Shutter Corporation (三和シヤッター工業株式会社)**. |  |  |  |  |  |  |
|  | --- |  |  |  |  |  |  |
|  | ## 1. Tổng Quan Về Dự Án SANWA & Dòng Sản Phẩm Cửa Thép |  |  |  |  |  |  |
|  | ### 1.1. Tập đoàn Sanwa Shutter (三和シヤッター工業) |  |  |  |  |  |  |
|  | * Tập đoàn sản xuất vật liệu xây dựng và giải pháp kiến trúc hàng đầu Nhật Bản, |  |  |  |  |  |  |
|  |  chuyên biệt về các loại cửa công nghiệp, cửa nhà ở, cửa thép chống cháy và khung mặt tiền. |  |  |  |  |  |  |
|  | ### 1.2. Các Dòng Sản Phẩm Cốt Lõi Dự Án |  |  |  |  |  |  |
|  | * **SD (Steel Door - Cửa Thép):** Dòng cửa thép tiêu chuẩn dùng cho chung cư, tòa nhà văn phòng, nhà xưởng, phòng kỹ thuật. |  |  |  |  |  |  |
|  | * **1LSD (1-Leaf Steel Door - Cửa Thép Đơn):** Cửa thép 1 cánh (ví dụ các mã kiểm thử thực tế của Sanwa như `SD-1`, `1LSD-24`). |  |  |  |  |  |  |
|  | * **2LSD (2-Leaf Steel Door - Cửa Thép Đôi):** Cửa thép 2 cánh đi chung 1 khung. |  |  |  |  |  |  |
|  | * **Shutter (Cửa Cuốn):** Cửa cuốn nhà phố, cửa cuốn nhà xưởng trọng tải nặng, cửa cuốn chống bão/chống cháy. |  |  |  |  |  |  |
|  | * **Aluminum/Steel Fronts (Khung Mặt Tiền):** Hệ thống khung nhôm/thép kính cho các showroom và tòa nhà cao tầng. |  |  |  |  |  |  |
|  | --- |  |  |  |  |  |  |
|  | ## 2. Thuật Ngữ Nghiệp Vụ Cửa Thép (Steel Door Domain Terms) |  |  |  |  |  |  |
|  | ### 2.1. Cấu Trúc Tổng Thể Cửa Thép (Door Components) |  |  |  |  |  |  |
|  | * **Khung Cửa / Khung Ngoại (Outer Frame / Door Frame):** Bộ khung thép bao quanh cố định vào tường, đỡ cánh cửa. |  |  |  |  |  |  |
|  | * **Cánh Cửa / Tấm Panel (Door Leaf / Panel):** Phần cánh cửa chuyển động mở ra/đóng vào. |  |  |  |  |  |  |
|  | * **Độ Sâu Khung (Frame Depth - 枠見込み):** Độ dày/độ sâu nếp gấp phôi thép định hình của khung cửa (tính bằng mm). |  |  |  |  |  |  |
|  | ### 2.2. Chi Tiết Cơ Khí Trên Cửa Thép |  |  |  |  |  |  |
|  | * **Lỗ Khóa & Tay Nắm Gạt (Lock Hole & Lever Handle):** Vị trí lỗ dập/khoét tròn hoặc elip trên cánh và khung cửa để gắn bộ tay khóa, ổ khóa và tay nắm gạt. |  |  |  |  |  |  |
|  | * **Độ Cao Ổ Khóa (Lock Height / Lock Ht):** Khoảng cách từ tâm lỗ khóa xuống mặt sàn hoàn thiện (hoặc chân khung cửa). *Ví dụ:* Yêu cầu chuẩn thường là `1000.0 mm` hoặc `950.0 mm`. |  |  |  |  |  |  |
|  | * **Bản Lề (Hinges - 蝶番 / ヒンジ):** Các tấm linh kiện kim loại gia cường đính dọc theo mép thân khung cửa để đỡ cánh. *Ví dụ:* Bộ cửa SD tiêu chuẩn thường dùng **3 bản lề** hoặc **4 bản lề** tùy theo độ nặng của cánh. |  |  |  |  |  |  |
|  | * **Vết Cắt Khuyết L-Notch (L-Notch Cutout / Chân Khung L-Shape):** Vết dập/cắt khuyết góc chữ L ở hai chân dưới của khung cửa thép. |  |  |  |  |  |  |
|  |   * **Mục đích:** Để chân khung cửa ôm sập âm vào sàn bê tông hoặc nẹp chân tường khi lắp đặt tại công trình. |  |  |  |  |  |  |
|  | * **Đường Quét Mở Cửa (Door Swing Arc / 開き方向):** Nét vẽ vòng cung thể hiện bán kính quét và hướng mở cửa (mở vào trong - 内開き hoặc mở ra ngoài - 外開き). |  |  |  |  |  |  |
|  | ### 2.3. Kích Thước & Dung Sai Thi Công |  |  |  |  |  |  |
|  | * **Chiều Rộng Khung (Outer Width - W):** Kích thước phủ bì chiều rộng của bộ khung cửa (ví dụ: `900.0 mm`). |  |  |  |  |  |  |
|  | * **Chiều Cao Khung (Outer Height - H):** Kích thước phủ bì chiều cao của bộ khung cửa (ví dụ: `2100.0 mm`). |  |  |  |  |  |  |
|  | * **Dung Sai Thi Công (Tolerance - $\Delta$):** Sai số khoảng cách cho phép giữa con số đo từ OpenCV trên bản vẽ và con số yêu cầu trong DB Access (thường quy định dung sai cho phép $\le 10.0 \text{ mm}$). |  |  |  |  |  |  |
|  | --- |  |  |  |  |  |  |
|  | ## 3. Thuật Ngữ Định Dạng Dữ Liệu & Luồng Dự Án SANWA |  |  |  |  |  |  |
|  | ### 3.1. Nguồn Dữ Liệu Đầu Vào & Hệ Thống |  |  |  |  |  |  |
|  | * **DB Access (Microsoft Access Database `.accdb` / `.mdb`):** File dữ liệu đơn hàng do khách hàng Sanwa / nhân viên kinh doanh đi khảo sát công trình nhập vào (chứa thông số yêu cầu: Width, Height, Lock Height, L-Notch, Hinge count...). |  |  |  |  |  |  |
|  | * **MySQL Database:** Database trung tâm của hệ thống Web Backend (Python) dùng để lưu dữ liệu sau khi import file Access và lưu lịch sử kiểm thử. |  |  |  |  |  |  |
|  | * **Bản Vẽ CAD Cửa Thép (PDF / PNG / DWG):** Bản vẽ thiết kế kỹ thuật do nhân viên CAD triển khai dựa trên đơn hàng trong DB Access. |  |  |  |  |  |  |
|  | * **File Cắt CNC HPGL (`.hpgl`):** Tệp tin lệnh gia công dập/cắt phôi thép tự động chuyển xuống xưởng sản xuất. |  |  |  |  |  |  |
|  | ### 3.2. Quy Trình Kiểm Thử Tự Động (Auto-Verification Workflow) |  |  |  |  |  |  |
|  | * **Phase 1 (Verification DB Access $\leftrightarrow$ Bản Vẽ CAD):**  |  |  |  |  |  |  |
|  |   * Kiểm tra tự động xem bản vẽ CAD do nhân viên vẽ có **khớp 100% với đơn hàng trong DB Access** hay không (đo W, H, Lock Height, đếm số bản lề, kiểm tra vết cắt L-Notch chân khung). |  |  |  |  |  |  |
|  | * **Phase 2 (Verification Bản Vẽ CAD $\leftrightarrow$ File HPGL CNC):** |  |  |  |  |  |  |
|  |   * So khớp lớp nét vẽ giữa file thiết kế CAD và file cắt dập HPGL để phát hiện điểm chênh lệch trước khi đưa phôi thép vào máy gia công. |  |  |  |  |  |  |
|  | --- |  |  |  |  |  |  |
|  | ## 4. Thuật Ngữ Kỹ Thuật OpenCV Chuyên Dụng Cho Cửa Thép SANWA |  |  |  |  |  |  |
|  | | Thuật ngữ / Hàm OpenCV | Ý nghĩa & Ứng dụng cụ thể trong Dự án SANWA | |  |  |  |  |  |  |
|  | | :--- | :--- | |  |  |  |  |  |  |
|  | | **`cv2.inRange` (Color Masking / Lọc màu)** | Tách riêng nét vẽ **màu đen** của khung cửa/bản lề và loại bỏ hoàn toàn các **đường dóng kích thước màu xanh** cùng chữ viết nhiễu. | |  |  |  |  |  |  |
|  | | **`cv2.findContours` (Tìm đường viền)** | Quét bức ảnh nhị phân để trích xuất tập hợp các ranh giới đường viền khép kín của khung cửa, bản lề, vết cắt L-Notch. | |  |  |  |  |  |  |
|  | | **`cv2.boundingRect` (Khung bao chữ nhật)** | Vẽ khung chữ nhật tối thiểu bao ngoài contour để tính chiều rộng $W$, chiều cao $H$ pixel và quy đổi sang milimét ($1\text{px} = 2.5\text{mm}$). | |  |  |  |  |  |  |
|  | | **`cv2.HoughCircles` (Dò lỗ tròn ổ khóa)** | Thuật toán biến đổi Hough phát hiện đường tròn, dùng để **định vị tọa độ tâm ổ khóa $(cx, cy)$** và tính độ cao ổ khóa từ chân khung. | |  |  |  |  |  |  |
|  | | **Hinge Detection (Dò đếm bản lề)** | Quét khoanh vùng các nét khối chữ nhật nhỏ nằm dọc theo viền mép đứng của khung cửa để đếm tổng số bản lề thực tế. | |  |  |  |  |  |  |
|  | | **L-Notch Detection (Dò góc khuyết chân)** | Kiểm tra sự tồn tại của khối chữ nhật khuyết tại 2 góc chân dưới khung cửa để xác nhận có dập chân L-Notch hay không. | |  |  |  |  |  |  |
|  | | **`cv2.approxPolyDP` (Xấp xỉ đa giác)** | Đếm số lượng đỉnh của hình khối để phân biệt hình chữ nhật phẳng 4 đỉnh ($90^\circ$) với khối L-Shape 6-8 đỉnh. | |  |  |  |  |  |  |
|  | | **Verification Logic (So khớp & Kết luận)** | Đánh giá chênh lệch $\Delta = |\text{DB} - \text{OpenCV}|$. Xuất trạng thái **MATCH/MISMATCH** và kết luận **PASSED (Xanh)** / **FAILED (Đỏ)**. | |  |  |  |  |  |  |
|  | --- |  |  |  |  |  |  |
|  | *Tài liệu được cập nhật chuẩn hóa cho dòng sản phẩm Cửa Thép Sanwa SD-1 / 1LSD-24 (Phiên bản v2).* |  |  |  |  |  |  |
## Sheet: OpenCV
| <<Overview |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  | Tìm hiểu OpenCV |  |  |  |  |  |  |
|  | Một số câu lệnh cơ bản trong OpenCV |  |  |  |  |  |  |
|  | Chuyển sang ảnh xám (Grayscale) & Lọc nhiễu |  |  |  |  |  |  |
|  | Nhị phân hóa (Thresholding) |  |  |  |  |  |  |
|  | Làm dày nét, co nét, co trước dày sau, dày trước co sau |  |  |  |  |  |  |
|  | Làm mảnh nét |  |  |  |  |  |  |
|  | Tìm đường thẳng |  |  |  |  |  |  |
|  | Chuyển sang ảnh xám (Grayscale) & Lọc nhiễu |  |  |  |  |  |  |
|  |  | import numpy as np |  |  |  |  |  |
|  |  | import cv2 |  |  |  |  |  |
|  |  | def main(): |  |  |  |  |  |
|  |  |     # Đọc ảnh bản vẽ |  |  |  |  |  |
|  |  |     image_path = ('docs/sample_nozawa_drawing.png') |  |  |  |  |  |
|  |  |     image = cv2.imread(image_path) |  |  |  |  |  |
|  |  |     if image is None: |  |  |  |  |  |
|  |  |         print(f"Lỗi: không tìm thấy ảnh tại {image_path}") |  |  |  |  |  |
|  |  |         return |  |  |  |  |  |
|  |  |     # 1.Chuyển ảnh sang xám |  |  |  |  |  |
|  |  |     gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) |  |  |  |  |  |
|  |  |     # 2. Khử nhiễu bằng Gausian Blur |  |  |  |  |  |
|  |  |     blurred = cv2.GaussianBlur(gray, (3,3), 0) |  |  |  |  |  |
|  |  |     heavy_blurred = cv2.GaussianBlur(gray, (31, 31), 0) |  |  |  |  |  |
|  |  |     # Ghép 2 ảnh xám và ảnh làm mờ cạnh nhau để so sánh |  |  |  |  |  |
|  |  |     comparison = np.hstack([gray, blurred]) |  |  |  |  |  |
|  |  |     # Lưu ảnh ra thư mục dự án |  |  |  |  |  |
|  |  |     cv2.imwrite("output_gray.png", gray) |  |  |  |  |  |
|  |  |     cv2.imwrite("output_blurred.png", blurred) |  |  |  |  |  |
|  |  |     cv2.imwrite("output_heavy_blur.png", heavy_blurred) |  |  |  |  |  |
|  |  |     print("Đã lưu ảnh ra file gray và blurred, heavy_blurred") |  |  |  |  |  |
|  |  |     cv2.imwrite("output/comparison.png", comparison) |  |  |  |  |  |
|  |  |     print("Đã lưu ảnh ra thư mục output") |  |  |  |  |  |
|  |  |     # Hiển thị cửa sổ so sánh |  |  |  |  |  |
|  |  |     #cv2.imshow("So sánh: Trai(Gray) vs Phai(blurred)", comparison) |  |  |  |  |  |
|  |  |     cv2.imshow("Heavy blurred", heavy_blurred) |  |  |  |  |  |
|  |  |     # Chờ người dùng nhấn 1 phím bất kì để đóng cửa sổ |  |  |  |  |  |
|  |  |     cv2.waitKey(0) |  |  |  |  |  |
|  |  |     cv2.destroyAllWindows() |  |  |  |  |  |
|  |  | Kết quả |  |  |  |  |  |
|  | 2.2 Nhị phân hóa (Thresholding) |  |  |  |  |  |  |
|  |  | Ảnh xám(gray) sẽ có độ sáng trải dài từ 0(đen sì) tới 255(trắng tinh) với rất nhiều sắc độ xám ở giữa |  |  |  |  |  |
|  |  | Nhị phân hóa là thao tác đưa ảnh về đúng 2 màu duy nhất: Đen(0) hoặc Trắng(255) dựa vào một vạch phân cách gọi là Ngưỡng(Threshold) |  |  |  |  |  |
|  |  |  | Điểm ảnh nào sáng hơn ngưỡng--> thành Trắng |  |  |  |  |
|  |  |  | Điểm ảnh nào tối hơn ngưỡng--> thành Đen |  |  |  |  |
|  |  | Quy ước vàng trong OPENCV:  |  |  |  |  |  |
|  |  |  | Mọi thuật toán phân tích hình học, tìm đường bao viền(findContours), đếm vật thể trong OpenCV đều quy ước: |  |  |  |  |
|  |  |  |  | Nét vẽ/Chi tiết cần lấy phải là màu TRẮNG(255) |  |  |  |
|  |  |  |  | Nền giấy phải là màu ĐEN(0) |  |  |  |
|  |  |  | Trong khi đó, bản vẽ thực tế lại là nét đen trên nền giấy trắng. Đó là lý do trong cả 2 câu lệnh đều có cờ cv2.THRESH_BINARY_INV(INV= invert - đảo ngược biến nét đen thành trắng, nền trắng thành đen) |  |  |  |  |
|  |  | Dòng lệnh 1: Otsu Thresholding (Ngưỡng toàn cục tự động) |  |  |  |  |  |
|  |  | python | # Otsu Thresholding (Thích hợp cho bản vẽ nét rõ) |  |  |  |  |
|  |  | _, binary_otsu = cv2.threshold(blurred, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU) |  |  |  |  |  |
|  |  | Mục đích: Tìm một con số ngưỡng chuẩn duy nhất cho toàn bộ bức ảnh. Thuật toán Otsu sẽ tự động nhìn vào biểu đồ màu (histogram) của ảnh để tự quyết định ngưỡng tối ưu mà bạn không cần phải đoán mò (ví dụ nó tự chọn số 180). |  |  |  |  |  |
|  |  | Chi tiết tham số:  |  |  |  |  |  |
|  |  | blurred: Ảnh đầu vào (thường dùng ảnh đã làm mờ nhẹ để khử các hạt nhiễu nhỏ trước khi phân ngưỡng). |  |  |  |  |  |
|  |  | 0: Ngưỡng ban đầu (khi đã dùng Otsu thì giá trị này bị bỏ qua, điền tạm là 0). |  |  |  |  |  |
|  |  | 255: Giá trị tối đa (điểm ảnh được chọn sẽ gán thành 255 - màu trắng). |  |  |  |  |  |
|  |  | cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU:  |  |  |  |  |  |
|  |  | THRESH_OTSU: Yêu cầu máy tự tính ngưỡng. |  |  |  |  |  |
|  |  | THRESH_BINARY_INV: Đảo ngược (nét vẽ thành trắng, nền thành đen). |  |  |  |  |  |
|  |  | _: Giá trị trả về thứ nhất là con số ngưỡng mà Otsu tự tính được (thường dùng dấu gạch dưới _ để bỏ qua vì ta không cần quan tâm đến con số này). |  |  |  |  |  |
|  |  | binary_otsu: Ảnh nhị phân kết quả. |  |  |  |  |  |
|  |  | Dòng lệnh 2: Adaptive Thresholding (Ngưỡng thích ứng cục bộ) |  |  |  |  |  |
|  |  | python | # Adaptive Thresholding (Thích hợp cho bản vẽ scan mờ/lệch sáng) |  |  |  |  |
|  |  | binary_adaptive = cv2.adaptiveThreshold( |  |  |  |  |  |
|  |  |     gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 2 |  |  |  |  |  |
|  |  | ) |  |  |  |  |  |
|  |  | Vấn đề giải quyết: Nếu bản vẽ scan bị lệch sáng (ví dụ: góc trên bên trái sáng trưng, góc dưới bên phải bị bóng tối hoặc ố vàng), thì Otsu sẽ thất bại vì một ngưỡng chung không thể áp dụng cho cả vùng sáng lẫn vùng tối. |  |  |  |  |  |
|  |  | Cách Adaptive hoạt động: Nó chia nhỏ bức ảnh thành hàng nghìn ô vuông nhỏ, và tính ngưỡng riêng biệt cho từng ô một! |  |  |  |  |  |
|  |  | Chi tiết tham số:  |  |  |  |  |  |
|  |  | gray: Ảnh xám đầu vào. |  |  |  |  |  |
|  |  | 255: Giá trị tối đa (màu trắng). |  |  |  |  |  |
|  |  | cv2.ADAPTIVE_THRESH_GAUSSIAN_C: Công thức tính ngưỡng cục bộ dựa trên trọng số Gauss (điểm gần tâm ô vuông có tiếng nói lớn hơn). |  |  |  |  |  |
|  |  | cv2.THRESH_BINARY_INV: Đảo ngược nét thành trắng, nền thành đen. |  |  |  |  |  |
|  |  | 11 (Block Size): Kích thước của ô vuông cục bộ để tính ngưỡng (ở đây là 11×1111 \times 1111×11 pixel, bắt buộc phải là số lẻ: 11, 15, 21,...). |  |  |  |  |  |
|  |  | 2 (C): Hằng số trừ bớt đi từ giá trị trung bình tính được. Con số này giúp gạt bỏ những hạt nhiễu li ti ở nền giấy. |  |  |  |  |  |
|  |  | 3. So sánh: Khi nào nên dùng loại nào? |  |  |  |  |  |
|  |  | Tiêu chí | Otsu Thresholding | Adaptive Thresholding |  |  |  |
|  |  | Bản vẽ phù hợp | Bản vẽ chất lượng tốt, xuất từ CAD/PDF ra ảnh, ánh sáng đồng đều. | Bản vẽ scan bị ố vàng, bóng mờ, chụp bằng camera điện thoại bị lệch sáng. |  |  |  |
|  |  | Đặc điểm nét ra | Nét vẽ liền mạch, nền đen rất sạch sẽ không có hạt nhiễu. | Bắt được cả những nét rất mờ, nhưng nền giấy có thể bị xuất hiện lấm tấm hạt nhiễu nhỏ. |  |  |  |
|  |  | Otsu (phát âm: Ô-sư) là tên một thuật toán nhị phân hóa tự động kinh điển trong xử lý ảnh, được đề xuất vào năm 1979 bởi giáo sư người Nhật Nobuyuki Otsu (大津展之). |  |  |  |  |  |
|  |  | --- |  |  |  |  |  |
|  |  | ### 1. Vấn đề mà Otsu giải quyết là gì? |  |  |  |  |  |
|  |  | Thông thường, khi muốn biến ảnh xám thành ảnh đen-trắng (nhị phân), bạn phải **tự chọn thủ công một con số ngưỡng** (Threshold), ví dụ chọn số `127`: |  |  |  |  |  |
|  |  | - Điểm ảnh $< 127 \rightarrow$ Đen |  |  |  |  |  |
|  |  | - Điểm ảnh $\ge 127 \rightarrow$ Trắng |  |  |  |  |  |
|  |  | 👉 **Nhược điểm của cách thủ công:** Nếu ảnh chụp hơi tối hoặc hơi sáng, con số `127` sẽ sai ngay lập tức (ảnh có thể bị đen sì hoặc trắng xóa toàn bộ). Bạn sẽ phải ngồi thử đi thử lại bằng tay rất mất thời gian. |  |  |  |  |  |
|  |  | 👉 **Otsu sinh ra để giải quyết việc này:** Bạn không cần phải đoán mò con số nào cả, **thuật toán Otsu sẽ tự nhìn vào dữ liệu ảnh và tự tính ra con số ngưỡng tối ưu nhất**. |  |  |  |  |  |
|  |  | --- |  |  |  |  |  |
|  |  | ### 2. Thuật toán Otsu hoạt động như thế nào? |  |  |  |  |  |
|  |  | Hãy tưởng tượng trong bức ảnh bản vẽ của bạn có 2 thành phần chính: |  |  |  |  |  |
|  |  | 1. **Nét vẽ / Chữ viết** (tập hợp các điểm ảnh màu sẫm/tối). |  |  |  |  |  |
|  |  | 2. **Nền giấy** (tập hợp các điểm ảnh màu sáng). |  |  |  |  |  |
|  |  | Nếu vẽ biểu đồ phân bố độ sáng (Histogram) từ 0 đến 255, bức ảnh sẽ trông như **2 ngọn núi**: |  |  |  |  |  |
|  |  | ```text |  |  |  |  |  |
|  |  | Số lượng pixel |  |  |  |  |  |
|  |  |   ▲ |  |  |  |  |  |
|  |  |   │       /\ (Ngọn núi 1: Nét vẽ tối) |  |  |  |  |  |
|  |  |   │      /  \                 /\ (Ngọn núi 2: Nền giấy sáng) |  |  |  |  |  |
|  |  |   │     /    \               /  \ |  |  |  |  |  |
|  |  |   │____/______\_____\ /_____/____\_______► Độ sáng (0 - 255) |  |  |  |  |  |
|  |  |                      ▲ |  |  |  |  |  |
|  |  |                 Ngưỡng Otsu  |  |  |  |  |  |
|  |  |            (Tìm đáy thung lũng đẹp nhất) |  |  |  |  |  |
|  |  | ``` |  |  |  |  |  |
|  |  | Thuật toán Otsu sẽ duyệt qua các mức xám từ 0 đến 255 và tìm ra **vạch phân chia (ngưỡng T)** sao cho: |  |  |  |  |  |
|  |  | - Các điểm trong cùng nhóm (nét vẽ với nét vẽ, nền với nền) có màu sắc **đồng nhất nhất** (*tối thiểu hóa phương sai nội nhóm - Within-class variance*). |  |  |  |  |  |
|  |  | - Hai nhóm này **tách biệt nhau xa nhất có thể** (*tối đa hóa phương sai giữa 2 nhóm - Between-class variance*). |  |  |  |  |  |
|  |  | --- |  |  |  |  |  |
|  |  | ### 3. Ưu và nhược điểm của Otsu |  |  |  |  |  |
|  |  | * **Ưu điểm:** |  |  |  |  |  |
|  |  |   - **Tự động 100%**: Không cần người dùng cài đặt thông số cố định. |  |  |  |  |  |
|  |  |   - **Cực nhanh và nét**: Rất phù hợp với bản vẽ kỹ thuật CAD, tài liệu scan, hóa đơn... nơi mà nét vẽ và nền giấy tương phản rõ ràng. |  |  |  |  |  |
|  |  | * **Nhược điểm:** |  |  |  |  |  |
|  |  |   - Otsu tính **một ngưỡng duy nhất cho toàn bộ bức ảnh** (*Global Threshold*). Do đó, nếu ảnh bị **bóng đổ** (nửa bên trái sáng trưng, nửa bên phải tối mờ) thì Otsu sẽ bị sai lệch. *(Khi gặp ảnh bị lệch sáng thì ta mới cần dùng tới `Adaptive Threshold`)*. |  |  |  |  |  |
|  |  | --- |  |  |  |  |  |
|  |  | ### 4. Xem con số mà Otsu chọn cho bản vẽ của bạn |  |  |  |  |  |
|  |  | Trong code của bạn: |  |  |  |  |  |
|  |  | ```python |  |  |  |  |  |
|  |  | otsu_val, binary_otsu = cv2.threshold(blurred, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU) |  |  |  |  |  |
|  |  | print("Ngưỡng tối ưu mà thuật toán Otsu tự tính được là:", otsu_val) |  |  |  |  |  |
|  |  | ``` |  |  |  |  |  |
|  |  | Khi chạy dòng này trên ảnh bản vẽ `sample_nozawa_drawing.png`, OpenCV sẽ in ra một con số cụ thể (ví dụ: `185.0`). Con số này chính là ranh giới chuẩn xác nhất mà thuật toán Otsu đã tìm ra để phân tách nét vẽ và nền giấy. |  |  |  |  |  |
|  |  | # Nhị phân hóa bằng Otsu |  |  |  |  |  |
|  |  |     otsu_val, binary_otsu = cv2.threshold(blurred, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU) |  |  |  |  |  |
|  |  |     print(f"Ngưỡng Otsu : {otsu_val}") |  |  |  |  |  |
|  |  |     otsu_val_heavy, binary_otsu_heavy = cv2.threshold(heavy_blurred, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU) |  |  |  |  |  |
|  |  |     print(f"Ngưỡng Otsu Heavy: {otsu_val_heavy}") |  |  |  |  |  |
|  |  |     # Tạo cửa sổ hiển thị |  |  |  |  |  |
|  |  |     cv2.imshow("Binary Otsu", binary_otsu) |  |  |  |  |  |
|  |  |     cv2.imshow("Binary Otsu Heavy", binary_otsu_heavy) |  |  |  |  |  |
|  |  |     cv2.waitKey(0) |  |  |  |  |  |
|  |  |     cv2.destroyAllWindows() |  |  |  |  |  |
|  |  | Kết quả |  |  |  |  |  |
|  |  | # Nhị phân hóa bằng Adaptive |  |  |  |  |  |
|  |  |     binary_adaptive = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,  |  |  |  |  |  |
|  |  |                                             cv2.THRESH_BINARY_INV, 11, 2) |  |  |  |  |  |
|  |  |     cv2.imshow("Binary Adaptive", binary_adaptive) |  |  |  |  |  |
|  |  |     cv2.waitKey(0) |  |  |  |  |  |
|  |  |     cv2.destroyAllWindows() |  |  |  |  |  |
|  |  | Kết quả |  |  |  |  |  |
|  | Làm dày nét |  |  |  |  |  |  |
|  |  | # Phép Toán Hình Thái Học (Morphological Operations) |  |  |  |  |  |
|  |  | Đây là nhóm phép toán xử lý **hình dạng** của các đối tượng trong ảnh nhị phân (trắng/đen). Hãy tưởng tượng bạn đang làm việc với ảnh chữ viết tay hoặc bản vẽ kỹ thuật. |  |  |  |  |  |
|  |  | --- |  |  |  |  |  |
|  |  | ## 🧱 Kernel (Nhân) — "Cục tẩy / Cây bút" |  |  |  |  |  |
|  |  | ```python |  |  |  |  |  |
|  |  | kernel = np.ones((3, 3), np.uint8) |  |  |  |  |  |
|  |  | ``` |  |  |  |  |  |
|  |  | Kernel là một **ma trận nhỏ 3×3** toàn số 1, đóng vai trò như một "công cụ" trượt qua từng pixel của ảnh: |  |  |  |  |  |
|  |  | ``` |  |  |  |  |  |
|  |  | ┌───┬───┬───┐ |  |  |  |  |  |
|  |  | │ 1 │ 1 │ 1 │ |  |  |  |  |  |
|  |  | ├───┼───┼───┤ |  |  |  |  |  |
|  |  | │ 1 │ 1 │ 1 │ |  |  |  |  |  |
|  |  | ├───┼───┼───┤ |  |  |  |  |  |
|  |  | │ 1 │ 1 │ 1 │ |  |  |  |  |  |
|  |  | └───┴───┴───┘ |  |  |  |  |  |
|  |  | ``` |  |  |  |  |  |
|  |  | - **Kernel lớn hơn** (5×5, 7×7) → hiệu ứng mạnh hơn |  |  |  |  |  |
|  |  | - **Kernel nhỏ hơn** (3×3) → hiệu ứng nhẹ, tinh tế hơn |  |  |  |  |  |
|  |  | --- |  |  |  |  |  |
|  |  | ## 1️⃣ Dilation — Làm Dày Nét (Phép giãn nở) |  |  |  |  |  |
|  |  | ```python |  |  |  |  |  |
|  |  | dilated = cv2.dilate(binary_otsu, kernel, iterations=1) |  |  |  |  |  |
|  |  | ``` |  |  |  |  |  |
|  |  | **Nguyên lý:** Trượt kernel qua ảnh. Nếu **BẤT KỲ pixel nào** trong vùng kernel là trắng (255) → pixel trung tâm **trở thành trắng**. |  |  |  |  |  |
|  |  | ``` |  |  |  |  |  |
|  |  | Trước (nét mảnh, đứt)          Sau Dilation (nét dày, nối lại) |  |  |  |  |  |
|  |  |                                  |  |  |  |  |  |
|  |  |   ·  ·  ·  ·  ·  ·               ·  ·  ·  ·  ·  · |  |  |  |  |  |
|  |  |   ·  ·  █  ·  ·  ·               ·  █  █  █  ·  · |  |  |  |  |  |
|  |  |   ·  ·  █  ·  ·  ·      →        ·  █  █  █  ·  · |  |  |  |  |  |
|  |  |   ·  ·  ·  ·  ·  ·               ·  █  █  █  ·  · |  |  |  |  |  |
|  |  |   ·  ·  ·  █  ·  ·               ·  ·  █  █  █  · |  |  |  |  |  |
|  |  |   ·  ·  ·  ·  ·  ·               ·  ·  █  █  █  · |  |  |  |  |  |
|  |  | ``` |  |  |  |  |  |
|  |  | **Tác dụng:** |  |  |  |  |  |
|  |  | - ✅ Hàn gắn nét bị đứt |  |  |  |  |  |
|  |  | - ✅ Nối liền khoảng trống nhỏ giữa các nét |  |  |  |  |  |
|  |  | - ✅ Làm chữ/đường nét đậm hơn |  |  |  |  |  |
|  |  | - ⚠️ Nhược điểm: nhiễu nhỏ cũng bị phình to ra |  |  |  |  |  |
|  |  | **Ứng dụng thực tế:** Chữ viết tay mờ, nét quá mảnh → dilation giúp nét rõ ràng hơn. |  |  |  |  |  |
|  |  | --- |  |  |  |  |  |
|  |  | ## 2️⃣ Erosion — Làm Co Nét (Phép xói mòn) |  |  |  |  |  |
|  |  | ```python |  |  |  |  |  |
|  |  | eroded = cv2.erode(binary_otsu, kernel, iterations=1) |  |  |  |  |  |
|  |  | ``` |  |  |  |  |  |
|  |  | **Nguyên lý:** Trượt kernel qua ảnh. Chỉ khi **TẤT CẢ pixel** trong vùng kernel đều là trắng → pixel trung tâm **mới giữ nguyên trắng**. Ngược lại → **chuyển thành đen**. |  |  |  |  |  |
|  |  | ``` |  |  |  |  |  |
|  |  | Trước (có nhiễu đốm)           Sau Erosion (sạch nhiễu) |  |  |  |  |  |
|  |  |   ·  ·  ·  ·  █  ·               ·  ·  ·  ·  ·  ·    ← đốm nhiễu biến mất |  |  |  |  |  |
|  |  |   ·  █  █  █  ·  ·               ·  ·  █  ·  ·  · |  |  |  |  |  |
|  |  |   ·  █  █  █  ·  ·      →        ·  ·  █  ·  ·  ·    ← nét bị co lại |  |  |  |  |  |
|  |  |   ·  █  █  █  ·  ·               ·  ·  █  ·  ·  · |  |  |  |  |  |
|  |  |   ·  ·  ·  ·  ·  ·               ·  ·  ·  ·  ·  · |  |  |  |  |  |
|  |  | ``` |  |  |  |  |  |
|  |  | **Tác dụng:** |  |  |  |  |  |
|  |  | - ✅ Tẩy sạch các đốm nhiễu li ti (vì đốm nhỏ bị xóa hoàn toàn) |  |  |  |  |  |
|  |  | - ✅ Tách rời các đối tượng dính nhau |  |  |  |  |  |
|  |  | - ⚠️ Nhược điểm: nét chính cũng bị mỏng đi |  |  |  |  |  |
|  |  | **Ứng dụng thực tế:** Ảnh scan có bụi bẩn, đốm mực → erosion xóa sạch. |  |  |  |  |  |
|  |  | --- |  |  |  |  |  |
|  |  | ## 3️⃣ Opening — Co trước, Dày sau |  |  |  |  |  |
|  |  | ```python |  |  |  |  |  |
|  |  | opened = cv2.morphologyEx(binary_otsu, cv2.MORPH_OPEN, kernel) |  |  |  |  |  |
|  |  | # Tương đương với: |  |  |  |  |  |
|  |  | # temp = cv2.erode(binary_otsu, kernel)   # Bước 1: Co |  |  |  |  |  |
|  |  | # opened = cv2.dilate(temp, kernel)       # Bước 2: Dày |  |  |  |  |  |
|  |  | ``` |  |  |  |  |  |
|  |  | **Nguyên lý:** `Erosion → Dilation` (hai bước liên tiếp) |  |  |  |  |  |
|  |  | ``` |  |  |  |  |  |
|  |  |    Ảnh gốc              Sau Erosion            Sau Dilation |  |  |  |  |  |
|  |  |  (có nhiễu đốm)       (co: xóa nhiễu,        (dày: khôi phục |  |  |  |  |  |
|  |  |                         nét cũng co)           nét về gần gốc) |  |  |  |  |  |
|  |  |   █  ·  ·  ·  ·        ·  ·  ·  ·  ·         ·  ·  ·  ·  · |  |  |  |  |  |
|  |  |   ·  ·  ·  ·  ·   →    ·  ·  ·  ·  ·    →    ·  ·  ·  ·  · |  |  |  |  |  |
|  |  |   ·  █  █  █  ·        ·  ·  █  ·  ·         ·  █  █  █  · |  |  |  |  |  |
|  |  |   ·  █  █  █  ·        ·  ·  █  ·  ·         ·  █  █  █  · |  |  |  |  |  |
|  |  |   ·  █  █  █  ·        ·  ·  █  ·  ·         ·  █  █  █  · |  |  |  |  |  |
|  |  |   ·  ·  ·  ·  ·        ·  ·  ·  ·  ·         ·  ·  ·  ·  · |  |  |  |  |  |
|  |  |    |  |  |  |  |  |
|  |  |   ↑ đốm nhiễu          ↑ nhiễu biến mất       ↑ nét phục hồi |  |  |  |  |  |
|  |  |     ở góc trái                                   nhiễu vẫn mất! |  |  |  |  |  |
|  |  | ``` |  |  |  |  |  |
|  |  | **Tác dụng:** |  |  |  |  |  |
|  |  | - ✅ **Loại bỏ nhiễu đốm nhỏ** mà vẫn giữ nguyên kích thước nét chính |  |  |  |  |  |
|  |  | #NAME? |  |  |  |  |  |
|  |  | **Ứng dụng thực tế:** Bản vẽ kỹ thuật scan bị bẩn → Opening làm sạch nền mà không ảnh hưởng đường nét. |  |  |  |  |  |
|  |  | --- |  |  |  |  |  |
|  |  | ## 4️⃣ Closing — Dày trước, Co sau |  |  |  |  |  |
|  |  | ```python |  |  |  |  |  |
|  |  | closed = cv2.morphologyEx(binary_otsu, cv2.MORPH_CLOSE, kernel) |  |  |  |  |  |
|  |  | # Tương đương với: |  |  |  |  |  |
|  |  | # temp = cv2.dilate(binary_otsu, kernel)  # Bước 1: Dày |  |  |  |  |  |
|  |  | # closed = cv2.erode(temp, kernel)        # Bước 2: Co |  |  |  |  |  |
|  |  | ``` |  |  |  |  |  |
|  |  | **Nguyên lý:** `Dilation → Erosion` (ngược lại với Opening) |  |  |  |  |  |
|  |  | ``` |  |  |  |  |  |
|  |  |    Ảnh gốc              Sau Dilation           Sau Erosion |  |  |  |  |  |
|  |  |  (nét bị đứt gãy)     (dày: nối khoảng       (co: thu nét về |  |  |  |  |  |
|  |  |                         trống, nét phình)      kích thước gốc) |  |  |  |  |  |
|  |  |   ·  ·  ·  ·  ·        ·  ·  ·  ·  ·         ·  ·  ·  ·  · |  |  |  |  |  |
|  |  |   ·  █  █  ·  ·   →    █  █  █  █  ·    →    ·  █  █  ·  · |  |  |  |  |  |
|  |  |   ·  ·  ·  ·  ·        █  █  █  █  █         ·  █  █  █  ·  ← được nối! |  |  |  |  |  |
|  |  |   ·  ·  █  █  ·        ·  █  █  █  █         ·  ·  █  █  · |  |  |  |  |  |
|  |  |   ·  ·  ·  ·  ·        ·  █  █  █  █         ·  ·  ·  ·  · |  |  |  |  |  |
|  |  |   ↑ khoảng trống        ↑ khoảng trống         ↑ nét nối liền |  |  |  |  |  |
|  |  |     giữa 2 nét            được lấp đầy           kích thước gốc |  |  |  |  |  |
|  |  | ``` |  |  |  |  |  |
|  |  | **Tác dụng:** |  |  |  |  |  |
|  |  | - ✅ **Nối các đứt gãy nhỏ** trên đường nét mà vẫn giữ kích thước nét |  |  |  |  |  |
|  |  | #NAME? |  |  |  |  |  |
|  |  | **Ứng dụng thực tế:** Ảnh chữ viết tay bị đứt nét do mực nhạt → Closing hàn lại. |  |  |  |  |  |
|  |  | --- |  |  |  |  |  |
|  |  | ## 📊 Bảng So Sánh Tổng Hợp |  |  |  |  |  |
|  |  | | Phép toán | Công thức | Mục đích chính | Khi nào dùng? | |  |  |  |  |  |
|  |  | |-----------|-----------|----------------|---------------| |  |  |  |  |  |
|  |  | | **Dilation** | Giãn nở | Làm dày nét | Nét quá mảnh, bị đứt | |  |  |  |  |  |
|  |  | | **Erosion** | Xói mòn | Làm co nét | Nhiều nhiễu đốm, nét quá dày | |  |  |  |  |  |
|  |  | | **Opening** | Erosion → Dilation | Xóa nhiễu nhỏ | Nền bẩn, có đốm li ti | |  |  |  |  |  |
|  |  | | **Closing** | Dilation → Erosion | Nối đứt gãy | Nét bị đứt, có lỗ nhỏ | |  |  |  |  |  |
|  |  | --- |  |  |  |  |  |
|  |  | ## 💡 Mẹo về `iterations` |  |  |  |  |  |
|  |  | ```python |  |  |  |  |  |
|  |  | # iterations = số lần lặp lại phép toán |  |  |  |  |  |
|  |  | dilated_1 = cv2.dilate(img, kernel, iterations=1)  # Dày nhẹ |  |  |  |  |  |
|  |  | dilated_3 = cv2.dilate(img, kernel, iterations=3)  # Dày gấp 3 lần |  |  |  |  |  |
|  |  | ``` |  |  |  |  |  |
|  |  | - `iterations=1`: hiệu ứng nhẹ, phù hợp đa số trường hợp |  |  |  |  |  |
|  |  | - Tăng `iterations` = hiệu ứng mạnh hơn (tương đương dùng kernel lớn hơn) |  |  |  |  |  |
|  |  | > **Quy tắc vàng:** Luôn bắt đầu với `iterations=1` và kernel 3×3, rồi tăng dần nếu chưa đạt kết quả mong muốn. |  |  |  |  |  |
|  |  | def main(): |  |  |  |  |  |
|  |  |     # Phép toán hình thái học(morphology) |  |  |  |  |  |
|  |  |     kernel = np.ones((3,3), np.uint8) |  |  |  |  |  |
|  |  |     # Đọc ảnh bản vẽ |  |  |  |  |  |
|  |  |     image_path = ('docs/sample_nozawa_drawing.png') |  |  |  |  |  |
|  |  |     image = cv2.imread(image_path) |  |  |  |  |  |
|  |  |     # 1.Chuyển ảnh sang xám |  |  |  |  |  |
|  |  |     gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) |  |  |  |  |  |
|  |  |     # 2. Khử nhiễu bằng Gausian Blur |  |  |  |  |  |
|  |  |     blurred = cv2.GaussianBlur(gray, (15,15), 0) |  |  |  |  |  |
|  |  |     # Nhị phân hóa bằng Otsu |  |  |  |  |  |
|  |  |     otsu_val, binary_otsu = cv2.threshold(blurred, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU) |  |  |  |  |  |
|  |  |     print(f"Ngưỡng Otsu : {otsu_val}") |  |  |  |  |  |
|  |  |     # Dilated - Làm dày nét |  |  |  |  |  |
|  |  |     dilated = cv2.dilate(binary_otsu, kernel, iterations=1) |  |  |  |  |  |
|  |  |     # Erosion - Làm co nét |  |  |  |  |  |
|  |  |     eroded = cv2.erode(binary_otsu, kernel, iterations=1) |  |  |  |  |  |
|  |  |     # Opening - Co trước, dày sau(xóa nhiễu đốm) |  |  |  |  |  |
|  |  |     opened = cv2.morphologyEx(binary_otsu, cv2.MORPH_OPEN, kernel) |  |  |  |  |  |
|  |  |     # Closing - Dày trước, co sau(nối đứt gãy) |  |  |  |  |  |
|  |  |     closed = cv2.morphologyEx(binary_otsu, cv2.MORPH_CLOSE, kernel) |  |  |  |  |  |
|  |  |     # Thu nhỏ & hiển thị để so sánh |  |  |  |  |  |
|  |  |     scale = 0.5 |  |  |  |  |  |
|  |  |     cv2.imshow("Dilated", cv2.resize(dilated, (0, 0), fx=scale, fy=scale)) |  |  |  |  |  |
|  |  |     cv2.imshow("Eroded", cv2.resize(eroded, (0, 0), fx=scale, fy=scale)) |  |  |  |  |  |
|  |  |     cv2.imshow("Opened", cv2.resize(opened, (0, 0), fx=scale, fy=scale)) |  |  |  |  |  |
|  |  |     cv2.imshow("Closed", cv2.resize(closed, (0, 0), fx=scale, fy=scale)) |  |  |  |  |  |
|  |  |     cv2.waitKey(0) |  |  |  |  |  |
|  |  |     cv2.destroyAllWindows() |  |  |  |  |  |
|  |  | So sánh Dilation vs Gốc → để ý nét chữ/đường kẻ dày hơn |  |  |  |  |  |
|  |  | So sánh Erosion vs Gốc → để ý đốm nhỏ biến mất, nét mỏng đi |  |  |  |  |  |
|  |  | So sánh Opening vs Gốc → nhiễu đốm mất nhưng nét gần như giữ nguyên |  |  |  |  |  |
|  |  | So sánh Closing vs Gốc → chỗ nét đứt được nối lại |  |  |  |  |  |
|  | So ánh Eroded(Co nét) vs Thinning(làm mảnh nét) |  |  |  |  |  |  |
|  |  | Nét gốc (dày 5px):      █████ |  |  |  |  |  |
|  |  | Sau Erosion:             ███       ← co đều từ 2 phía, vẫn dày ~3px |  |  |  |  |  |
|  |  | Sau Thinning:            █         ← thu về đúng 1px, giữ hình dạng |  |  |  |  |  |
|  | Erosion — Làm co nét |  |  |  |  |  |  |
|  | Cơ chế: Cào đều tất cả các cạnh vào trong theo kích thước kernel |  |  |  |  |  |  |
|  | Kết quả: Nét mỏng hơn nhưng không đảm bảo về số pixel dày |  |  |  |  |  |  |
|  | Phụ thuộc vào: Kích thước kernel + số iterations |  |  |  |  |  |  |
|  | Nét dày 10px + kernel 3×3 → còn ~8px |  |  |  |  |  |  |
|  | Tốc độ: Rất nhanh ⚡ |  |  |  |  |  |  |
|  | Thinning (Zhang-Suen) — Làm mảnh nét |  |  |  |  |  |  |
|  | Cơ chế: Thuật toán thông minh, lặp đi lặp lại tỉa pixel từng cạnh cho đến khi nét chỉ còn đúng 1 pixel |  |  |  |  |  |  |
|  | Kết quả: Nét luôn luôn là 1 pixel dù ban đầu dày bao nhiêu |  |  |  |  |  |  |
|  | Phụ thuộc vào: Không cần kernel, tự xử lý đến cùng |  |  |  |  |  |  |
|  | Nét dày 10px → còn đúng 1px |  |  |  |  |  |  |
|  | Tốc độ: Chậm hơn ⏳ (nhiều vòng lặp) |  |  |  |  |  |  |
|  | Khi nào dùng cái nào? |  |  |  |  |  |  |
|  | Tình huống |  |  |  |  |  | Dùng |
|  | Muốn xóa nhiễu, thu nhỏ nét một chút |  |  |  |  |  | Erosion |
|  | Muốn vẽ lại đường tâm (skeleton) của nét |  |  |  |  |  | Thinning |
|  | Đếm đường nét, theo dõi đường thẳng |  |  |  |  |  | Thinning |
|  | Chuẩn bị cho Opening/Closing |  |  |  |  |  | Erosion |
|  | Nhận dạng ký tự (OCR) chuẩn hóa |  |  |  |  |  | Thinning |
|  | Làm mảnh nét |  |  |  |  |  |  |
|  |  | def main(): |  |  |  |  |  |
|  |  |     # Đọc ảnh bản vẽ |  |  |  |  |  |
|  |  |     image_path = ('docs/sample_nozawa_drawing.png') |  |  |  |  |  |
|  |  |     image = cv2.imread(image_path) |  |  |  |  |  |
|  |  |     # 1.Chuyển ảnh sang xám |  |  |  |  |  |
|  |  |     gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) |  |  |  |  |  |
|  |  |      |  |  |  |  |  |
|  |  |     # Làm mảnh nét |  |  |  |  |  |
|  |  |     _, binary = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY_INV) |  |  |  |  |  |
|  |  |     thinned = cv2.ximgproc.thinning(binary, thinningType=cv2.ximgproc.THINNING_ZHANGSUEN) |  |  |  |  |  |
|  |  |     scale = 0.5 |  |  |  |  |  |
|  |  |     cv2.imshow("Thinned", cv2.resize(thinned, (0, 0), fx=scale, fy=scale)) |  |  |  |  |  |
|  |  |     cv2.waitKey(0) |  |  |  |  |  |
|  |  |     cv2.destroyAllWindows() |  |  |  |  |  |
|  |  | Kết quả |  |  |  |  |  |
|  | Phát hiện đường thẳng |  |  |  |  |  |  |
|  |  | def main(): |  |  |  |  |  |
|  |  |     # Đọc ảnh bản vẽ |  |  |  |  |  |
|  |  |     image_path = ('docs/sample_nozawa_drawing.png') |  |  |  |  |  |
|  |  |     image = cv2.imread(image_path) |  |  |  |  |  |
|  |  |     # 1.Chuyển ảnh sang xám |  |  |  |  |  |
|  |  |     gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) |  |  |  |  |  |
|  |  |     # Tìm line |  |  |  |  |  |
|  |  |     # Bước 1: Phát hiện cạnh với cv2.Canny |  |  |  |  |  |
|  |  |     edges = cv2.Canny(gray, 50, 150, apertureSize=3) |  |  |  |  |  |
|  |  |     # Bước 2: Tìm đường thẳng với cv2.HoughLinesP |  |  |  |  |  |
|  |  |     lines = cv2.HoughLinesP(edges, rho=1, theta=np.pi/180, threshold=80, minLineLength=40, maxLineGap=10) |  |  |  |  |  |
|  |  |     # Bước 3: Vẽ đường thẳng lên ảnh |  |  |  |  |  |
|  |  |     output_lines = image.copy() # Tạo bản sao để không làm hỏng ảnh gốc |  |  |  |  |  |
|  |  |     print("Shape của lines:", lines.shape) |  |  |  |  |  |
|  |  |     print("Số đường tìm được:", len(lines)) |  |  |  |  |  |
|  |  |     if lines is not None: # Kiểm tra có tìm thấy đường không |  |  |  |  |  |
|  |  |         for line in lines: |  |  |  |  |  |
|  |  |             x1, y1, x2, y2 = line #Giải nén tọa độ từ [x1,y1,x2,y2] |  |  |  |  |  |
|  |  |             cv2.line(output_lines, (x1, y1), (x2, y2), (0, 0, 255), 2) # Điểm đầu điểm cuối đỏ BGR dày 2px |  |  |  |  |  |
|  |  |             print(f"Đường: ({x1},{y1}) --> ({x2},{y2})") |  |  |  |  |  |
|  |  | Kết quả |  |  |  |  |  |
|  |  |  | PS C:\work\Projects\Sanwa\02.SourceCode\python-hello-world> python main.py |  |  |  |  |
|  |  |  | Shape của lines: (253, 4) |  |  |  |  |
|  |  |  | Số đường tìm được: 253 |  |  |  |  |
|  |  |  | Đường: (44,1293) --> (1741,1293) |  |  |  |  |
|  |  |  | Đường: (42,46) --> (1743,46) |  |  |  |  |
|  |  |  | Đường: (42,1289) --> (1743,1289) |  |  |  |  |
|  |  |  | Đường: (44,42) --> (1741,42) |  |  |  |  |
|  |  |  | Đường: (42,86) --> (1743,86) |  |  |  |  |
|  |  |  | Đường: (1743,1291) --> (1743,44) |  |  |  |  |
|  |  |  | Đường: (42,89) --> (1739,89) |  |  |  |  |
|  |  |  | … |  |  |  |  |
|  |  | Giải thích |  |  |  |  |  |
|  |  |  | ## 📐 Giải thích: Phát Hiện Đường Thẳng (Line Detection) |  |  |  |  |
|  |  |  | ### Bước 1 — Phát hiện cạnh với `cv2.Canny` |  |  |  |  |
|  |  |  | ``` |  |  |  |  |
|  |  |  | edges = cv2.Canny(gray, 50, 150, apertureSize=3) |  |  |  |  |
|  |  |  | ``` |  |  |  |  |
|  |  |  | - `gray` → ảnh xám đầu vào |  |  |  |  |
|  |  |  | - `50` → **ngưỡng thấp**: pixel nào yếu hơn mức này thì bị loại |  |  |  |  |
|  |  |  | - `150` → **ngưỡng cao**: pixel mạnh hơn mức này thì chắc chắn là cạnh |  |  |  |  |
|  |  |  | - Vùng **giữa 50–150**: giữ lại nếu **nối liền với cạnh mạnh**, còn không thì bỏ |  |  |  |  |
|  |  |  | - `apertureSize=3` → kích thước bộ lọc Sobel bên trong (thường để mặc định 3) |  |  |  |  |
|  |  |  | --- |  |  |  |  |
|  |  |  | ### Bước 2 — Tìm đoạn thẳng với `cv2.HoughLinesP` |  |  |  |  |
|  |  |  | ``` |  |  |  |  |
|  |  |  | lines = cv2.HoughLinesP(edges, rho=1, theta=np.pi/180, threshold=80, minLineLength=40, maxLineGap=10) |  |  |  |  |
|  |  |  | ``` |  |  |  |  |
|  |  |  | Thuật toán hoạt động theo kiểu **"bầu chọn"**: mỗi điểm cạnh sẽ bỏ phiếu cho các đường thẳng đi qua nó, đường nào được bầu nhiều nhất thì được công nhận. |  |  |  |  |
|  |  |  | - `rho=1` → độ chính xác khoảng cách = 1 pixel (càng nhỏ càng chính xác) |  |  |  |  |
|  |  |  | - `theta=np.pi/180` → độ chính xác góc = **1 độ** |  |  |  |  |
|  |  |  | - `threshold=80` → phải có ít nhất **80 điểm bầu** mới công nhận là đường (giảm = bắt nhiều hơn, tăng = chỉ lấy đường rõ) |  |  |  |  |
|  |  |  | - `minLineLength=40` → đoạn thẳng phải dài **ít nhất 40 pixel** (ngắn hơn thì bỏ) |  |  |  |  |
|  |  |  | - `maxLineGap=10` → nếu 2 đoạn cách nhau **dưới 10 pixel** thì nối thành 1 |  |  |  |  |
|  |  |  | Kết quả `lines` trả về dạng mảng `(N, 1, 4)` → mỗi phần tử là `[[x1, y1, x2, y2]]` |  |  |  |  |
|  |  |  | --- |  |  |  |  |
|  |  |  | ### Bước 3 — Vẽ đường lên ảnh |  |  |  |  |
|  |  |  | ``` |  |  |  |  |
|  |  |  | output_lines = image.copy()       # Tạo bản sao để không làm hỏng ảnh gốc |  |  |  |  |
|  |  |  | if lines is not None:             # Kiểm tra có tìm thấy đường không |  |  |  |  |
|  |  |  |     for line in lines: |  |  |  |  |
|  |  |  |         x1, y1, x2, y2 = line[0] # Giải nén tọa độ từ [[x1,y1,x2,y2]] |  |  |  |  |
|  |  |  |         cv2.line(output_lines, (x1,y1), (x2,y2), (0,0,255), 2) |  |  |  |  |
|  |  |  |         #                       điểm đầu  điểm cuối  đỏ BGR   dày 2px |  |  |  |  |
|  |  |  | ``` |  |  |  |  |
|  |  |  | - `image.copy()` → luôn tạo bản sao trước khi vẽ |  |  |  |  |
|  |  |  | - `line[0]` → phải lấy phần tử `[0]` vì mỗi line có shape `(1, 4)` |  |  |  |  |
|  |  |  | - `(0, 0, 255)` → màu **đỏ** trong BGR (Blue=0, Green=0, Red=255) |  |  |  |  |
|  |  |  | --- |  |  |  |  |
|  |  |  | 💡 **Mẹo tinh chỉnh:** |  |  |  |  |
|  |  |  | - Muốn bắt **nhiều đường hơn** → giảm `threshold` và `minLineLength` |  |  |  |  |
|  |  |  | - Muốn **chỉ lấy đường dài** → tăng `minLineLength` |  |  |  |  |
|  |  |  | - Muốn **nối đoạn đứt gãy** → tăng `maxLineGap` |  |  |  |  |
|  |  | ## 📐 Nguyên Tắc Cơ Bản Tìm Đoạn Thẳng |  |  |  |  |  |
|  |  | ### Quy trình 3 bước |  |  |  |  |  |
|  |  | ``` |  |  |  |  |  |
|  |  | Ảnh gốc → [Canny] → Ảnh cạnh → [HoughLinesP] → Danh sách đoạn thẳng |  |  |  |  |  |
|  |  | ``` |  |  |  |  |  |
|  |  | --- |  |  |  |  |  |
|  |  | ### Bước 1: Tìm cạnh (Canny) |  |  |  |  |  |
|  |  | Máy tính **không thấy đường thẳng**, nó chỉ thấy **sự thay đổi độ sáng**. |  |  |  |  |  |
|  |  | - Chỗ nào màu sắc thay đổi đột ngột (sáng ↔ tối) → đó là **cạnh** |  |  |  |  |  |
|  |  | - Canny tính toán độ thay đổi đó và xuất ra ảnh trắng/đen: |  |  |  |  |  |
|  |  |   - **Trắng** = cạnh |  |  |  |  |  |
|  |  |   - **Đen** = không có gì |  |  |  |  |  |
|  |  | --- |  |  |  |  |  |
|  |  | ### Bước 2: Tìm đường thẳng (Hough Transform) |  |  |  |  |  |
|  |  | Ý tưởng: **mỗi điểm trắng "bầu chọn"** cho tất cả các đường thẳng có thể đi qua nó. |  |  |  |  |  |
|  |  | - Nếu nhiều điểm cùng bầu cho **một đường** → đường đó tồn tại |  |  |  |  |  |
|  |  | - `threshold=80` → cần ít nhất 80 điểm bỏ phiếu mới công nhận |  |  |  |  |  |
|  |  | Hình dung đơn giản: |  |  |  |  |  |
|  |  | > Giống như điều tra xem nhiều nhân chứng cùng nhìn thấy một chiếc xe không — càng nhiều người xác nhận thì chiếc xe đó càng chắc chắn có thật. |  |  |  |  |  |
|  |  | --- |  |  |  |  |  |
|  |  | ### Bước 3: Lọc kết quả |  |  |  |  |  |
|  |  | Không phải đường nào tìm được cũng hữu ích, nên lọc thêm: |  |  |  |  |  |
|  |  | | Điều kiện | Tham số | Ý nghĩa | |  |  |  |  |  |
|  |  | |---|---|---| |  |  |  |  |  |
|  |  | | Đủ dài | `minLineLength` | Đoạn quá ngắn → bỏ | |  |  |  |  |  |
|  |  | | Không đứt gãy | `maxLineGap` | Đoạn gần nhau → nối thành 1 | |  |  |  |  |  |
|  |  | --- |  |  |  |  |  |
|  |  | ### Tóm gọn trong 1 câu |  |  |  |  |  |
|  |  | > **Canny** tìm chỗ sáng/tối thay đổi → **Hough** dùng "bầu chọn" để xác định đường thẳng nào có đủ điểm cạnh xếp thẳng hàng → lọc theo độ dài và khoảng hở. |  |  |  |  |  |
|  | Contour, bouding box |  |  |  |  |  |  |
|  |  | Contour là gì? |  |  |  |  |  |
|  |  | Contour là đường viền bao quanh một vùng có cùng màu sắc/cường độ pixel. Nó giúp xác định hình dạng của các đối tượng trong ảnh. |  |  |  |  |  |
|  |  | Bounding Box là gì? |  |  |  |  |  |
|  |  | Bounding Box là hình chữ nhật nhỏ nhất bao quanh toàn bộ một contour. |  |  |  |  |  |
|  |  | # 6. Phân Tích Contour & Bounding Box |  |  |  |  |  |
|  |  | ## 🔍 Giải thích lý thuyết |  |  |  |  |  |
|  |  | ### Contour là gì? |  |  |  |  |  |
|  |  | **Contour** là đường viền bao quanh một vùng có cùng màu sắc/cường độ pixel. Nó giúp xác định hình dạng của các đối tượng trong ảnh. |  |  |  |  |  |
|  |  | ### Bounding Box là gì? |  |  |  |  |  |
|  |  | **Bounding Box** là hình chữ nhật nhỏ nhất bao quanh toàn bộ một contour. |  |  |  |  |  |
|  |  | --- |  |  |  |  |  |
|  |  | ## 📖 Giải thích từng dòng code |  |  |  |  |  |
|  |  | ```python |  |  |  |  |  |
|  |  | # Bước 1: Tìm tất cả contour trong ảnh nhị phân (binary) |  |  |  |  |  |
|  |  | contours, hierarchy = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE) |  |  |  |  |  |
|  |  | ``` |  |  |  |  |  |
|  |  | | Tham số | Ý nghĩa | |  |  |  |  |  |
|  |  | |---|---| |  |  |  |  |  |
|  |  | | `binary` | Ảnh đầu vào (phải là ảnh nhị phân - chỉ có 0 và 255) | |  |  |  |  |  |
|  |  | | `cv2.RETR_TREE` | Chế độ lấy contour: lấy **tất cả** và xây dựng cây phân cấp (cha-con) | |  |  |  |  |  |
|  |  | | `cv2.CHAIN_APPROX_SIMPLE` | Nén contour: chỉ lưu điểm đầu-cuối đoạn thẳng, tiết kiệm bộ nhớ | |  |  |  |  |  |
|  |  | | `contours` | Danh sách các contour tìm được | |  |  |  |  |  |
|  |  | | `hierarchy` | Quan hệ phân cấp giữa các contour (cha/con) | |  |  |  |  |  |
|  |  | > [!NOTE] Các chế độ `RETR_*`: |  |  |  |  |  |
|  |  | > - `RETR_EXTERNAL` – Chỉ lấy contour ngoài cùng |  |  |  |  |  |
|  |  | > - `RETR_LIST` – Lấy tất cả, không phân cấp |  |  |  |  |  |
|  |  | > - `RETR_TREE` – Lấy tất cả + xây cây phân cấp |  |  |  |  |  |
|  |  | ```python |  |  |  |  |  |
|  |  | output_contours = image.copy()  # Sao chép ảnh gốc để vẽ lên |  |  |  |  |  |
|  |  | for cnt in contours:            # Duyệt từng contour |  |  |  |  |  |
|  |  |     area = cv2.contourArea(cnt) # Tính diện tích (pixel²) |  |  |  |  |  |
|  |  |     if area > 100:              # Lọc bỏ contour quá nhỏ (nhiễu) |  |  |  |  |  |
|  |  |         x, y, w, h = cv2.boundingRect(cnt)  # Lấy tọa độ bounding box |  |  |  |  |  |
|  |  |         #   x, y = góc trên-trái |  |  |  |  |  |
|  |  |         #   w, h = chiều rộng, chiều cao |  |  |  |  |  |
|  |  |         cv2.rectangle(output_contours, (x, y), (x+w, y+h), (0, 255, 0), 2) |  |  |  |  |  |
|  |  |         #   Vẽ hình chữ nhật màu xanh lá, độ dày 2px |  |  |  |  |  |
|  |  | ``` |  |  |  |  |  |
|  |  | --- |  |  |  |  |  |
|  |  | ## ✍️ Ví dụ hoàn chỉnh |  |  |  |  |  |
|  |  | ```python |  |  |  |  |  |
|  |  | import cv2 |  |  |  |  |  |
|  |  | import numpy as np |  |  |  |  |  |
|  |  | def main(): |  |  |  |  |  |
|  |  |     # Bước 1: Tạo ảnh mẫu có các hình dạng |  |  |  |  |  |
|  |  |     image = np.zeros((400, 600, 3), dtype='uint8') # Ảnh đen nền |  |  |  |  |  |
|  |  |     # Vẽ một số hình lên ảnh |  |  |  |  |  |
|  |  |     cv2.rectangle(image, (50, 50), (150, 150), (255, 200, 100), -1) # Hình vuông xanh ngọc |  |  |  |  |  |
|  |  |     cv2.circle(image, (300, 200), 80, (100, 255, 100), -1) # Hình tròn xanh green |  |  |  |  |  |
|  |  |     cv2.rectangle(image, (420, 100), (560, 300), (200, 150, 255), -1) # Hình chữ nhật hồng |  |  |  |  |  |
|  |  |     # Bước 2: Chuyển sang ảnh xám + nhị phân |  |  |  |  |  |
|  |  |     gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) |  |  |  |  |  |
|  |  |     _, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY) |  |  |  |  |  |
|  |  |     # Bước 3: Tìm Contour |  |  |  |  |  |
|  |  |     contours, hierachy = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE) |  |  |  |  |  |
|  |  |     print(f"Tổng số contour tìm được: {len(contours)}") |  |  |  |  |  |
|  |  |     # Bước 4: Vẽ Contours + Bouding Box |  |  |  |  |  |
|  |  |     output = image.copy() |  |  |  |  |  |
|  |  |     for i, cnt in enumerate(contours): |  |  |  |  |  |
|  |  |         area = cv2.contourArea(cnt) # Tính diện tích |  |  |  |  |  |
|  |  |         if area > 100: # Lọc nhiễu |  |  |  |  |  |
|  |  |             # Vẽ contour(màu đỏ) |  |  |  |  |  |
|  |  |             cv2.drawContours(output, [cnt], -1, (0, 0, 255), 2) |  |  |  |  |  |
|  |  |             # Vẽ bounding box(màu xanh lá) |  |  |  |  |  |
|  |  |             x, y, w, h = cv2.boundingRect(cnt) |  |  |  |  |  |
|  |  |             cv2.rectangle(output, (x, y), (x + w, y + h), (0, 255, 0), 2) |  |  |  |  |  |
|  |  |             # Hiển thị thông tin |  |  |  |  |  |
|  |  |             label = f"{i} A = {int(area)}" |  |  |  |  |  |
|  |  |             cv2.putText(output, label, (x, y - 8), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 0), 1) |  |  |  |  |  |
|  |  |             print(f"Contour #{i}: diện tích = {int(area)}, BBox=({x}, {y}, {w}, {h})") |  |  |  |  |  |
|  |  |     # Bước 5: Hiển thị kết quả |  |  |  |  |  |
|  |  |     cv2.imshow("Origin Image", image) |  |  |  |  |  |
|  |  |     cv2.imshow("Gray Image", gray) |  |  |  |  |  |
|  |  |     cv2.imshow("Binary Image", binary) |  |  |  |  |  |
|  |  |     cv2.imshow("Contour + Bounding Box", output) |  |  |  |  |  |
|  |  |     cv2.waitKey(0) |  |  |  |  |  |
|  |  |     cv2.destroyAllWindows() |  |  |  |  |  |
|  |  | # BƯỚC 5: Hiển thị kết quả |  |  |  |  |  |
|  |  | # ========================================= |  |  |  |  |  |
|  |  | cv2.imshow("Anh goc",      image) |  |  |  |  |  |
|  |  | cv2.imshow("Anh nhi phan", binary) |  |  |  |  |  |
|  |  | cv2.imshow("Contour + BoundingBox", output) |  |  |  |  |  |
|  |  | cv2.waitKey(0) |  |  |  |  |  |
|  |  | cv2.destroyAllWindows() |  |  |  |  |  |
|  |  | ``` |  |  |  |  |  |
|  |  | --- |  |  |  |  |  |
|  |  | ## 🧠 Tóm tắt luồng xử lý |  |  |  |  |  |
|  |  | ``` |  |  |  |  |  |
|  |  | Ảnh gốc (BGR) |  |  |  |  |  |
|  |  |     │ |  |  |  |  |  |
|  |  |     ▼ |  |  |  |  |  |
|  |  | Ảnh xám (grayscale) |  |  |  |  |  |
|  |  |     │ |  |  |  |  |  |
|  |  |     ▼ |  |  |  |  |  |
|  |  | Ảnh nhị phân (threshold/Canny) |  |  |  |  |  |
|  |  |     │ |  |  |  |  |  |
|  |  |     ▼ |  |  |  |  |  |
|  |  | findContours() → danh sách contour |  |  |  |  |  |
|  |  |     │ |  |  |  |  |  |
|  |  |     ▼ |  |  |  |  |  |
|  |  | Lọc theo diện tích (area > 100) |  |  |  |  |  |
|  |  |     │ |  |  |  |  |  |
|  |  |     ├─→ drawContours() → vẽ viền đỏ |  |  |  |  |  |
|  |  |     └─→ boundingRect() → vẽ hộp xanh lá |  |  |  |  |  |
|  |  | ``` |  |  |  |  |  |
|  |  | --- |  |  |  |  |  |
|  |  | ## 💡 Mẹo thực tế |  |  |  |  |  |
|  |  | | Tình huống | Gợi ý | |  |  |  |  |  |
|  |  | |---|---| |  |  |  |  |  |
|  |  | | Quá nhiều contour nhiễu | Tăng ngưỡng `area > 500` hoặc dùng `cv2.RETR_EXTERNAL` | |  |  |  |  |  |
|  |  | | Muốn lấy contour gần với hình thật | Dùng `cv2.CHAIN_APPROX_NONE` (lưu mọi điểm) | |  |  |  |  |  |
|  |  | | Muốn hộp xoay theo góc nghiêng | Dùng `cv2.minAreaRect()` thay cho `boundingRect()` | |  |  |  |  |  |
|  |  | | Muốn hình tròn bao quanh | Dùng `cv2.minEnclosingCircle()` | |  |  |  |  |  |
|  |  | ## Giải thích hàm `cv2.rectangle()` |  |  |  |  |  |
|  |  | Hàm này dùng để **vẽ hình chữ nhật** lên ảnh trong OpenCV. |  |  |  |  |  |
|  |  | --- |  |  |  |  |  |
|  |  | ### Các tham số |  |  |  |  |  |
|  |  | | Tham số | Kiểu | Bắt buộc | Mô tả | |  |  |  |  |  |
|  |  | |---|---|---|---| |  |  |  |  |  |
|  |  | | `img` | `MatLike` | ✅ | Ảnh đầu vào (numpy array). Hình chữ nhật sẽ được vẽ trực tiếp lên ảnh này. | |  |  |  |  |  |
|  |  | | `pt1` | `Point` | ✅ | Tọa độ góc **trên-trái** của hình chữ nhật, dạng `(x, y)` | |  |  |  |  |  |
|  |  | | `pt2` | `Point` | ✅ | Tọa độ góc **dưới-phải** của hình chữ nhật, dạng `(x, y)` | |  |  |  |  |  |
|  |  | | `color` | `Scalar` | ✅ | Màu sắc đường viền, dạng `(B, G, R)` — ví dụ: `(0, 255, 0)` là màu xanh lá | |  |  |  |  |  |
|  |  | | `thickness` | `int` | ❌ | Độ dày nét vẽ (pixel). Nếu truyền **`-1`** → tô đặc toàn bộ hình chữ nhật | |  |  |  |  |  |
|  |  | | `lineType` | `int` | ❌ | Kiểu đường kẻ: `cv2.LINE_4`, `cv2.LINE_8` (mặc định), `cv2.LINE_AA` (khử răng cưa) | |  |  |  |  |  |
|  |  | | `shift` | `int` | ❌ | Số bit thập phân trong tọa độ điểm (thường để mặc định `0`) | |  |  |  |  |  |
|  |  | --- |  |  |  |  |  |
|  |  | ### Ví dụ sử dụng |  |  |  |  |  |
|  |  | ```python |  |  |  |  |  |
|  |  | import cv2 |  |  |  |  |  |
|  |  | img = cv2.imread("image.jpg") |  |  |  |  |  |
|  |  | # Vẽ hình chữ nhật màu xanh lá, nét dày 2px |  |  |  |  |  |
|  |  | cv2.rectangle( |  |  |  |  |  |
|  |  |     img, |  |  |  |  |  |
|  |  |     pt1=(50, 50),    # góc trên-trái |  |  |  |  |  |
|  |  |     pt2=(200, 150),  # góc dưới-phải |  |  |  |  |  |
|  |  |     color=(0, 255, 0), |  |  |  |  |  |
|  |  |     thickness=2, |  |  |  |  |  |
|  |  |     lineType=cv2.LINE_AA |  |  |  |  |  |
|  |  | ) |  |  |  |  |  |
|  |  | # Vẽ hình chữ nhật tô đặc màu đỏ (thickness = -1) |  |  |  |  |  |
|  |  | cv2.rectangle(img, (300, 50), (450, 150), (0, 0, 255), thickness=-1) |  |  |  |  |  |
|  |  | cv2.imshow("Result", img) |  |  |  |  |  |
|  |  | cv2.waitKey(0) |  |  |  |  |  |
|  |  | ``` |  |  |  |  |  |
|  |  | --- |  |  |  |  |  |
|  |  | ### Lưu ý quan trọng |  |  |  |  |  |
|  |  | > [!IMPORTANT] |  |  |  |  |  |
|  |  | > - `color` theo thứ tự **BGR** (không phải RGB) trong OpenCV. |  |  |  |  |  |
|  |  | > - Hàm **sửa trực tiếp** `img` (in-place) và cũng **trả về** `img`. |  |  |  |  |  |
|  |  | > - `pt1` phải là góc **trên-trái**, `pt2` phải là góc **dưới-phải**; nếu đảo ngược tọa độ, OpenCV vẫn tự xử lý đúng. |  |  |  |  |  |
## Sheet: DXF_File
| <<Overview |  |
| --- | --- |
|  | Tìm hiểu  DXF File |
|  | **DXF** (viết tắt của **Drawing Exchange Format** hoặc *Drawing Interchange Format*) là định dạng tệp bản vẽ kỹ thuật do hãng **Autodesk** (công ty phát triển phần mềm AutoCAD nổi tiếng) tạo ra từ năm 1982. |
|  | --- |
|  | ### 1. Mục đích ra đời của DXF |
|  | Trong kỹ thuật cơ khí, xây dựng và kiến trúc, định dạng file thiết kế chuẩn của AutoCAD là **`.DWG`** — nhưng `.dwg` là định dạng đóng, độc quyền và rất khó để các phần mềm khác đọc được. |
|  | Vì vậy, Autodesk tạo ra **`.DXF`** như một **"ngôn ngữ chung"**: |
|  | - Cho phép chia sẻ, trao đổi dữ liệu bản vẽ giữa AutoCAD với các phần mềm CAD/CAM/CNC khác (như SolidWorks, Catia, phần mềm cắt laser, máy in 3D,...). |
|  | #NAME? |
|  | --- |
|  | ### 2. File DXF chứa những thông tin gì? |
|  | DXF lưu trữ bản vẽ dưới dạng **đồ hoạ vector** (không phải ảnh pixel như JPG hay PNG). Dữ liệu bên trong bao gồm: |
|  | - **Các thực thể hình học (Entities):** Toạ độ các điểm, đoạn thẳng (`LINE`), đường tròn (`CIRCLE`), cung tròn (`ARC`), đa tuyến (`POLYLINE`), đường cong spline, các khối ký hiệu (`BLOCK / INSERT`). |
|  | - **Lớp bản vẽ (Layers):** Phân chia các nét vẽ theo từng tầng (nét thấy, nét khuất, nét kích thước,...). |
|  | - **Chữ & Chú thích (Text / Dimension):** Nội dung chữ, ký hiệu và kích thước kèm toạ độ đặt chữ. |
|  | --- |
|  | ### 3. File DXF đóng vai trò gì trong dự án của bạn? |
|  | Trong dự án **find_data_integration** này: |
|  | 1. **File gốc là [`1.dxf`](file:///c:/work/Projects/Sanwa/01.Document/find_data_integration/1.dxf) / [`2.dxf`](file:///c:/work/Projects/Sanwa/01.Document/find_data_integration/2.dxf)**: Đây chính là bản vẽ thiết kế kỹ thuật thực tế. |
|  | 2. **Thư viện [`ezdxf`](file:///c:/work/Projects/Sanwa/01.Document/find_data_integration/inject.py#L338-L341)** (trong Python): Mở file DXF này ra và đọc toàn bộ ~140.000 đoạn nét vẽ hình học cùng toạ độ thực tế của chúng. |
|  | 3. **Quy đổi sang [`banve.svg`](file:///c:/work/Projects/Sanwa/01.Document/find_data_integration/banve.svg)**:  |
|  |    - Vì trình duyệt web (Chrome, Edge) không thể mở trực tiếp file DXF, code trong [`inject.py`](file:///c:/work/Projects/Sanwa/01.Document/find_data_integration/inject.py) đã chuyển đổi toạ độ từ DXF sang ảnh vector **SVG** để hiển thị sắc nét trên web. |
|  |    - Khi bạn kéo chuột chọn symbol trên web, hệ thống sẽ ánh xạ toạ độ từ màn hình ngược lại hệ toạ độ của DXF để tra cứu và đếm số lượng. |
## Sheet: Sample01
| <<Overview |  |
| --- | --- |
|  | Tìm hiểu Sample01 |
|  | Dưới đây là hướng dẫn chi tiết về cách chạy và sử dụng dự án **find_data_integration**. |
|  | --- |
|  | ### 1. Tổng quan dự án |
|  | Dự án này là hệ thống tích hợp xử lý bản vẽ kỹ thuật CAD (file DXF) và dữ liệu OCR: |
|  | - **`inject.py`**: Chuyển đổi bản vẽ CAD (`.dxf`) sang định dạng vector SVG (`banve.svg`), tính toán ma trận quy đổi toạ độ DXF $\leftrightarrow$ SVG (`mapping.json`), đồng thời nhúng CSS/JavaScript tương tác trực tiếp vào file SVG. |
|  | *L21*`find_data_integration.py`**: Chứa thuật toán khớp toạ độ vùng người dùng chọn trên SVG sang toạ độ DXF, đối chiếu với cơ sở dữ liệu chữ/symbol OCR (`P60_with_region.json`) và phân loại số lượng xuất hiện theo từng khu vực phân vùng (`regions_box.json`). |
|  | - **`server.py`**: Khởi chạy một Web Server với FastAPI / Uvicorn, phục vụ bản vẽ trực quan và các API tìm kiếm symbol (`/api/find`, `/api/regions`). |
|  | --- |
|  | ### 2. Các bước chạy dự án |
|  | Thư mục hiện tại của bạn đã có sẵn môi trường ảo `venv` và các thư viện cần thiết. Bạn chỉ cần thực hiện các bước sau trong Terminal (PowerShell hoặc Command Prompt tại thư mục dự án): |
|  | #### Bước 1: Kích hoạt môi trường ảo (`venv`) |
|  | - **Trên PowerShell**: |
|  |   ```powershell |
|  |   .\venv\Scripts\Activate.ps1 |
|  |   ``` |
|  |   *(Nếu gặp lỗi bị chặn script execution policy trên PowerShell, hãy chạy lệnh: `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process` rồi kích hoạt lại)*. |
|  | - **Trên Command Prompt (CMD)**: |
|  |   ```cmd |
|  |   venv\Scripts\activate.bat |
|  |   ``` |
|  | *(Lưu ý: Nếu sau này cần cài lại thư viện trên máy mới, bạn chỉ cần gõ `pip install -r requirements.txt`)*. |
|  | --- |
|  | #### Bước 2: Khởi động Server |
|  | Có 2 cách khởi chạy: |
|  | * **Cách 1 (Khuyên dùng - tự động mở trình duyệt web)**: |
|  |   ```powershell |
|  |   python server.py |
|  |   ``` |
|  |   Sau khi khởi chạy khoảng 2 giây, hệ thống sẽ tự động bật trình duyệt mặc định và mở trang bản vẽ. |
|  | * **Cách 2 (Sử dụng Uvicorn với chế độ tự động reload khi sửa code)**: |
|  |   ```powershell |
|  |   uvicorn server:app --reload |
|  |   ``` |
|  |   Sau đó, bạn tự mở trình duyệt và truy cập: [http://127.0.0.1:8000](http://127.0.0.1:8000). |
|  | --- |
|  | ### 3. Cách sử dụng trên giao diện Web |
|  | 1. Khi truy cập vào [http://127.0.0.1:8000](http://127.0.0.1:8000), hệ thống tự chuyển hướng tới `/banve.svg`. |
|  | 2. Giao diện hiển thị toàn bộ bản vẽ kỹ thuật (được render dưới dạng vector sắc nét). |
|  | 3. **Thao tác tìm kiếm Symbol**: |
|  |    - Sử dụng chuột kéo thả (drag & drop) một khung chữ nhật bao quanh ký hiệu (symbol) hoặc đoạn chữ bạn cần tìm. |
|  |    - Script nhúng trên trình duyệt sẽ tự động gửi toạ độ hộp chọn về API `/api/find`. |
|  |    - Hệ thống sẽ tìm các symbol/chữ tương ứng trên toàn bộ bản vẽ và highlight (làm nổi bật) tất cả các vị trí trùng khớp, đồng thời hiển thị bảng thống kê số lượng theo từng khu vực (region như `DB10`,...). |
|  | --- |
|  | ### 4. Các cấu hình quan trọng cần biết |
|  | Khi bạn muốn thay đổi bản vẽ hoặc dữ liệu đầu vào, hãy lưu ý cấu hình trong các file sau: |
|  | 1. **Thay đổi file bản vẽ DXF ([`inject.py`](file:///c:/work/Projects/Sanwa/01.Document/find_data_integration/inject.py#L39-L57))**: |
|  |    - Dòng 39: `DXF_PATH = "1.dxf"` $\rightarrow$ Đổi tên/đường dẫn đến file DXF bạn muốn hiển thị (ví dụ: `"2.dxf"`). |
|  |    - Dòng 56: `REBUILD = True` $\rightarrow$ Đặt thành `True` khi bạn thay đổi file DXF hoặc muốn vẽ lại toàn bộ SVG. Khi `REBUILD = True`, quá trình phân tích DXF và tạo lại `banve.svg` sẽ mất từ 1 đến vài chục giây tuỳ độ phức tạp bản vẽ. |
|  |    - Khi đã tạo xong file SVG ưng ý, bạn có thể chỉnh lại `REBUILD = False` để server khởi động tức thì trong các lần sau. |
|  | 2. **Dữ liệu OCR & Phân vùng ([`find_data_integration.py`](file:///c:/work/Projects/Sanwa/01.Document/find_data_integration/find_data_integration.py#L39-L44))**: |
|  |    - `OCR_PATH = BASE_DIR / "P60_with_region.json"`: File dữ liệu chứa các toạ độ text OCR. |
|  |    - `REGIONS_PATH = BASE_DIR / "regions_box.json"`: File dữ liệu định nghĩa các phân vùng trên bản vẽ. |
|  |    - Đảm bảo 2 file này nằm cùng thư mục với `server.py`. |
## Sheet: Sample02
| <<Overview |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | Tìm hiểu Sample02 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | Nội dung Sample02: Kiểm thử tự động bản vẽ Cửa thép Sanwa Phase 1 (sanwa_sd_verification_demo.py) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | Đối tượng kiểm thử: Bản vẽ CAD Cửa thép đơn 1 cánh Sanwa Shutter (Mã SD-1 / 1LSD-24). |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | Mục tiêu nghiệp vụ: Tự động hóa quá trình so khớp dữ liệu đơn hàng trong DB Access (yêu cầu từ khách hàng) với Bản vẽ CAD (do nhân viên kỹ thuật vẽ) để phát hiện sai sót trước khi sản xuất. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | 1. Các hạng mục kiểm thử chính (Verification Items) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | 1. Đo kích thước khung cửa: Xác định chiều rộng (\(W\)) và chiều cao (\(H\)) phủ bì của khung ngoại. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | 2. Định vị ổ khóa: Dò tìm vị trí tâm lỗ khóa và tính độ cao tay khóa từ chân sàn lên (\(\text{Lock Height}\)). |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | 3. Đếm số lượng bản lề: Quét dọc mép khung đứng bên trái để đếm tổng số bản lề thép đính trên khung. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | 4. Phát hiện góc dập L-Notch: Nhận diện vết cắt dập khuyết chữ L ở chân khung cửa. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | 5. Đánh giá Pass/Fail: So sánh thông số đo được với DB Access dựa trên dung sai cho phép \(\le 10\text{mm}\). |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | 2. Công nghệ & Thuật toán OpenCV sử dụng |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | Ngôn ngữ & Thư viện: Python, opencv-contrib-python, numpy, pandas. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | Lọc nét màu (cv2.inRange): Tách nét vẽ màu đen của cửa, loại bỏ hoàn toàn đường dóng kích thước màu xanh dương và chữ viết. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | Khoanh vùng & Đo đạc (cv2.findContours + cv2.boundingRect): Trích xuất tọa độ \((x, y, w, h)\) để đo kích thước khung cửa, đếm bản lề và phát hiện chân L-Notch. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | Dò hình tròn (cv2.HoughCircles): Định vị tâm và bán kính lỗ tròn ổ khóa. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | 3. Kết quả đầu ra (Outputs) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | Báo cáo dạng Bảng (Console/Excel Log): Bảng so sánh chi tiết giữa Yêu cầu DB Access vs. Đo thực tế OpenCV kèm độ sai lệch \(\Delta\) và trạng thái MATCH / MISMATCH. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | Bản vẽ xuất trực quan (.png): Ảnh bản vẽ CAD được OpenCV vẽ khung khoanh vùng lỗi, gắn nhãn vị trí (HINGE, LOCK HT, L-NOTCH) và đính banner kết luận PASSED (Xanh) hoặc FAILED (Đỏ). |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | Ảnh đầu vào |  |  |  |  |  |  |  |  |  | Ảnh đầu ra PASS |  |  |  |  |  |  |  |  | Ảnh đầu ra FAIL |
|  |  | sample_steel_door_sd1.png |  |  |  |  |  |  |  |  | sanwa_sd_result_SD-1_PASS.png |  |  |  |  |  |  |  |  | sanwa_sd_result_SD-1_FAIL.png |
|  | Tiến hành run file sanwa_sd_verification_demo.py |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  | 1. if __name__ == "__main__": |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  | Ý nghĩa: Đảm bảo các dòng lệnh bên trong chỉ chạy khi bạn mở và thực thi trực tiếp file script này |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  (python sanwa_sd_verification_demo.py). |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  | 2. Kịch bản 1: Kiểm thử bản vẽ KHỚP 100% (SD-1_PASS) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  | correct_sd_specs: Khai báo mảng dữ liệu giả lập yêu cầu từ DB Access  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  | (Rộng 900mm, Cao 2100mm, Khóa 1000mm, Có L-Notch, 3 Bản lề). |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  | run_steel_door_verification(...): Đưa ảnh sample_steel_door_sd1.png vào so sánh.  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  | 3. Kịch bản 2: Kiểm thử bản vẽ CÓ SAI LỆCH (SD-1_FAIL) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  | erroneous_sd_specs: Cố tình giả lập dữ liệu DB Access bị lệch 2 thông số so với thực tế trên bản vẽ: |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  | Độ cao khóa: DB yêu cầu 850.0 mm (nhưng bản vẽ đang vẽ 1000.0 mm). |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  | Số bản lề: DB yêu cầu 4 cái (nhưng bản vẽ chỉ vẽ 3 cái). |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  | run_steel_door_verification(...): Khi chạy, thuật toán OpenCV sẽ so sánh chênh lệch, phát hiện ra ngay 2 lỗi này và thông báo FAILED. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | Mô tả code function chính run_steel_door_verification |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | img = cv2.imread(image_path) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  | Đọc ảnh |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | black_mask = cv2.inRange(img, (0, 0, 0), (80, 80, 80)) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  | Dòng lệnh này trong OpenCV thực hiện kỹ thuật Lọc màu (Color Filtering / Color Masking)  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  | để giữ lại duy nhất các nét vẽ màu đen của khung cửa và loại bỏ hoàn toàn các đường  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  | dóng kích thước màu xanh dương cũng như chữ viết trên bản vẽ. Cụ thể ý nghĩa từng phần như sau: |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  | 1. Phân tích chi tiết cú pháp |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  | black_mask = cv2.inRange(img, (0, 0, 0), (80, 80, 80)) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  | cv2.inRange(...): Lệnh kiểm tra xem từng pixel trong ảnh có nằm trong dải màu từ [Thấp nhất] đến [Cao nhất] hay không. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  | img: Ảnh bản vẽ đầu vào (trong OpenCV, màu sắc được lưu theo thứ tự BGR: Blue - Green - Red). |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  | (0, 0, 0): Ngưỡng màu thấp nhất — tương ứng với màu Đen tuyền (B=0, G=0, R=0). |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  | (80, 80, 80): Ngưỡng màu cao nhất — tương ứng với màu Xám đậm / Gần đen (B=80, G=80, R=80). |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  | 👉 Kết quả trả về (black_mask): Là một ảnh nhị phân (chỉ có 2 màu đen & trắng): |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  | Pixel nào thuộc nét vẽ màu đen (có dải màu BGR từ 0 đến 80) $\rightarrow$ Sẽ chuyển thành màu Trắng (giá trị 255). |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  | Pixel nào có màu xanh dương, màu đỏ, màu chữ hoặc nền trắng $\rightarrow$ Sẽ bị loại bỏ hoàn toàn và biến thành màu Đen (giá trị 0). |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  | 2. Tại sao bước này lại CỰC KỲ QUAN TRỌNG trong dự án SANWA? |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  | Trên bản vẽ CAD cửa thép (sample_steel_door_sd1.png): |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  | 1. Nét vẽ khung cửa chính, bản lề, ổ khóa: Được vẽ bằng nét mực màu đen. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  | 2. Đường dóng kích thước (Dimension lines) & Con số (Text): Thường được vẽ bằng màu xanh dương (Blue). |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  | Nếu bạn chỉ dùng hàm chuyển ảnh xám cvtColor thông thường, OpenCV sẽ coi đường dóng màu xanh cũng là đường nét bản vẽ.  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  | Khi chạy thuật toán findContours để đo chiều rộng/chiều cao cửa, OpenCV sẽ bị dính các đường  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  | dóng kích thước vào khung cửa ➔ dẫn đến đo sai kích thước thực tế. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  | Nhờ dòng lệnh cv2.inRange này, chúng ta tạo ra một mặt nạ (Mask) cực kỳ sạch,  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  | giúp OpenCV "mắt mù" với các đường dóng màu xanh và chỉ tập trung soi đúng khung cửa thép màu đen. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | contours, _ = cv2.findContours(black_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  | Đây là bước quan trọng nhất để OpenCV "xác định và khoanh vùng" các hình khối (như khung cửa, bản lề, vết cắt L-Notch) từ bức ảnh nhị phân black_mask |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  | 1. Đầu ra (Return Values): contours, _ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  | contours: Là một danh sách (Python list). Mỗi phần tử trong danh sách này đại diện cho một đường viền khép kín (Contour). Một contour thực chất là một mảng tập hợp các tọa độ $(x, y)$ của các điểm nối liền với nhau tạo thành ranh giới bao quanh hình khối. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  | _ (Hierarchy): Là bảng phân cấp biểu diễn quan hệ cha-con giữa các đường viền (ví dụ: contour nào nằm ngoài, contour nào nằm lồng bên trong). Do trong đoạn này ta chưa cần dùng tới bảng phân cấp này nên dùng dấu gạch dưới _ để bỏ qua. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  | 2. Các tham số đầu vào (Arguments) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  | ① black_mask (Ảnh nhị phân đầu vào) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  | Là bức ảnh đen-trắng thu được từ bước cv2.inRange trước đó. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  | OpenCV sẽ quét qua toàn bộ ảnh này và đi tìm ranh giới của tất cả các vùng màu Trắng (nét vẽ bản lề/khung cửa) đứng trên nền màu Đen. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  | ② cv2.RETR_TREE (Chế độ truy xuất đường viền) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  | Xác định cách OpenCV tìm kiếm và tổ chức các đường viền. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  | RETR_TREE sẽ quét và lập bản đồ toàn bộ cây phân cấp (Tree Hierarchy) của mọi contour. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  | Ví dụ: Nó sẽ nhận biết khung cửa ngoại là contour cha (bên ngoài), còn lỗ khóa và bản lề nằm bên trong là các contour con (bên trong). |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  | ③ cv2.CHAIN_APPROX_SIMPLE (Phương pháp nén tọa độ) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  | Đây là kỹ thuật nén điểm giúp tăng tốc độ xử lý và tiết kiệm bộ nhớ: |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  | Nếu dùng CHAIN_APPROX_NONE: Một đường thẳng dài $100\text{px}$ sẽ phải lưu trữ đủ cả $100$ tọa độ pixel. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  | Khi dùng CHAIN_APPROX_SIMPLE: OpenCV tự động tối ưu và chỉ lưu 2 điểm đầu - cuối của đường thẳng |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  | (hoặc 4 điểm góc đối với một khung hình chữ nhật). |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  | 💡 Tóm tắt tác dụng trong kịch bản SANWA: |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  | Sau khi dòng lệnh này chạy xong, biến contours sẽ chứa danh sách tọa độ của tất cả các hình vẽ màu đen trên bản vẽ. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  | Vòng lặp for cnt in contours: ngay sau đó sẽ duyệt qua danh sách này,  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  | lấy ra từng đường viền và dùng lệnh cv2.boundingRect(cnt) để đo chính xác chiều rộng ($w$), chiều cao ($h$) của khung cửa thép! |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | for cnt in contours: |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |         area = cv2.contourArea(cnt) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |         x, y, w, h = cv2.boundingRect(cnt) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |         # Khung cửa chính w ~ 360, h ~ 840 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |         if 330 <= w <= 400 and 800 <= h <= 900: |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |             if area > max_area: |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |                 max_area = area |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |                 door_frame_cnt = cnt |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  | 1. for cnt in contours: |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  | Ý nghĩa: Vòng lặp duyệt qua lần lượt từng đường viền cnt trong danh sách contours mà hàm cv2.findContours tìm được ở bước trước. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  | Trên bản vẽ có rất nhiều đường viền (khung cửa, lỗ khóa, bản lề, vết cắt L-notch...),  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |   nên ta phải kiểm tra từng đường viền để nhặt ra đúng khung cửa chính. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  | 2. area = cv2.contourArea(cnt) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  | cv2.contourArea(cnt): Hàm tính diện tích tổng cộng (tính bằng số pixel) nằm bên trong đường viền cnt. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  | 3. x, y, w, h = cv2.boundingRect(cnt) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  | cv2.boundingRect(cnt): Vẽ một hình chữ nhật bao quanh tối thiểu (Bounding Box) bao lấy đường viền cnt. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  | Hàm trả về 4 thông số kích thước (tính bằng pixel): |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  | x, y: Tọa độ góc trên-bên trái của hình chữ nhật trên bức ảnh. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  | w (Width): Chiều rộng của hình chữ nhật. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  | h (Height): Chiều cao của hình chữ nhật. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  | 4. if 330 <= w <= 400 and 800 <= h <= 900: (Bộ lọc kích thước - Dimension Filtering) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  | Tại sao cần dòng này? Nếu không lọc, OpenCV sẽ bị lẫn giữa khung cửa chính với các hình vẽ nhỏ khác như bản lề hay lỗ khóa. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  | Logic lọc: Chỉ chấp nhận những đường viền nào có Chiều rộng w từ 330 đến 400 pixel  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |   VÀ Chiều cao h từ 800 đến 900 pixel (đây là dải kích thước chuẩn của khung cửa thép trên bức ảnh mẫu sample_steel_door_sd1.png). |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  | 5. Tìm Contour lớn nhất phù hợp (if area > max_area:) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  | if area > max_area: |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |     max_area = area |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |     door_frame_cnt = cnt |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  | Trong trường hợp có nhiều hình lồng nhau thỏa mãn điều kiện kích thước trên, thuật toán sẽ so sánh diện tích area. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  | Hình nào có diện tích lớn nhất (max_area) sẽ được chọn và lưu vào biến door_frame_cnt  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  | — chính thức xác định đây là Khung cửa thép chính. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  | 💡 Tóm tắt kết quả sau đoạn code này: |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  | Sau khi vòng lặp kết thúc, ta thu được biến door_frame_cnt chứa toàn bộ tọa độ khung cửa.  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  | Từ đó, ở các dòng lệnh tiếp theo ta chỉ cần nhân w và h với tỷ lệ SCALE_MM_PER_PX = 2.5 để đổi ra kích thước milimét thực tế của cửa: |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  | measured_width = w * 2.5 (mm) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  | measured_height = h * 2.5 (mm) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  # Kiểm tra góc cắt L-Notch ở chân khung cửa |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |         for cnt in contours: |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |             bx, by, bw, bh = cv2.boundingRect(cnt) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |             if abs(by - (y + h - 40)) < 30 and (abs(bx - (x - 35)) < 15 or abs(bx - (x + w + 4)) < 15): |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |                 if 20 <= bw <= 40 and 30 <= bh <= 50: |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |                     has_l_notch = True |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |                     cv2.rectangle(annotated, (bx, by), (bx + bw, by + bh), (0, 0, 255), 2) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |                     cv2.putText(annotated, "L-NOTCH", (bx - 10, by + bh + 15), |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |                                 cv2.FONT_HERSHEY_SIMPLEX, 0.45, (0, 0, 255), 1) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  | Phát hiện vết cắt khuyết L-Notch ở chân khung cửa thép (vết dập chữ L giúp chân khung cửa ôm sập âm vào sàn bê tông). |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  | 1. for cnt in contours: & bx, by, bw, bh = cv2.boundingRect(cnt) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  | Vòng lặp duyệt qua từng đường viền cnt trên bản vẽ và lấy ra: |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  | bx, by: Tọa độ góc trên-bên trái của đối tượng đang xét. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  | bw, bh: Chiều rộng (bw) và chiều cao (bh) của đối tượng đang xét. (Lưu ý: Phân biệt với x, y, w, h là tọa độ và kích thước của Khung cửa chính đã tìm được ở bước trước). |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  | 2. Điều kiện 1: Kiểm tra Vị trí Không gian (Spatial Filter) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  | if abs(by - (y + h - 40)) < 30 and (abs(bx - (x - 35)) < 15 or abs(bx - (x + w + 4)) < 15): |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  | Đoạn điều kiện này giúp OpenCV xác định: "Đối tượng này có nằm đúng ở góc chân dưới bên trái hoặc bên phải của khung cửa hay không?" |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  | y + h: Là tọa độ đáy chân khung cửa. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  | abs(by - (y + h - 40)) < 30: Kiểm tra theo trục dọc \(Y\) xem vết cắt có nằm sát khu vực đáy chân cửa không (cho phép sai lệch trong khoảng 30 pixel). |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  | abs(bx - (x - 35)) < 15: Kiểm tra xem vết cắt có nằm sát chân khung bên TÁI hay không. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  | abs(bx - (x + w + 4)) < 15: Kiểm tra xem vết cắt có nằm sát chân khung bên PHẢI hay không. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  | 3. Điều kiện 2: Kiểm tra Kích thước vết cắt L-Notch (Size Filter) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  | if 20 <= bw <= 40 and 30 <= bh <= 50: |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  | Ý nghĩa: Tránh nhận nhầm các vết bẩn hoặc ký hiệu khác. Chỉ công nhận là vết cắt L-Notch nếu: |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  | Chiều rộng vết dập bw nằm trong khoảng từ 20 đến 40 pixel. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  | Chiều cao vết dập bh nằm trong khoảng từ 30 đến 50 pixel. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  | 4. Đánh dấu kết quả & Vẽ hình minh họa |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  | has_l_notch = True |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  | cv2.rectangle(annotated, (bx, by), (bx + bw, by + bh), (0, 0, 255), 2) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  | cv2.putText(annotated, "L-NOTCH", (bx - 10, by + bh + 15), |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |             cv2.FONT_HERSHEY_SIMPLEX, 0.45, (0, 0, 255), 1) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  | has_l_notch = True: Bật cờ xác nhận Bản vẽ CÓ chi tiết L-Notch (dùng để so sánh với biến req_l_notch trong DB Access sau này). |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  | cv2.rectangle(...): Khung một ô hình chữ nhật màu ĐỎ (0, 0, 255) xung quanh vết dập chữ L. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  | cv2.putText(...): In dòng chữ màu đỏ "L-NOTCH" ngay bên dưới chân khung cửa để nhân viên kiểm thử dễ dàng thấy vết dập trên ảnh báo cáo. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  | 💡 Tóm lại: Đoạn code này phối hợp giữa Vị trí (nằm ở đáy chân khung) + Kích thước (dạng ô chữ nhật nhỏ) để xác nhận bản vẽ có thiết kế vết cắt chân khung L-Shape hay không. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | # Khoanh khung cửa chính |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |         cv2.rectangle(annotated, (x, y), (x + w, y + h), (255, 0, 0), 3) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |         cv2.putText(annotated, f"FRAME SIZE: {measured_width}x{measured_height}mm", |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |                     (x, y - 12), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 0), 2) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  | Thêm khung xanh bao quanh cánh cửa và nội dung mô tả FRAME SIZE ở trên cánh cửa |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  # 2. Detect Lock Hole & Lever Handle Position (HoughCircles) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |     gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |     blurred = cv2.GaussianBlur(gray, (5, 5), 0) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |     circles = cv2.HoughCircles( |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |         blurred, |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |         cv2.HOUGH_GRADIENT, |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |         dp=1.2, |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |         minDist=50, |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |         param1=50, |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |         param2=22, |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |         minRadius=12, |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |         maxRadius=25 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |     ) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  | Dùng thuật toán Hough Circles để tìm lỗ tròn ổ khóa và tính độ cao tay khóa từ chân cửa lên. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  | 1. Tiền xử lý ảnh (Pre-processing) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  | cv2.cvtColor: Chuyển ảnh BGR sang ảnh xám (gray). |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  | cv2.GaussianBlur: Làm mờ nhẹ (5, 5) để xóa nhiễu li ti, giúp nhận diện đường tròn mượt hơn. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  | 2. Dò tìm hình tròn (cv2.HoughCircles) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  | Quét toàn bộ ảnh xám để tìm các hình tròn có bán kính trong khoảng 12 đến 25 pixel (minRadius=12, maxRadius=25). |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | if circles is not None and door_frame_cnt is not None: |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |         fx, fy, fw, fh = cv2.boundingRect(door_frame_cnt) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |         circles = np.uint16(np.round(circles)) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |         for c in circles[0, :]: |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |             cx, cy, r = c[0], c[1], c[2] |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |             if fx + fw - 100 <= cx <= fx + fw - 10 and fy + 200 <= cy <= fy + fh - 100: |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |                 lock_found = True |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |                 lock_dia_mm = round((r * 2) * SCALE_MM_PER_PX, 1) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |                 lock_y_from_bottom_mm = round((fy + fh - cy) * SCALE_MM_PER_PX, 1) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |                 cv2.circle(annotated, (cx, cy), r, (0, 160, 0), 3) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |                 cv2.circle(annotated, (cx, cy), 3, (0, 0, 255), -1) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |                 cv2.putText(annotated, f"LOCK HT: {lock_y_from_bottom_mm}mm", |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |                             (cx - 110, cy + 5), cv2.FONT_HERSHEY_SIMPLEX, 0.48, (0, 140, 0), 2) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  | 3. Lọc đúng vị trí ổ khóa & Tính độ cao (if ...) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  | Lọc vị trí: Chỉ nhận hình tròn có tâm cx nằm ở mép phải cánh cửa (fx + fw - 100 <= cx <= fx + fw - 10). |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  | Tính độ cao ổ khóa (mm): Lấy tọa độ chân khung cửa (fy + fh) trừ đi tọa độ tâm lỗ khóa (cy), |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  sau đó nhân với tỉ lệ đổi sang mm: \[\text{lock_y_from_bottom_mm} = ((\text{fy} + \text{fh}) - \text{cy}) \times 2.5\] |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  | 4. Vẽ đánh dấu trực quan lên ảnh |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  | cv2.circle: Vẽ vòng tròn xanh lá bao quanh lỗ khóa và chấm đỏ ở chính giữa tâm. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  | cv2.putText: In dòng chữ độ cao tay khóa đo được (ví dụ: LOCK HT: 1000mm) ngay cạnh ổ khóa. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | # 3. Detect Hinges Count along Left Edge |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |     hinge_count = 0 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |     if door_frame_cnt is not None: |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |         fx, fy, fw, fh = cv2.boundingRect(door_frame_cnt) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |         for cnt in contours: |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |             bx, by, bw, bh = cv2.boundingRect(cnt) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |             # Bản lề nằm ở lân cận mép trái fx - 25 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |             if abs(bx - (fx - 25)) < 10 and 15 <= bw <= 30 and 40 <= bh <= 60: |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |                 hinge_count += 1 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |                 cv2.rectangle(annotated, (bx, by), (bx + bw, by + bh), (255, 120, 0), 2) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |                 cv2.putText(annotated, "HINGE", (bx - 55, by + 30), cv2.FONT_HERSHEY_SIMPLEX, 0.45, (255, 120, 0), 1) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  | Đếm số lượng bản lề (Hinges) đính dọc theo mép khung đứng bên trái của cửa thép. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  | 1. Khởi tạo & Lấy tọa độ khung cửa |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  | hinge_count = 0 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  | if door_frame_cnt is not None: |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |     fx, fy, fw, fh = cv2.boundingRect(door_frame_cnt) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  | hinge_count = 0: Khởi tạo biến đếm số lượng bản lề ban đầu bằng 0. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  | fx: Tọa độ X mép trái của khung cửa chính. OpenCV sẽ dùng mốc fx này để giới hạn phạm vi tìm kiếm bản lề. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  | 2. Vòng lặp duyệt tìm đối tượng |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  | for cnt in contours: |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |     bx, by, bw, bh = cv2.boundingRect(cnt) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  | Duyệt qua từng đường viền cnt trên bản vẽ và lấy ra tọa độ (bx, by) cũng như chiều rộng bw, chiều cao bh của từng hình vẽ. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  | 3. Bộ lọc kép: Vị trí không gian + Kích thước hình học |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  | if abs(bx - (fx - 25)) < 10 and 15 <= bw <= 30 and 40 <= bh <= 60: |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  | Để không bị đếm nhầm các chi tiết khác trên bản vẽ, OpenCV áp dụng 2 điều kiện lọc nghiêm ngặt: |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  | Lọc Vị trí (Mép trái khung): abs(bx - (fx - 25)) < 10 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  | Bản lề luôn được bắt cố định ở lân cận mép trái khung cửa (nằm dịch ra ngoài khoảng 25 pixel so với mép fx). |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  | Đoạn code kiểm tra xem tọa độ bx của đối tượng có nằm đúng dải mép trái này hay không (cho phép sai lệch trong khoảng 10 pixel). |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  | Lọc Kích thước bản lề: 15 <= bw <= 30 and 40 <= bh <= 60 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  | Bản lề có dạng hình chữ nhật đứng nhỏ. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  | Chiều rộng bw phải từ 15 đến 30 pixel. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  | Chiều cao bh phải từ 40 đến 60 pixel. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  | 4. Tăng biến đếm & Đánh dấu trực quan |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  | hinge_count += 1 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  | cv2.rectangle(annotated, (bx, by), (bx + bw, by + bh), (255, 120, 0), 2) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  | cv2.putText(annotated, "HINGE", (bx - 55, by + 30), cv2.FONT_HERSHEY_SIMPLEX, 0.45, (255, 120, 0), 1) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  | Khi tìm thấy đối tượng thỏa mãn cả vị trí lẫn kích thước: |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  | hinge_count += 1: Tăng số lượng bản lề tìm được lên 1. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  | cv2.rectangle(...): Khoanh một ô hình chữ nhật màu CAM (255, 120, 0) xung quanh bản lề. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  | cv2.putText(...): In nhãn chữ màu cam "HINGE" ngay cạnh bản lề để kiểm thử viên dễ quan sát trên ảnh báo cáo. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  | 💡 Tóm lại: Đoạn code này tự động quét dọc mép trái cửa, đếm ra tổng số bản lề thực tế (3 hoặc 4 cái).  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  | Kết quả hinge_count này sau đó được đối chiếu trực tiếp với yêu cầu req_hinge_count trong file DB Access để báo MATCH (Đúng) hoặc MISMATCH (Sai). |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | Xuất ra kết quả ảnh khớp |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | Ảnh đầu ra sanwa_sd_result_SD-1_PASS.png |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
## Sheet: SteelDoor
| <<Overview |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | Mô tả hình ảnh cửa thép Sanwa |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | Cửa thép Sanwa (Steel Door SD-1 / 1LSD-24) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | Các bộ phận cốt lõi trên Cửa thép Sanwa (SD-1) & Vai trò xử lý OpenCV: |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | 1. Khung ngoại (Outer Frame): |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | Khái niệm: Hệ khung thép định hình bao ngoài cố định vào khuôn tường. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | OpenCV: Được phát hiện bằng findContours để đo chiều rộng khung (\(W\)) và chiều cao khung (\(H\)). |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | 2. Cánh cửa thép (Door Leaf): |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | Khái niệm: Tấm cánh cửa chính được dập bằng thép tấm gia cường. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | 3. Bản lề (Hinges): |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | Khái niệm: Các cụm bản lề thép bắt cố định dọc theo mép đứng bên trái của khung cửa. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | OpenCV: Thuật toán sẽ duyệt dọc theo mép trái khung (\(x_{left}\)) để kiểm tra và đếm số lượng bản lề thực tế (thường là 3 hoặc 4 bản lề). |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | 4. Tay nắm & Ổ khóa (Lever Handle & Lock): |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | Khái niệm: Cụm tay gạt cơ khí và lỗ khoét tròn để gắn ruột ổ khóa trên cánh cửa. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | OpenCV: Dùng thuật toán HoughCircles để dò chính xác tâm lỗ tròn \((cx, cy)\) và bán kính lỗ. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | 5. Độ cao ổ khóa (Lock Height - 1000mm): |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | Khái niệm: Khoảng cách thẳng đứng tính từ mặt sàn hoàn thiện (FFL / chân khung) lên tới tâm ổ khóa. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | OpenCV: Tính bằng công thức lock_height = (y_bottom - cy) * scale_mm. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | 6. Góc cắt L-Notch (L-Shape Notch Cutout): |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | Khái niệm: Vết dập cắt góc hình chữ L ở hai chân dưới của khung cửa để ôm sập âm vào sàn bê tông hoặc nẹp chân tường. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | OpenCV: Kiểm tra diện tích khuyết chữ nhật ở 2 góc đáy khung bằng boundingRect. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | 7. Hướng mở cửa (Door Swing Arc): |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | Khái niệm: Nét vẽ vòng cung đứt thể hiện bán kính quét mở cửa (mở vào / mở ra). |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | So sánh |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | Steel Door SD-1  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | Steel Door SD-1 / 1LSD-24 |
|  | Điểm đặc thù của mã 1LSD-24 so với SD-1: |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | 1. Ý nghĩa mã ký hiệu (1LSD-24): |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | 1LSD (1-Leaf Steel Door): Dòng cửa thép đơn 1 cánh. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | 24 (Chiều cao chuẩn 2400mm): Khác với dòng SD-1 thông thường (cao 2100mm), dòng 1LSD-24 là chuẩn cửa thép cao trần (High-ceiling Steel Door) có chiều cao phủ bì lên tới 2400 mm (rộng 850 mm - 900 mm). |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | 2. Cấu trúc kỹ thuật cần kiểm thử bằng OpenCV: |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | Đo chiều cao vượt chuẩn: Khung cửa cao hơn (2400mm) nên tỷ lệ pixel dọc sẽ lớn hơn, cần lưu ý dải lọc h trong boundingRect. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | Vị trí bản lề: Do cửa cao và nặng hơn, mã 1LSD-24 thực tế có thể bố trí 3 bản lề phân bổ đều hoặc 4 bản lề (2 bản lề phía trên để chịu lực xệ cánh). |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | Vết dập L-Notch chân khung: Giữ nguyên quy cách dập khuyết góc chữ L ở 2 bên chân khung để ôm sập vào mặt sàn hoàn thiện. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
## Sheet: BenchMark
| <<Overview |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | BenchMark |  |  |  |  |  |  |  |  |  |  |  |
|  | Một số thuật ngữ |  |  |  |  |  |  |  |  |  |  |  |
|  |  | Ground Truth |  |  |  |  |  |  |  |  |  |  |
|  |  | GT (Ground Truth) là đáp án đúng do con người gán nhãn, dùng làm chuẩn để chấm model. Ví dụ: ảnh này thật sự có 3 người đội mũ. |  |  |  |  |  |  |  |  |  |  |
|  |  | Positive / Negative: model nói "có" đối tượng thì là Positive, nói "không có" thì là Negative. Từ "True / False" cho biết model nói đúng hay sai. |  |  |  |  |  |  |  |  |  |  |
|  |  | Bốn ô cơ bản |  |  |  |  |  |  |  |  |  |  |
|  |  | Thuật ngữ |  |  | Ý nghĩa |  |  |  |  |  |  | Ví dụ |
|  |  | TP (True Positive) |  |  | Model báo có và thật sự có |  |  |  |  |  |  | Model thấy mũ, GT cũng có mũ |
|  |  | FP (False Positive) |  |  | Model báo có nhưng thực tế không có (báo nhầm, đếm thừa) |  |  |  |  |  |  | Model coi cái xô màu vàng là mũ |
|  |  | FN (False Negative) |  |  | Thực tế có nhưng model bỏ sót (đếm thiếu) |  |  |  |  |  |  | Có mũ nhưng model không thấy |
|  |  | TN (True Negative) |  |  | Model báo không có và thực tế cũng không có |  |  |  |  |  |  | Ảnh không có mũ, model không báo gì |
|  |  | TN thường bị bỏ qua trong bài toán detect/đếm, vì "những thứ không phải mũ" là vô hạn nên không đếm được. Đó là lý do cột TN trong file của bạn để N/A. |  |  |  |  |  |  |  |  |  |  |
|  |  | Các chỉ số tính từ TP/FP/FN/TN |  |  |  |  |  |  |  |  |  |  |
|  |  | Precision (P) = TP / (TP + FP). Trong số những cái model báo có, bao nhiêu phần trăm đúng. Precision thấp nghĩa là báo nhầm nhiều. |  |  |  |  |  |  |  |  |  |  |
|  |  | Recall (R) = TP / (TP + FN). Trong số những cái thật sự có, model tìm ra được bao nhiêu phần trăm. Recall thấp nghĩa là bỏ sót nhiều. |  |  |  |  |  |  |  |  |  |  |
|  |  | F1-Score = 2·P·R / (P + R). Trung bình điều hòa của P và R, gộp hai chỉ số thành một con số. Chỉ cao khi cả P và R đều cao. Nếu P=1.0 mà R=0.1 thì F1 chỉ khoảng 0.18. |  |  |  |  |  |  |  |  |  |  |
|  |  | Accuracy (A) = (TP + TN) / (TP + TN + FP + FN). Tỉ lệ dự đoán đúng trên tổng số. Chỉ số này ít dùng cho detect vì cần TN và dễ gây hiểu lầm khi dữ liệu mất cân bằng. Bạn không cần dùng nó trong benchmark này. |  |  |  |  |  |  |  |  |  |  |
|  |  | Ví dụ: GT có 10 mũ, model báo 8 cái, trong đó 7 đúng và 1 sai. Khi đó TP=7, FP=1, FN=3, nên P=7/8=0.875, R=7/10=0.7, F1≈0.78. |  |  |  |  |  |  |  |  |  |  |
|  |  | Các khái niệm khác |  |  |  |  |  |  |  |  |  |  |
|  |  | Threshold (ngưỡng chấp nhận): model trả về mỗi detection kèm điểm tin cậy (confidence, từ 0 đến 1). Threshold là mức tối thiểu để chấp nhận detection đó. |  |  |  |  |  |  |  |  |  |  |
|  |  | Threshold cao (0.7) thì model chắc chắn hơn: Precision tăng, Recall giảm. |  |  |  |  |  |  |  |  |  |  |
|  |  | Threshold thấp (0.2) thì model dễ dãi hơn: Recall tăng, Precision giảm. |  |  |  |  |  |  |  |  |  |  |
|  |  | Vì vậy cần cố định một threshold thống nhất khi so sánh các model. |  |  |  |  |  |  |  |  |  |  |
|  |  | Confusion matrix (ma trận nhầm lẫn): bảng thể hiện model dự đoán gì so với thực tế. Với bài toán 2 lớp, đây chính là bảng 2×2 gồm TP, FP, FN, TN. Với nhiều class, mỗi hàng là class thật và mỗi cột là class model dự đoán. Nhìn vào đó bạn thấy được model hay nhầm class nào với class nào (ví dụ nhầm machinery với forklift). |  |  |  |  |  |  |  |  |  |  |
|  |  | IoU (Intersection over Union): đo độ trùng lặp giữa box dự đoán và box GT, bằng diện tích phần giao chia cho diện tích phần hợp. Giá trị từ 0 (không trùng) đến 1 (trùng khít). Thường coi detection là đúng khi IoU ≥ 0.5. |  |  |  |  |  |  |  |  |  |  |
|  |  | mAP (mean Average Precision): chỉ số chuẩn cho object detection. Với mỗi class, vẽ đường cong Precision–Recall khi thay đổi threshold, lấy diện tích dưới đường cong (AP), rồi lấy trung bình trên các class (mAP). mAP@0.5 dùng IoU 0.5 để xác định đúng/sai, còn mAP@0.5:0.95 lấy trung bình trên nhiều mức IoU và khắt khe hơn. |  |  |  |  |  |  |  |  |  |  |
|  |  | Áp dụng vào dự án của bạn |  |  |  |  |  |  |  |  |  |  |
|  |  | Bạn dùng: GT, TP, FP, FN, Precision, Recall, F1, threshold (cho YOLO). |  |  |  |  |  |  |  |  |  |  |
|  |  | Bạn không cần: IoU và mAP, vì yêu cầu là chỉ cần phát hiện đúng và đủ số lượng, không cần box chính xác. Hơn nữa VLM thường không trả box tốt nên cũng không thể tính mAP công bằng cho cả bốn nhóm model. |  |  |  |  |  |  |  |  |  |  |
|  |  | Cần biết để đọc tài liệu: IoU và mAP xuất hiện rất nhiều trong paper và tài liệu YOLO, nên hiểu khái niệm sẽ giúp bạn đọc hiểu, và có thể báo cáo thêm cho YOLO nếu khách yêu cầu. |  |  |  |  |  |  |  |  |  |  |
|  |  | Run app |  |  |  |  |  |  |  |  |  |  |
|  |  | PS C:\work\Projects\Nozawa\03.GIT\src> python -m venv venv |  |  |  |  |  |  |  |  |  |  |
|  |  | PS C:\work\Projects\Nozawa\03.GIT\src> venv/scripts/activate |  |  |  |  |  |  |  |  |  |  |
|  |  | (venv) PS C:\work\Projects\Nozawa\03.GIT\src> pip install -r requirements.txt |  |  |  |  |  |  |  |  |  |  |
|  |  | (venv) PS C:\work\Projects\Nozawa\03.GIT\src> py .\run_infer.py |  |  |  |  |  |  |  |  |  |  |
|  |  | requirements: Ultralytics requirement ['git+https://github.com/ultralytics/CLIP.git'] not found, attempting AutoUpdate... |  |  |  |  |  |  |  |  |  |  |
|  |  | Using Python 3.14.2 environment at: venv |  |  |  |  |  |  |  |  |  |  |
|  |  | requirements: Ultralytics requirement ['git+https://github.com/ultralytics/CLIP.git'] not found, attempting AutoUpdate... |  |  |  |  |  |  |  |  |  |  |
|  |  | Using Python 3.14.2 environment at: venv |  |  |  |  |  |  |  |  |  |  |
|  |  | Resolved 19 packages in 2.11s |  |  |  |  |  |  |  |  |  |  |
|  |  |    Updating https://github.com/ultralytics/CLIP.git (HEAD) |  |  |  |  |  |  |  |  |  |  |
|  |  | Resolved 19 packages in 2.11s |  |  |  |  |  |  |  |  |  |  |
|  |  | (venv) PS C:\work\Projects\Nozawa\03.GIT\src> python evaluate.py |  |  |  |  |  |  |  |  |  |  |
|  |  | Cách dùng: py evaluate.py "đường\dẫn\ground_truth.xlsx" [tên_site] |  |  |  |  |  |  |  |  |  |  |
|  |  | (venv) PS C:\work\Projects\Nozawa\03.GIT\src> python evaluate.py output\groundtruth\GroundTruth1.xlsx Sheet1 |  |  |  |  |  |  |  |  |  |  |
|  |  | [GT] 23 dòng, 25 cột (A..Z, không có J) |  |  |  |  |  |  |  |  |  |  |
|  |  | [ok] yolo26: 10 variant |  |  |  |  |  |  |  |  |  |  |
|  |  | [ok] yoloe26: 10 variant |  |  |  |  |  |  |  |  |  |  |
|  |  | Saved C:\work\Projects\Nozawa\03.GIT\src\output\metrics.xlsx |  |  |  |  |  |  |  |  |  |  |
|  |  | (venv) PS C:\work\Projects\Nozawa\03.GIT\src> python evaluate.py ..\groundtruth\GroundTruth1.xlsx Sheet1     |  |  |  |  |  |  |  |  |  |  |
|  |  | (venv) PS C:\work\Projects\Nozawa\03.GIT\src> py .\run_infer.py |  |  |  |  |  |  |  |  |  |  |
|  |  | (venv) PS C:\work\Projects\Nozawa\03.GIT\src> python evaluate.py |  |  |  |  |  |  |  |  |  |  |
|  |  | YOLO là gì |  |  |  |  |  |  |  |  |  |  |
|  |  | YOLO (You Only Look Once) là họ model nhận diện đối tượng (object detection). Bạn đưa vào một ảnh, model trả về danh sách những gì nó thấy: loại đối tượng (người, mũ, xe nâng...), vị trí (box) và độ tự tin (confidence). |  |  |  |  |  |  |  |  |  |  |
|  |  | Cái tên "chỉ nhìn một lần" nghĩa là model xử lý cả ảnh trong một lượt, nên rất nhanh (trong file của bạn, Yolov26 chỉ khoảng 28ms mỗi ảnh). Vì nhanh và nhẹ nên YOLO hay được dùng cho camera giám sát, xe tự lái, xử lý video thời gian thực. |  |  |  |  |  |  |  |  |  |  |
|  |  | Cách hoạt động ở mức đơn giản: |  |  |  |  |  |  |  |  |  |  |
|  |  | 1. Ảnh được resize về kích thước cố định (thường 640×640). |  |  |  |  |  |  |  |  |  |  |
|  |  | 2. Model quét ảnh và đề xuất các box cùng nhãn. |  |  |  |  |  |  |  |  |  |  |
|  |  | 3. Các box trùng nhau được loại bớt (bước NMS). |  |  |  |  |  |  |  |  |  |  |
|  |  | 4. Kết quả: ví dụ person 0.92, helmet 0.85, forklift 0.78. |  |  |  |  |  |  |  |  |  |  |
|  |  | Điểm cần nhớ: |  |  |  |  |  |  |  |  |  |  |
|  |  | YOLO thường chỉ nhận diện những class nó đã được học (ví dụ COCO có person nhưng không có helmet hay forklift). Muốn thêm class thì phải huấn luyện (fine-tune) bằng ảnh có gán nhãn. |  |  |  |  |  |  |  |  |  |  |
|  |  | YOLOE là biến thể cho phép bạn gõ tên class bằng chữ (text prompt), nên nhận diện được class mới mà không cần train. |  |  |  |  |  |  |  |  |  |  |
|  |  | SAHI là gì |  |  |  |  |  |  |  |  |  |  |
|  |  | SAHI (Slicing Aided Hyper Inference) không phải là một model. Nó là một kỹ thuật bổ trợ đứng trước YOLO để giúp tìm vật nhỏ tốt hơn. |  |  |  |  |  |  |  |  |  |  |
|  |  | Vấn đề: ảnh camera thường rất lớn (ví dụ 4000×3000), nhưng YOLO resize về 640×640. Người ở xa hoặc cái mũ nhỏ sẽ co lại chỉ còn vài pixel và model không thấy được. |  |  |  |  |  |  |  |  |  |  |
|  |  | Cách SAHI giải quyết: cắt ảnh lớn thành nhiều mảnh nhỏ (có phần chồng lấn nhau), cho YOLO chạy trên từng mảnh, rồi ghép kết quả về ảnh gốc và loại các box trùng. |  |  |  |  |  |  |  |  |  |  |
|  |  | Ví dụ so sánh: nhìn cả tấm bản đồ lớn thì khó thấy các điểm nhỏ, nhưng chia bản đồ thành nhiều ô và xem kỹ từng ô thì thấy rõ hơn. |  |  |  |  |  |  |  |  |  |  |
|  |  | So sánh nhanh |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  | YOLO |  |  |  | SAHI |  |  |  |  |
|  |  | Bản chất |  | Model nhận diện |  |  |  | Kỹ thuật cắt ảnh, dùng kèm YOLO |  |  |  |  |
|  |  | Làm gì |  | Tìm đối tượng trong ảnh |  |  |  | Giúp YOLO tìm được vật nhỏ |  |  |  |  |
|  |  | Tốc độ |  | Nhanh |  |  |  | Chậm hơn (chạy YOLO nhiều lần mỗi ảnh) |  |  |  |  |
|  |  | Ưu điểm |  | Nhẹ, real-time |  |  |  | Tăng Recall cho vật nhỏ |  |  |  |  |
|  |  | Nhược điểm |  | Bỏ sót vật nhỏ |  |  |  | Dễ đếm trùng, tốn thời gian |  |  |  |  |
|  |  | Vậy "YOLO + SAHI" nghĩa là: dùng YOLO làm bộ nhận diện, và thêm SAHI để cắt ảnh trước khi đưa vào. |  |  |  |  |  |  |  |  |  |  |
|  |  | 1. CUDA là gì? |  |  |  |  |  |  |  |  |  |  |
|  |  | - **CUDA** (*Compute Unified Device Architecture*) là nền tảng tính toán song song độc quyền do hãng **NVIDIA** phát triển. |  |  |  |  |  |  |  |  |  |  |
|  |  | - Bình thường, CPU chỉ có từ 4 đến 32 nhân (cores) xử lý tuần tự. Trong khi đó, GPU NVIDIA có hàng ngàn nhân tính toán nhỏ chuyên biệt. Vì các mô hình Deep Learning (như YOLO) bản chất là hàng triệu phép tính nhân ma trận song song, việc chạy trên GPU thông qua CUDA sẽ **nhanh hơn gấp từ 5 đến 50 lần** so với chạy CPU. |  |  |  |  |  |  |  |  |  |  |
|  |  | --- |  |  |  |  |  |  |  |  |  |  |
|  |  | ### 2. Mode `cuda` trong [`run_infer.py`](file:///c:/work/Projects/Nozawa/03.GIT/src/run_infer.py) hoạt động thế nào? |  |  |  |  |  |  |  |  |  |  |
|  |  | Tại dòng [702](file:///c:/work/Projects/Nozawa/03.GIT/src/run_infer.py#L702): |  |  |  |  |  |  |  |  |  |  |
|  |  | ```python |  |  |  |  |  |  |  |  |  |  |
|  |  | device="cuda" if torch.cuda.is_available() else "cpu" |  |  |  |  |  |  |  |  |  |  |
|  |  | ``` |  |  |  |  |  |  |  |  |  |  |
|  |  | - **Nếu máy bạn có GPU NVIDIA hỗ trợ và đã cài đặt đúng PyTorch CUDA**: Chương trình sẽ dùng mode `"cuda"`, đẩy dữ liệu ảnh và trọng số model lên bộ nhớ VRAM của GPU để suy luận (inference) cực nhanh. |  |  |  |  |  |  |  |  |  |  |
|  |  | - **Nếu không có**: Chương trình tự động hạ cấp xuống mode `"cpu"`, tốc độ sẽ chậm hơn đáng kể. |  |  |  |  |  |  |  |  |  |  |
|  |  | --- |  |  |  |  |  |  |  |  |  |  |
|  |  | ### 3. Tại sao trong code có hàm [`sync()`](file:///c:/work/Projects/Nozawa/03.GIT/src/run_infer.py#L567-L571) ở dòng 567? |  |  |  |  |  |  |  |  |  |  |
|  |  | ```python |  |  |  |  |  |  |  |  |  |  |
|  |  | def sync(): |  |  |  |  |  |  |  |  |  |  |
|  |  |     """Chờ GPU xong việc để đo thời gian chính xác (không làm gì nếu chạy CPU).""" |  |  |  |  |  |  |  |  |  |  |
|  |  |     if torch.cuda.is_available(): |  |  |  |  |  |  |  |  |  |  |
|  |  |         torch.cuda.synchronize() |  |  |  |  |  |  |  |  |  |  |
|  |  | ``` |  |  |  |  |  |  |  |  |  |  |
|  |  | - Khi ở mode `cuda`, việc tính toán trên GPU diễn ra **bất đồng bộ (asynchronous)**: CPU ném tác vụ xử lý cho GPU xong sẽ chạy tiếp ngay lệnh Python phía sau mà không đợi GPU tính xong. |  |  |  |  |  |  |  |  |  |  |
|  |  | - Lệnh `torch.cuda.synchronize()` bắt chương trình phải **đợi GPU xử lý xong hoàn toàn** rồi mới bấm giờ dừng `time.perf_counter()`. Nhờ đó, chỉ số thời gian suy luận (ms/ảnh, FPS) trong bảng benchmark xuất ra mới chính xác. |  |  |  |  |  |  |  |  |  |  |
|  |  | --- |  |  |  |  |  |  |  |  |  |  |
|  |  | ### 4. Điều kiện để máy kích hoạt được mode `cuda` |  |  |  |  |  |  |  |  |  |  |
|  |  | 1. Máy tính có trang bị card đồ họa rời của **NVIDIA** (ví dụ RTX 3060, RTX 4070, GTX 1650,...; card AMD hay Intel không dùng CUDA). |  |  |  |  |  |  |  |  |  |  |
|  |  | 2. Đã cài đặt **NVIDIA Driver**. |  |  |  |  |  |  |  |  |  |  |
|  |  | 3. Thư viện `torch` trong môi trường ảo (virtualenv) phải là phiên bản build cùng CUDA (ví dụ `cu118`, `cu121` hoặc `cu124`). Bạn có thể kiểm tra nhanh bằng lệnh: |  |  |  |  |  |  |  |  |  |  |
|  |  |    ```python |  |  |  |  |  |  |  |  |  |  |
|  |  |    import torch |  |  |  |  |  |  |  |  |  |  |
|  |  |    print(torch.cuda.is_available())  # True = đã nhận CUDA |  |  |  |  |  |  |  |  |  |  |
|  |  |    ``` |  |  |  |  |  |  |  |  |  |  |
|  |  | VARIANT |  |  |  |  |  |  |  |  |  |  |
|  |  | Trong Deep Learning và cụ thể trong file [`run_infer.py`](file:///c:/work/Projects/Nozawa/03.GIT/src/run_infer.py), **variant** có nghĩa là **biến thể (phiên bản kích cỡ/quy mô)** khác nhau của cùng một dòng mô hình. |  |  |  |  |  |  |  |  |  |  |
|  |  | --- |  |  |  |  |  |  |  |  |  |  |
|  |  | ### 1. Các `variant` trong dự án của bạn |  |  |  |  |  |  |  |  |  |  |
|  |  | Được định nghĩa tại biến [`MODELS`](file:///c:/work/Projects/Nozawa/03.GIT/src/run_infer.py#L40-L49) (dòng 40–49): |  |  |  |  |  |  |  |  |  |  |
|  |  | ```python |  |  |  |  |  |  |  |  |  |  |
|  |  | MODELS = { |  |  |  |  |  |  |  |  |  |  |
|  |  |     "yolo26": ["yolo26n", "yolo26s", "yolo26m", "yolo26l", "yolo26x"], |  |  |  |  |  |  |  |  |  |  |
|  |  |     "yoloe26": [ |  |  |  |  |  |  |  |  |  |  |
|  |  |         "yoloe-26n-seg", |  |  |  |  |  |  |  |  |  |  |
|  |  |         "yoloe-26s-seg", |  |  |  |  |  |  |  |  |  |  |
|  |  |         "yoloe-26m-seg", |  |  |  |  |  |  |  |  |  |  |
|  |  |         "yoloe-26l-seg", |  |  |  |  |  |  |  |  |  |  |
|  |  |         "yoloe-26x-seg", |  |  |  |  |  |  |  |  |  |  |
|  |  |     ], |  |  |  |  |  |  |  |  |  |  |
|  |  | } |  |  |  |  |  |  |  |  |  |  |
|  |  | ``` |  |  |  |  |  |  |  |  |  |  |
|  |  | Ở đây: |  |  |  |  |  |  |  |  |  |  |
|  |  | - **Model Type (`mt`)**: Là dòng kiến trúc gốc (ví dụ: `yolo26` hoặc `yoloe26`). |  |  |  |  |  |  |  |  |  |  |
|  |  | - **Variant (`v`)**: Là các phiên bản cụ thể dựa trên quy ước chữ cái đuôi: **n, s, m, l, x**. |  |  |  |  |  |  |  |  |  |  |
|  |  | --- |  |  |  |  |  |  |  |  |  |  |
|  |  | ### 2. Ý nghĩa các kích cỡ variant (từ nhỏ đến lớn) |  |  |  |  |  |  |  |  |  |  |
|  |  | | Ký tự | Tên đầy đủ | Đặc điểm chính | Phù hợp với | |  |  |  |  |  |  |  |  |  |  |
|  |  | | :--- | :--- | :--- | :--- | |  |  |  |  |  |  |  |  |  |  |
|  |  | | **n** | **Nano** | Số lượng tham số ít nhất, siêu nhẹ, chạy nhanh nhất, tốn ít RAM/VRAM nhất, nhưng độ chính xác (accuracy) thấp nhất. | Thiết bị nhúng, camera IoT, CPU yếu. | |  |  |  |  |  |  |  |  |  |  |
|  |  | | **s** | **Small** | Nhỏ, tốc độ cao, độ chính xác ở mức vừa phải. | Ứng dụng real-time trên máy tính thông thường. | |  |  |  |  |  |  |  |  |  |  |
|  |  | | **m** | **Medium** | Cỡ vừa, cân bằng rất tốt giữa tốc độ và độ chính xác. | Đa số các ứng dụng thực tế. | |  |  |  |  |  |  |  |  |  |  |
|  |  | | **l** | **Large** | Cỡ lớn, mô hình sâu hơn, nhận diện chính xác cao nhưng chạy nặng và chậm hơn. | Cần GPU đủ mạnh, ưu tiên độ chuẩn xác. | |  |  |  |  |  |  |  |  |  |  |
|  |  | | **x** | **Extra Large** | Lớn nhất, nhiều tham số nhất, nhận diện chính xác nhất nhưng nặng nhất và tốn nhiều VRAM nhất. | Server GPU khủng, không quá khắt khe về FPS. | |  |  |  |  |  |  |  |  |  |  |
|  |  | *(Hậu tố `-seg` trong `yoloe-26*-seg` biểu thị biến thể hỗ trợ cả tác vụ Instance Segmentation - phân vùng điểm ảnh, bên cạnh Bounding Box).* |  |  |  |  |  |  |  |  |  |  |
|  |  | --- |  |  |  |  |  |  |  |  |  |  |
|  |  | ### 3. Tại sao trong code lại duyệt qua từng variant? |  |  |  |  |  |  |  |  |  |  |
|  |  | Tại dòng [745](file:///c:/work/Projects/Nozawa/03.GIT/src/run_infer.py#L745): |  |  |  |  |  |  |  |  |  |  |
|  |  | ```python |  |  |  |  |  |  |  |  |  |  |
|  |  | for v in variants: |  |  |  |  |  |  |  |  |  |  |
|  |  |     ... |  |  |  |  |  |  |  |  |  |  |
|  |  |     d, i, st = run_variant(mt, v, sahi) |  |  |  |  |  |  |  |  |  |  |
|  |  | ``` |  |  |  |  |  |  |  |  |  |  |
|  |  | Chương trình duyệt qua lần lượt từng variant để **chạy thử nghiệm và đo đạc (benchmark)**: |  |  |  |  |  |  |  |  |  |  |
|  |  | - So sánh thời gian xử lý (`time_ms`, `fps`). |  |  |  |  |  |  |  |  |  |  |
|  |  | . So sánh chất lượng nhận diện trên tập ảnh thực tế. |  |  |  |  |  |  |  |  |  |  |
|  |  | . giúp bạn chọn ra biến thể tối ưu nhất (đủ nhanh nhưng vẫn đủ chính xác) trước Khi quyết định đưa vào triển khai thực tế. |  |  |  |  |  |  |  |  |  |  |
|  |  | YOLO, YOLOE |  |  |  |  |  |  |  |  |  |  |
|  |  | Khi so sánh (trong báo cáo, tài liệu hay đặt tên biến trong code), bạn **nên dùng cặp: `YOLO` và `YOLOE`** (hoặc `YOLO26` và `YOLOE26`), **không nên dùng `yolov` và `yoloe`**. |  |  |  |  |  |  |  |  |  |  |
|  |  | Lý do chi tiết như sau: |  |  |  |  |  |  |  |  |  |  |
|  |  | --- |  |  |  |  |  |  |  |  |  |  |
|  |  | ### 1. Về mặt ngữ nghĩa và quy ước đặt tên |  |  |  |  |  |  |  |  |  |  |
|  |  | - **YOLO** (*You Only Look Once*): Là tên của cả dòng kiến trúc chuẩn. |  |  |  |  |  |  |  |  |  |  |
|  |  | - **YOLOE**: Chữ **E** viết hoa là một phần của tên model (*Enhanced / Open-Vocabulary YOLO* do Ultralytics phát triển, hỗ trợ Text/Visual Prompt và Segmentation). |  |  |  |  |  |  |  |  |  |  |
|  |  | - **Chữ `v` trong `YOLOv`**: Thực chất là viết tắt của **Version** (phiên bản). Nó chỉ có ý nghĩa khi **đi kèm với một con số cụ thể** phía sau (như `YOLOv8`, `YOLOv10`, `YOLOv26`).  |  |  |  |  |  |  |  |  |  |  |
|  |  |   > ❌ Nếu viết trơ trọi **`yolov` vs `yoloe`**: Sẽ bị khập khiễng vì một bên là viết tắt của từ "version", một bên là tên riêng của kiến trúc.   |  |  |  |  |  |  |  |  |  |  |
|  |  |   >  Nếu viết **`YOLO` vs `YOLOE`**: Đây là sự đối chiếu chuẩn xác giữa 2 kiến trúc (kiến trúc YOLO truyền thống vs kiến trúc YOLOE mở rộng). |  |  |  |  |  |  |  |  |  |  |
|  |  | --- |  |  |  |  |  |  |  |  |  |  |
|  |  | ### 2. Hai cách gọi chuẩn tùy theo ngữ cảnh |  |  |  |  |  |  |  |  |  |  |
|  |  | #### Cách 1: So sánh tổng quát về mặt phương pháp / kiến trúc |  |  |  |  |  |  |  |  |  |  |
|  |  | > **Nên dùng: `YOLO` vs `YOLOE`** |  |  |  |  |  |  |  |  |  |  |
|  |  | - Đây cũng chính là 2 class gốc mà bạn đang import trực tiếp từ thư viện Ultralytics trong file [`run_infer.py`](file:///c:/work/Projects/Nozawa/03.GIT/src/run_infer.py#L5): |  |  |  |  |  |  |  |  |  |  |
|  |  |   ```python |  |  |  |  |  |  |  |  |  |  |
|  |  |   from ultralytics import YOLO, YOLOE |  |  |  |  |  |  |  |  |  |  |
|  |  |   ``` |  |  |  |  |  |  |  |  |  |  |
|  |  | #### Cách 2: So sánh cụ thể theo phiên bản trong dự án của bạn |  |  |  |  |  |  |  |  |  |  |
|  |  | Nếu gắn với phiên bản `26` đang có trong code, bạn có thể chọn 1 trong 2 chuẩn đồng bộ sau: |  |  |  |  |  |  |  |  |  |  |
|  |  | - **Chuẩn Ultralytics hiện đại (khuyên dùng):** `YOLO26` vs `YOLOE26` *(Từ phiên bản YOLO11, Ultralytics đã lược bỏ chữ `v`)*. |  |  |  |  |  |  |  |  |  |  |
|  |  | - **Chuẩn truyền thống:** `YOLOv26` vs `YOLOE-26`. |  |  |  |  |  |  |  |  |  |  |
|  |  | --- |  |  |  |  |  |  |  |  |  |  |
|  |  | ### 3. Sự khác biệt cốt lõi giữa 2 mô hình trong bài toán của bạn |  |  |  |  |  |  |  |  |  |  |
|  |  | Khi trình bày báo cáo hoặc so sánh kết quả benchmark, bạn có thể tóm tắt sự khác biệt giữa chúng như sau: |  |  |  |  |  |  |  |  |  |  |
|  |  | | Tiêu chí | YOLO (ví dụ `yolo26`) | YOLOE (ví dụ `yoloe-26*-seg`) | |  |  |  |  |  |  |  |  |  |  |
|  |  | | :--- | :--- | :--- | |  |  |  |  |  |  |  |  |  |  |
|  |  | | **Bản chất mô hình** | **Closed-set Object Detection** (Tập nhãn cố định theo COCO 80 lớp). | **Open-vocabulary / Prompt-based** (Nhận diện theo prompt văn bản tùy ý). | |  |  |  |  |  |  |  |  |  |  |
|  |  | | **Cách dùng trong code** | Chỉ dùng để nhận diện người: `classes=[0]` (`person`). | Dùng `set_classes(PROMPTS)` để bắt được nhiều class đặc thù: xe nâng (`forklift`), khẩu trang, mũ bảo hộ, vạch kẻ sàn... | |  |  |  |  |  |  |  |  |  |  |
|  |  | | **Đầu ra (Output)** | Chỉ xuất **Bounding Box** (hộp chữ nhật). | Hỗ trợ cả **Bounding Box** và **Segmentation Mask** (vùng bao điểm ảnh chi tiết). | |  |  |  |  |  |  |  |  |  |  |
|  |  | --- |  |  |  |  |  |  |  |  |  |  |
|  |  | > [!TIP] |  |  |  |  |  |  |  |  |  |  |
|  |  | > **Điểm cần lưu ý trong code hiện tại:** |  |  |  |  |  |  |  |  |  |  |
|  |  | > Trong file [`run_infer.py`](file:///c:/work/Projects/Nozawa/03.GIT/src/run_infer.py#L40-L55), thư mục lưu trữ đang đặt là `yolov26_variants` (có chữ `v`), nhưng key và tên file lại đặt là `yolo26` (không có `v`). Bạn nên thống nhất lại một cách gọi (ví dụ đồng bộ dùng `yolo26` hoặc `yolov26`) để code và đường dẫn thư mục luôn nhất quán. |  |  |  |  |  |  |  |  |  |  |
## Sheet: GroundTruth
| <<Overview |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | Giải thích các chỉ số đánh giá mô hình: GT, TP, FP, TN, FN, P, R, F1, Acc |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | Ví dụ 1 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | Nhận diện "person" trong ảnh camera nhà máy |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | Bạn có 10 bức ảnh từ camera. Nhiệm vụ của model YOLO là phát hiện: ảnh này có người (person) hay không? |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | Con người xem và gán nhãn (Ground Truth): |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | Tổng 10 ảnh |  |  |  |  |  |  |  |
|  | 6 ảnh CÓ người |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 6 ảnh có người |  |  |  |  |  |  |  |
|  | 4 ảnh KHÔNG có người (ảnh trống, chỉ có máy móc, xe nâng...) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 4 ảnh không có người |  |  |  |  |  |  |  |
|  | Model YOLO dự đoán: |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | Ảnh | Thực tế (GT) |  |  |  | Model đoán |  |  | Kết quả |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | 1 | 👷 Có người |  |  |  | ✅ "Có person" |  |  | TP ✔️ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | 2 | 👷 Có người |  |  |  | ✅ "Có person" |  |  | TP ✔️ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | 3 | 👷 Có người |  |  |  | ✅ "Có person" |  |  | TP ✔️ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | 4 | 👷 Có người |  |  |  | ✅ "Có person" |  |  | TP ✔️ |  |  |  |  |  |  |  |  |  | Model đoán có người và đúng |  |  |  |  |  |  |  |
|  | 5 | 👷 Có người |  |  |  | ❌ "Không có person" |  |  | FN 😱 |  |  |  |  |  |  |  |  |  | Model đoán không có người, và sai |  |  |  |  |  |  |  |
|  | 6 | 👷 Có người |  |  |  | ❌ "Không có person" |  |  | FN 😱 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | 7 | 🏭 Không có người |  |  |  | ✅ "Không có person" |  |  | TN ✔️ |  |  |  |  |  |  |  |  |  | Model đoán không có người, và đúng |  |  |  |  |  |  |  |
|  | 8 | 🏭 Không có người |  |  |  | ✅ "Không có person" |  |  | TN ✔️ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | 9 | 🏭 Không có người |  |  |  | ✅ "Không có person" |  |  | TN ✔️ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | 10 | 🏭 Không có người |  |  |  | ❌ "Có person" |  |  | FP 😤 |  |  |  |  |  |  |  |  |  | Model đoán có người, và sai |  |  |  |  |  |  |  |
|  | Ảnh 10: Model nhìn thấy cái áo treo trên giá, tưởng là người → báo nhầm. Ảnh 5, 6: Người đứng xa camera hoặc bị che khuất → model không thấy, bỏ sót. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | 1. GT — Ground Truth (Nhãn chuẩn) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | Nghĩa: Đáp án đúng do con người xem ảnh và gán nhãn bằng tay. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | Trong ví dụ: Con người xem 10 ảnh và xác nhận: |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | Ảnh 1–6: CÓ person (6 ảnh) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | Ảnh 7–10: KHÔNG có person (4 ảnh) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | [!IMPORTANT] GT không phải chỉ số đánh giá, mà là đáp án chuẩn để so sánh với kết quả của model. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | 2. Bộ 4 kết quả: TP, FP, TN, FN |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | Mỗi ảnh khi so GT với kết quả model sẽ rơi vào đúng 1 trong 4 ô: |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |                         Thực tế (GT) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |                    CÓ person       KHÔNG có person |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | TP | FP | TN | FN |  |  |  |
|  |  |                 ┌────────────────┬────────────────┐ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 4 | 1 | 3 | 2 |  |  |  |
|  |  |   Model    CÓ   │   TP = 4 ảnh   │   FP = 1 ảnh   │ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |   đoán          ├────────────────┼────────────────┤ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |            KHÔNG│   FN = 2 ảnh   │   TN = 3 ảnh   │ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |                 └────────────────┴────────────────┘ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | TP — True Positive (Đúng mà đúng) = 4 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | TP: Model báo có mà đúng |  |  |  |  |  |  |  |
|  | Model đoán "Có person" → Thực tế đúng là có người. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | Ảnh 1, 2, 3, 4: Có người đi lại trong khung hình, model phát hiện ra → ✔️ Đúng! |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | FP — False Positive (Sai mà báo có) = 1 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | FP: model báo có mà sai |  |  |  |  |  |  |  |
|  | Model đoán "Có person" → Thực tế không có người. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | Ảnh 10: Chỉ có cái áo treo trên giá, model nhầm tưởng là người → 😤 Báo nhầm! |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | TN — True Negative (Đúng mà đúng không) = 3 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | TN: Model báo không có mà đúng |  |  |  |  |  |  |  |
|  | Model đoán "Không có person" → Thực tế đúng là không có người. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | Ảnh 7, 8, 9: Ảnh chỉ có máy móc, xe nâng, model đúng khi nói "không có ai" → ✔️ Đúng! |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | FN — False Negative (Sai mà bỏ sót) = 2 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | FN: model báo không có mà sai |  |  |  |  |  |  |  |
|  | Model đoán "Không có person" → Thực tế có người nhưng model bỏ sót. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | Ảnh 5: Người đứng xa camera, hình quá nhỏ → model không nhận ra. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | Ảnh 6: Người bị xe nâng che khuất một nửa → model bỏ qua. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | [!TIP] Mẹo nhớ nhanh: |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | Chữ đầu T (True) / F (False) = Model đoán Đúng hay Sai |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | T/F: đoán đúng hay sai |  |  |  |  |  |  |  |
|  | Chữ sau P (Positive) / N (Negative) = Model đoán "CÓ" hay "KHÔNG" |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | P/N: model báo có/không |  |  |  |  |  |  |  |
|  |  |  | Model nói "CÓ person" |  |  | Model nói "KHÔNG có person" |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | Đoán đúng |  | True Positive |  |  | True Negative |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | Đoán sai |  | False Positive |  |  | False Negative |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | 3. Precision (P) — Độ chính xác khi báo "CÓ" |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | Precision: độ chính xác khi báo "Có" |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | Precision = TP/(TP + FP) |  |  | (độ chính xác) |  | Precision = 4/(4+1)= 4/5 = 80% |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | Trong 5 lần model báo có, bao nhiêu lần thực sự có người. Tức là 5 lần báo có thì đúng với thực tế bao nhiêu |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | Hoặc hiểu theo kiểu: trong những lần model báo có, thực sự đúng thực tế được bao nhiêu |  |  |  |  |  |  |  |
|  | Câu hỏi mà Precision trả lời: |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | "Trong 5 lần model báo 'Có person', bao nhiêu lần thực sự có người?" |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | Trả lời: 4/5 lần = 80%. Còn 1 lần (ảnh 10) là báo nhầm. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | Khi nào cần Precision cao? Khi báo nhầm gây hậu quả lớn.  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | Khi nào cần Precision: khi báo nhầm gây hậu quả lớn |  |  |  |  |  |  |  |
|  | Ví dụ: hệ thống tự động phát cảnh báo qua loa mỗi khi phát hiện người vào vùng nguy hiểm — nếu báo nhầm liên tục, công nhân sẽ mất tin tưởng và bỏ qua cảnh báo. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | Ví dụ: hệ thống tự động phát cảnh báo qua loa mỗi khi phát hiện người vào vùng nguy hiểm. Nếu báo nhầm liên tục, công nhân sẽ mất tin tưởng và bỏ qua cảnh báo |  |  |  |  |  |  |  |
|  | 4. Recall (R) — Tỷ lệ phát hiện được |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | Recall: Tỷ lệ phát hiện được |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | Recall = TP/(TP + FN) |  |  | (Tỷ lệ phát hiện được) |  |  | Recall = 4/(4 + 2) = 4/6 = 66.7%  |
|  | Câu hỏi mà Recall trả lời: |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | "Trong 6 ảnh thực sự có người, model bắt được bao nhiêu?" |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | Trong 6 ảnh thực sự có người, model bắt được bao nhiêu |  |  |  |  |  |  |  |
|  | Trả lời: Chỉ bắt được 4/6 = 66.7%. Bỏ sót 2 người (ảnh 5 và 6). |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | Model đang bắt được 4 ảnh có người, 2 ảnh báo không có người nhưng thực sự là đang có người |  |  |  |  |  |  |  |
|  | Khi nào cần Recall cao? Khi bỏ sót gây nguy hiểm. Ví dụ: phát hiện người xâm nhập khu vực cấm — bỏ sót 1 người có thể gây tai nạn nghiêm trọng. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | Khi nào cần Recall: Khi bỏ sót gây nguy hiểm. Ví dụ: phát hiện người xâm nhập khu vực cấm - bỏ sót 1 người có thể gây tai nạn nghiêm trọng |  |  |  |  |  |  |  |
|  | 5. F1-Score — Điểm cân bằng giữa P và R |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | F1 - Score = Điểm cân bằng giữa P và R |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | F1 = 2 x (P X R)/(P + R) = 2 x (0.80 x 0.667)/(0.80 + 0.067) = 72.7% |  |  |  |  |  |  |
|  | Câu hỏi mà F1 trả lời: |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | "Nhìn tổng thể, model vừa ít báo nhầm vừa ít bỏ sót ở mức nào?" |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | Nhìn tổng thể, model vừa ít báo nhầm, vừa ít bỏ sót ở mức nào |  |  |  |  |  |  |  |
|  | F1 chỉ cao khi cả P lẫn R đều cao. Nếu một trong hai quá thấp, F1 sẽ bị kéo xuống mạnh. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | F1 chỉ cao khi cả P và R đều cao.  |  |  |  |  |  |  |  |
|  | Ví dụ cực đoan: Nếu model luôn đoán "Có person" cho mọi ảnh: |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | Ví dụ cực đoan: nếu model luôn đoán Có person cho mọi ảnh |  |  |  |  |  |  |  |
|  | P = 6/10 = 60% (vì 4 ảnh trống bị báo nhầm) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | P = 6/10 = 60%(6/(6+4)) |  |  |  |  |  |  |  |
|  | R = 6/6 = 100% (bắt hết vì đoán tất cả là CÓ) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | R = 6/6 = 100%(bắt hết vì đoán tất cả là CÓ) |  |  |  |  |  |  |  |
|  | F1 = 2 × 0.6 × 1.0 / (0.6 + 1.0) = 75% → F1 phạt nặng vì P thấp |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | F1 = 2 x 0.6 x 1.0/(0.6 + 1.0) = 75%->F1 phạt nặng vì P thấp |  |  |  |  |  |  |  |
|  | 6. Accuracy (Acc) — Tỷ lệ đoán đúng tổng thể |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | Accuracy(Acc) - Tỷ lệ đoán đúng tổng thể |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | Acc = (TP + TN)/(TP + TN + FP + FN) =(4 + 3)/(4 + 3+ 1 + 2) = 70% |  |  |  |  |  |  |
|  | Câu hỏi mà Accuracy trả lời: |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | Trong tất cả 10 ảnh, model đoán đúng bao nhiêu |  |  |  |  |  |  |  |
|  | "Trong tất cả 10 ảnh, model đoán đúng bao nhiêu?" (đúng CÓ + đúng KHÔNG) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | Đoán đúng 7/10 ảnh |  |  |  |  |  |  |  |
|  | Trả lời: 7/10 = 70%. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | Tuy nhiên Accuracy dễ gây hiểu nhầm: ví dụ 950/1000 ảnh không có người, nếu model đoán toàn bộ không có person -> 95%. |  |  |  |  |  |  |  |
|  | [!CAUTION] Accuracy dễ gây hiểu nhầm! Ví dụ: Nếu 950/1000 ảnh không có người, model chỉ cần luôn đoán "Không có person"  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  Nhưng thực tế Recall = 0%(không bắt được ai cả) |  |  |  |  |  |  |  |
|  | → Acc = 95% rất đẹp, nhưng thực tế Recall = 0% (không bắt được ai). Vì vậy trong object detection, P, R, F1 đáng tin hơn Accuracy. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | Vì vậy P, R, F1 đáng tin hơn Accuracy |  |  |  |  |  |  |  |
|  | Bảng tổng kết |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | Chỉ số |  | Công thức |  | Giá trị |  | Một câu dễ nhớ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | GT |  | — |  | 6 có, 4 không |  | Đáp án chuẩn do con người gán |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | TP |  | — |  | 4 |  | Có người → model nói CÓ → ✔️ Đúng! |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | FP |  | — |  | 1 |  | Không có người → model nói CÓ → 😤 Nhầm! |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | TN |  | — |  | 3 |  | Không có người → model nói KHÔNG → ✔️ Đúng! |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | FN |  | — |  | 2 |  | Có người → model nói KHÔNG → 😱 Sót! |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | P |  | TP/(TP+FP) |  | 0.8 |  | 5 lần báo CÓ, đúng 4 lần |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | R |  | TP/(TP+FN) |  | 0.667 |  | 6 người thật, bắt được 4 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | F1 |  | 2PR/(P+R) |  | 0.727 |  | Cân bằng giữa P và R |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | Acc |  | (TP+TN)/All |  | 0.7 |  | 10 ảnh, đoán đúng 7 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | Mối quan hệ giữa Precision và Recall |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | Trong file run_infer.py dòng 37: CONF = 0.50 chính là ngưỡng confidence này. Tùy bài toán mà bạn điều chỉnh: |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | An toàn lao động (không được bỏ sót người): Giảm CONF → ưu tiên Recall |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | Đếm/thống kê (cần chính xác): Tăng CONF → ưu tiên Precision |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | Ví dụ 2: Giải thích các chỉ số đánh giá mô hình: GT, TP, FP, TN, FN, P, R, F1, Acc |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | Bối cảnh ví dụ xuyên suốt |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | Giả sử bạn có 10 bức ảnh từ camera nhà máy. Bạn muốn kiểm tra mô hình YOLOE có phát hiện đúng "người không đội mũ bảo hộ" hay không. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | Sự thật (do con người xác nhận): |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | 6 ảnh CÓ người không đội mũ (vi phạm thật sự) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | 4 ảnh KHÔNG CÓ người không đội mũ (mọi người đều đội mũ) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | Kết quả mô hình YOLOE dự đoán: |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | Ảnh | Sự thật (GT) | Model dự đoán | Kết quả |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | 1 | ✅ Có vi phạm | ✅ Phát hiện vi phạm | TP ✔️ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | 2 | ✅ Có vi phạm | ✅ Phát hiện vi phạm | TP ✔️ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | 3 | ✅ Có vi phạm | ✅ Phát hiện vi phạm | TP ✔️ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | 4 | ✅ Có vi phạm | ✅ Phát hiện vi phạm | TP ✔️ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | 5 | ✅ Có vi phạm | ❌ Không phát hiện | FN 😰 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | 6 | ✅ Có vi phạm | ❌ Không phát hiện | FN 😰 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | 7 | ❌ Không vi phạm | ❌ Không phát hiện | TN ✔️ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | 8 | ❌ Không vi phạm | ❌ Không phát hiện | TN ✔️ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | 9 | ❌ Không vi phạm | ❌ Không phát hiện | TN ✔️ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | 10 | ❌ Không vi phạm | ✅ Phát hiện vi phạm | FP 😰 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | 1. GT — Ground Truth (Nhãn chuẩn / Sự thật) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | Ý nghĩa: Là kết quả đúng tuyệt đối do con người gán nhãn thủ công. Đây là "đáp án" để so sánh với kết quả dự đoán của mô hình. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | IMPORTANT |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | GT không phải là một chỉ số đánh giá, mà là dữ liệu tham chiếu gốc — nền tảng để tính tất cả các chỉ số còn lại. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | Trong ví dụ: GT cho biết có 6 ảnh thực sự vi phạm và 4 ảnh không vi phạm. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | 2. Bộ 4 kết quả cơ bản: TP, FP, TN, FN |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | Mỗi dự đoán của model so với GT sẽ rơi vào đúng 1 trong 4 ô sau: |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |                         Sự thật (GT) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |                    CÓ (Positive)    KHÔNG (Negative) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |                 ┌────────────────┬────────────────┐ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |   Model    CÓ   │   TP (4 ảnh)   │   FP (1 ảnh)   │ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |   dự đoán       ├────────────────┼────────────────┤ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |            KHÔNG│   FN (2 ảnh)   │   TN (3 ảnh)   │ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |                 └────────────────┴────────────────┘ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | TP — True Positive (Dương tính đúng) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | Nghĩa: Model nói "CÓ" → thực tế ĐÚNG LÀ CÓ. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | Ví dụ: Ảnh 1, 2, 3, 4 — Model phát hiện có người không đội mũ, kiểm tra lại thì đúng là có → TP = 4. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | Cảm giác: 😊 Phát hiện đúng! |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | FP — False Positive (Dương tính giả / Báo động giả) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | Nghĩa: Model nói "CÓ" → nhưng thực tế KHÔNG CÓ. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | Ví dụ: Ảnh 10 — Model báo có người không đội mũ, nhưng kiểm tra lại thì mọi người đều đội mũ đầy đủ → FP = 1. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | Cảm giác: 😤 Báo nhầm, tốn công kiểm tra vô ích! |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | TN — True Negative (Âm tính đúng) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | Nghĩa: Model nói "KHÔNG" → thực tế ĐÚNG LÀ KHÔNG. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | Ví dụ: Ảnh 7, 8, 9 — Model không phát hiện vi phạm, kiểm tra lại cũng đúng là không có → TN = 3. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | Cảm giác: 😊 Bỏ qua đúng! |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | FN — False Negative (Âm tính giả / Bỏ sót) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | Nghĩa: Model nói "KHÔNG" → nhưng thực tế CÓ. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | Ví dụ: Ảnh 5, 6 — Model không phát hiện vi phạm, nhưng thực tế có người không đội mũ bị bỏ sót → FN = 2. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | Cảm giác: 😱 Bỏ sót nguy hiểm! (Trong an toàn lao động, đây là lỗi nghiêm trọng nhất) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | TIP |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | Mẹo nhớ nhanh: |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | Chữ đầu T/F (True/False) = Model đoán Đúng hay Sai. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | Chữ sau P/N (Positive/Negative) = Model đoán là CÓ hay KHÔNG. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | Ví dụ: False Positive = Model đoán Sai rằng Có → Báo nhầm. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | 3. Precision (P) — Độ chính xác |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | P=TPTP+FPP = \frac{TP}{TP + FP}P=TP+FPTP​ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | Ý nghĩa: Trong tất cả những lần model báo "CÓ", bao nhiêu lần thực sự đúng? |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | Tính: |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | P=44+1=45=0.80=80%P = \frac{4}{4 + 1} = \frac{4}{5} = 0.80 = 80\%P=4+14​=54​=0.80=80% |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | Diễn giải: Mỗi khi model báo "có vi phạm", xác suất đúng là 80%. Còn 20% là báo nhầm. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | NOTE |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | Precision cao = Ít báo nhầm. Quan trọng khi báo nhầm gây tốn kém (ví dụ: hệ thống tự động dừng dây chuyền mỗi khi phát hiện vi phạm — nếu báo nhầm nhiều sẽ gây mất năng suất). |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | 4. Recall (R) — Độ phủ / Tỷ lệ phát hiện |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | R=TPTP+FNR = \frac{TP}{TP + FN}R=TP+FNTP​ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | Ý nghĩa: Trong tất cả các trường hợp thực sự CÓ, model phát hiện được bao nhiêu %? |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | Tính: |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | R=44+2=46≈0.667=66.7%R = \frac{4}{4 + 2} = \frac{4}{6} \approx 0.667 = 66.7\%R=4+24​=64​≈0.667=66.7% |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | Diễn giải: Trong 6 trường hợp vi phạm thật sự, model chỉ bắt được 4, bỏ sót 2 → Recall = 66.7%. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | WARNING |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | Recall thấp = Bỏ sót nhiều. Trong bài toán an toàn lao động (như dự án Nozawa), bỏ sót người không đội mũ có thể dẫn tới tai nạn → Recall quan trọng hơn Precision. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | 5. F1-Score — Trung bình điều hòa của P và R |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | F1=2×P×RP+RF1 = 2 \times \frac{P \times R}{P + R}F1=2×P+RP×R​ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | Ý nghĩa: Là chỉ số cân bằng giữa Precision và Recall. F1 cao khi cả hai đều cao. Nếu một trong hai quá thấp, F1 sẽ bị kéo xuống mạnh. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | Tính: |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | F1=2×0.80×0.6670.80+0.667=2×0.5331.467≈0.727=72.7%F1 = 2 \times \frac{0.80 \times 0.667}{0.80 + 0.667} = 2 \times \frac{0.533}{1.467} \approx 0.727 = 72.7\%F1=2×0.80+0.6670.80×0.667​=2×1.4670.533​≈0.727=72.7% |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | NOTE |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | Tại sao không dùng trung bình cộng? Vì trung bình cộng sẽ bị "đánh lừa". Ví dụ: P = 100%, R = 0% (model không phát hiện gì cả nhưng lần duy nhất nó phát hiện thì đúng) → TB cộng = 50% (trông ổn), nhưng F1 = 0% (phản ánh đúng thực tế là model vô dụng). |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | 6. Accuracy (Acc) — Độ chính xác tổng thể |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | Acc=TP+TNTP+TN+FP+FNAcc = \frac{TP + TN}{TP + TN + FP + FN}Acc=TP+TN+FP+FNTP+TN​ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | Ý nghĩa: Trong tất cả các trường hợp, model đoán đúng bao nhiêu %? (Đúng = cả đúng CÓ lẫn đúng KHÔNG) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | Tính: |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | Acc=4+34+3+1+2=710=0.70=70%Acc = \frac{4 + 3}{4 + 3 + 1 + 2} = \frac{7}{10} = 0.70 = 70\%Acc=4+3+1+24+3​=107​=0.70=70% |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | CAUTION |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | Accuracy có thể gây hiểu nhầm khi dữ liệu mất cân bằng! Ví dụ: Nếu 95% ảnh không vi phạm, model chỉ cần luôn đoán "KHÔNG" sẽ đạt Acc = 95% nhưng thực ra nó không phát hiện được gì cả (Recall = 0%). Vì vậy trong bài toán nhận diện vật thể, người ta thường ưu tiên dùng P, R, F1 thay vì Accuracy. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | Tổng kết bằng số từ ví dụ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | Chỉ số | Công thức | Giá trị | Ý nghĩa ngắn gọn |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | GT | — | 6 CÓ, 4 KHÔNG | Đáp án do con người gán |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | TP | — | 4 | Phát hiện đúng |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | FP | — | 1 | Báo nhầm |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | TN | — | 3 | Bỏ qua đúng |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | FN | — | 2 | Bỏ sót |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | P | TP/(TP+FP) | 0.8 | Khi báo CÓ thì đúng bao nhiêu? |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | R | TP/(TP+FN) | 0.667 | Bắt được bao nhiêu % vi phạm thật? |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | F1 | 2PR/(P+R) | 0.727 | Cân bằng giữa P và R |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | Acc | (TP+TN)/Tổng | 0.7 | Tổng thể đoán đúng bao nhiêu? |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | Mối quan hệ và sự đánh đổi giữa Precision và Recall |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | Trong file run_infer.py, biến CONF = 0.50 (dòng 37) chính là ngưỡng confidence này. Bạn có thể điều chỉnh nó để cân bằng giữa Precision và Recall tùy theo yêu cầu thực tế của dự án. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
## Sheet: Prompt
| <<Overview |  |  |  |
| --- | --- | --- | --- |
|  | Prompt |  |  |
|  | Tham khảo một số prompt để xuất ra dữ liệu |  |  |
|  | Prompt ra code và file Excel tổng Person…. |  |  |
|  |  | Tôi đang sử dụng đoạn code trên để detect object trong 1 ảnh bằng VLM local |  |
|  |  | Giờ hoàn thiện/bố sung code để : |  |
|  |  | Chạy với 1 folder ảnh |  |
|  |  | Lưu raw .txt nguyên vẹn kết quả từ VLM |  |
|  |  | Lưu .json đã chuyển đổi |  |
|  |  | Hỉnh ảnh đã vẽ bbox vào thư mục bbox |  |
|  |  | file excel điền đủ các cột : path ảnh, trạng thái (chạy có lỗi gì không : ok/ng), tổng đối tượng, tổng người, tổng khẩu trang, tổng mũ bảo hiểm, tổng áo bảo hộ, tổng xe nâng, hình ảnh đã thêm box |  |
|  |  | Tất cả đặt trong thư mục output |  |
|  | Prompt liên kết người với xe nâng gần |  |  |
|  |  | Yêu cầu ban đầu |  |
|  |  |  | nhờ liquid suy luận thêm relationship giữa người - xe nữa giúp anh |
|  |  |  | qween thôi cũng được |
|  |  |  | Dạ về Context Definitions, có 4 mục chính. Hiện em chạy prompt cho 2 mục Person – PPE và Person – Posture trước, 2 mục còn lại Person – Forklift với Person – Machinery dự định prompt riêng  (đều em chưa nghĩ ra hướng output phù hợp) |
|  |  |  | Prompt đang dùng : |
## Sheet: RunApp
| <<Overview |  |  |
| --- | --- | --- |
|  | Build & Run App |  |
|  | Cài python |  |
|  |  | PS C:\work\Projects\Sanwa\01.Document\find_data_integration> python --version |
|  | Chạy venv |  |
|  |  | PS C:\work\Projects\Sanwa\01.Document\find_data_integration> python -m venv venv |
|  | Chạy active |  |
|  |  | PS C:\work\Projects\Sanwa\01.Document\find_data_integration> venv/scripts/activate |
|  | Cài các thư viện trọng file requirement có sẵn |  |
|  |  | (venv) PS C:\work\Projects\Sanwa\01.Document\find_data_integration> pip install -r requirements.txt |
|  | Chạy |  |
|  |  | python server.py |
|  | Hoặc | (venv) PS C:\work\Projects\Sanwa\01.Document\find_data_integration> uvicorn server:app --reload |
|  | Mở trình duyệt và truy cập: http://127.0.0.1:8000/ |  |
|  | Chi tiết: |  |
|  | PS C:\work\Projects\Sanwa\01.Document\find_data_integration> python --version |  |
|  | Python 3.14.2 |  |
|  | PS C:\work\Projects\Sanwa\01.Document\find_data_integration> py list |  |
|  | Tag           Name           Managed By  Version  Alias |  |
|  | 3.14[-64]  *  Python 3.14.2  PythonCore  3.14.2   python3[-64].exe, python3.14[-64].exe |  |
|  | PS C:\work\Projects\Sanwa\01.Document\find_data_integration> python -m venv venv |  |
|  | PS C:\work\Projects\Sanwa\01.Document\find_data_integration> venv/scripts/activate |  |
|  | (venv) PS C:\work\Projects\Sanwa\01.Document\find_data_integration> pip install -r requirements.txt |  |
|  | Collecting pymupdf<2,>=1.24 (from -r requirements.txt (line 1)) |  |
|  |   Downloading pymupdf-1.28.2-cp310-abi3-win_amd64.whl.metadata (26 kB) |  |
|  | Collecting numpy<3,>=1.24 (from -r requirements.txt (line 2)) |  |
|  |   Downloading numpy-2.5.4-cp314-cp314-win_amd64.whl.metadata (6.6 kB) |  |
|  | Collecting ezdxf (from -r requirements.txt (line 3)) |  |
|  |   Downloading ezdxf-1.4.5-cp314-cp314-win_amd64.whl.metadata (10 kB) |  |
|  | Collecting matplotlib<4,>=3.8 (from -r requirements.txt (line 4)) |  |
|  |   Using cached matplotlib-3.11.2-cp314-cp314-win_amd64.whl.metadata (80 kB) |  |
|  | Collecting shapely<3,>=2.0 (from -r requirements.txt (line 5)) |  |
|  |   Downloading shapely-2.2.0-cp314-cp314-win_amd64.whl.metadata (6.8 kB) |  |
|  | Collecting opencv-python (from -r requirements.txt (line 6)) |  |
|  |   Using cached opencv_python-5.0.0.93-cp37-abi3-win_amd64.whl.metadata (20 kB) |  |
|  | Collecting svgwrite (from -r requirements.txt (line 7)) |  |
|  |   Downloading svgwrite-1.4.3-py3-none-any.whl.metadata (8.8 kB) |  |
|  | Collecting pillow (from -r requirements.txt (line 8)) |  |
|  |   Downloading pillow-13.0.0-cp314-cp314-win_amd64.whl.metadata (9.3 kB) |  |
|  | Collecting vtracer (from -r requirements.txt (line 9)) |  |
|  |   Downloading vtracer-0.6.15-cp314-cp314-win_amd64.whl.metadata (4.4 kB) |  |
|  | Collecting fastapi (from -r requirements.txt (line 10)) |  |
|  |   Downloading fastapi-0.162.0-py3-none-any.whl.metadata (26 kB) |  |
|  | Collecting uvicorn (from -r requirements.txt (line 11)) |  |
|  |   Downloading uvicorn-0.54.0-py3-none-any.whl.metadata (6.6 kB) |  |
|  | Collecting contourpy>=1.0.1 (from matplotlib<4,>=3.8->-r requirements.txt (line 4)) |  |
|  |   Using cached contourpy-1.4.0-cp314-cp314-win_amd64.whl.metadata (3.8 kB) |  |
|  | Collecting cycler>=0.10 (from matplotlib<4,>=3.8->-r requirements.txt (line 4)) |  |
|  |   Using cached cycler-0.12.1-py3-none-any.whl.metadata (3.8 kB) |  |
|  | Collecting fonttools>=4.28.2 (from matplotlib<4,>=3.8->-r requirements.txt (line 4)) |  |
|  |   Using cached fonttools-4.68.0-cp314-cp314-win_amd64.whl.metadata (142 kB) |  |
|  | Collecting kiwisolver>=1.3.1 (from matplotlib<4,>=3.8->-r requirements.txt (line 4)) |  |
|  |   Using cached kiwisolver-1.5.1-cp314-cp314-win_amd64.whl.metadata (5.2 kB) |  |
|  | Collecting packaging>=20.0 (from matplotlib<4,>=3.8->-r requirements.txt (line 4)) |  |
|  |   Downloading packaging-26.3-py3-none-any.whl.metadata (3.5 kB) |  |
|  | Collecting pyparsing>=3 (from matplotlib<4,>=3.8->-r requirements.txt (line 4)) |  |
|  |   Using cached pyparsing-3.3.3-py3-none-any.whl.metadata (5.9 kB) |  |
|  | Collecting python-dateutil>=2.7 (from matplotlib<4,>=3.8->-r requirements.txt (line 4)) |  |
|  |   Downloading python_dateutil-3.0.0-py2.py3-none-any.whl.metadata (8.2 kB) |  |
|  | Collecting typing_extensions>=4.6.0 (from ezdxf->-r requirements.txt (line 3)) |  |
|  |   Downloading typing_extensions-4.16.0-py3-none-any.whl.metadata (3.3 kB) |  |
|  | Collecting starlette>=0.46.0 (from fastapi->-r requirements.txt (line 10)) |  |
|  |   Downloading starlette-1.10.0-py3-none-any.whl.metadata (6.6 kB) |  |
|  | Collecting pydantic>=2.9.0 (from fastapi->-r requirements.txt (line 10)) |  |
|  |   Downloading pydantic-2.14.2-py3-none-any.whl.metadata (137 kB) |  |
|  | Collecting typing-inspection>=0.4.2 (from fastapi->-r requirements.txt (line 10)) |  |
|  |   Downloading typing_inspection-0.4.4-py3-none-any.whl.metadata (2.6 kB) |  |
|  | Collecting annotated-doc>=0.0.2 (from fastapi->-r requirements.txt (line 10)) |  |
|  |   Downloading annotated_doc-0.0.5-py3-none-any.whl.metadata (6.5 kB) |  |
|  | Collecting opentelemetry-api>=1.44.0 (from fastapi->-r requirements.txt (line 10)) |  |
|  |   Downloading opentelemetry_api-1.45.2-py3-none-any.whl.metadata (1.4 kB) |  |
|  | Collecting click>=7.0 (from uvicorn->-r requirements.txt (line 11)) |  |
|  |   Downloading click-8.5.0-py3-none-any.whl.metadata (2.6 kB) |  |
|  | Collecting h11>=0.8 (from uvicorn->-r requirements.txt (line 11)) |  |
|  |   Using cached h11-0.16.0-py3-none-any.whl.metadata (8.3 kB) |  |
|  | Collecting annotated-types>=0.6.0 (from pydantic>=2.9.0->fastapi->-r requirements.txt (line 10)) |  |
|  |   Downloading annotated_types-0.8.0-py3-none-any.whl.metadata (15 kB) |  |
|  | Collecting pydantic-core==2.50.2 (from pydantic>=2.9.0->fastapi->-r requirements.txt (line 10)) |  |
|  |   Downloading pydantic_core-2.50.2-cp314-cp314-win_amd64.whl.metadata (6.7 kB) |  |
|  | Collecting six>=1.6 (from python-dateutil>=2.7->matplotlib<4,>=3.8->-r requirements.txt (line 4)) |  |
|  |   Using cached six-1.17.0-py2.py3-none-any.whl.metadata (1.7 kB) |  |
|  | Collecting tzdata (from python-dateutil>=2.7->matplotlib<4,>=3.8->-r requirements.txt (line 4)) |  |
|  |   Downloading tzdata-2026.6-py2.py3-none-any.whl.metadata (1.4 kB) |  |
|  | Collecting anyio<5,>=4.0.0 (from starlette>=0.46.0->fastapi->-r requirements.txt (line 10)) |  |
|  |   Downloading anyio-4.15.1-py3-none-any.whl.metadata (4.7 kB) |  |
|  | Collecting idna>=2.8 (from anyio<5,>=4.0.0->starlette>=0.46.0->fastapi->-r requirements.txt (line 10)) |  |
|  |   Downloading idna-3.20-py3-none-any.whl.metadata (7.2 kB) |  |
|  | Downloading pymupdf-1.28.2-cp310-abi3-win_amd64.whl (19.8 MB) |  |
|  |    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 19.8/19.8 MB 1.3 MB/s  0:00:14 |  |
|  | Downloading numpy-2.5.4-cp314-cp314-win_amd64.whl (12.7 MB) |  |
|  |    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 12.7/12.7 MB 2.2 MB/s  0:00:05 |  |
|  | Using cached matplotlib-3.11.2-cp314-cp314-win_amd64.whl (9.5 MB) |  |
|  | Downloading shapely-2.2.0-cp314-cp314-win_amd64.whl (1.8 MB) |  |
|  |    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 1.8/1.8 MB 1.6 MB/s  0:00:01 |  |
|  | Downloading ezdxf-1.4.5-cp314-cp314-win_amd64.whl (3.1 MB) |  |
|  |    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 3.1/3.1 MB 1.9 MB/s  0:00:01 |  |
|  | Downloading opencv_python-5.0.0.93-cp37-abi3-win_amd64.whl (44.0 MB) |  |
|  |    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 44.0/44.0 MB 2.4 MB/s  0:00:18 |  |
|  | Downloading svgwrite-1.4.3-py3-none-any.whl (67 kB) |  |
|  | Downloading pillow-13.0.0-cp314-cp314-win_amd64.whl (7.3 MB) |  |
|  |    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 7.3/7.3 MB 4.2 MB/s  0:00:01 |  |
|  | Downloading vtracer-0.6.15-cp314-cp314-win_amd64.whl (842 kB) |  |
|  |    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 842.8/842.8 kB 2.8 MB/s  0:00:00 |  |
|  | Downloading fastapi-0.162.0-py3-none-any.whl (148 kB) |  |
|  | Downloading uvicorn-0.54.0-py3-none-any.whl (87 kB) |  |
|  | Downloading annotated_doc-0.0.5-py3-none-any.whl (5.3 kB) |  |
|  | Downloading click-8.5.0-py3-none-any.whl (125 kB) |  |
|  | Using cached contourpy-1.4.0-cp314-cp314-win_amd64.whl (240 kB) |  |
|  | Using cached cycler-0.12.1-py3-none-any.whl (8.3 kB) |  |
|  | Using cached fonttools-4.68.0-cp314-cp314-win_amd64.whl (2.5 MB) |  |
|  | Using cached h11-0.16.0-py3-none-any.whl (37 kB) |  |
|  | Using cached kiwisolver-1.5.1-cp314-cp314-win_amd64.whl (72 kB) |  |
|  | Downloading opentelemetry_api-1.45.2-py3-none-any.whl (60 kB) |  |
|  | Downloading packaging-26.3-py3-none-any.whl (129 kB) |  |
|  | Downloading pydantic-2.14.2-py3-none-any.whl (490 kB) |  |
|  | Downloading pydantic_core-2.50.2-cp314-cp314-win_amd64.whl (2.3 MB) |  |
|  |    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 2.3/2.3 MB 2.8 MB/s  0:00:00 |  |
|  | Downloading annotated_types-0.8.0-py3-none-any.whl (13 kB) |  |
|  | Using cached pyparsing-3.3.3-py3-none-any.whl (126 kB) |  |
|  | Downloading python_dateutil-3.0.0-py2.py3-none-any.whl (94 kB) |  |
|  | Using cached six-1.17.0-py2.py3-none-any.whl (11 kB) |  |
|  | Downloading starlette-1.10.0-py3-none-any.whl (80 kB) |  |
|  | Downloading anyio-4.15.1-py3-none-any.whl (132 kB) |  |
|  | Downloading idna-3.20-py3-none-any.whl (69 kB) |  |
|  | Downloading typing_extensions-4.16.0-py3-none-any.whl (45 kB) |  |
|  | Downloading typing_inspection-0.4.4-py3-none-any.whl (14 kB) |  |
|  | Downloading tzdata-2026.6-py2.py3-none-any.whl (348 kB) |  |
|  | annotated-types, annotated-doc, uvicorn, typing-inspection, shapely, python-dateutil, pydantic-core, opentelemetry-api, opencv-python, ezdxf, contourpy, anyio, starlette, pydantic, matplotlib, fastapi |  |
|  | Successfully installed annotated-doc-0.0.5 annotated-types-0.8.0 anyio-4.15.1 click-8.5.0 contourpy-1.4.0 cycler-0.12.1 ezdxf-1.4.5 fastapi-0.162.0 fonttools-4.68.0 h11-0.16.0 idna-3.20 kiwisolver-1.5.1 matplotlib-3.11.2 numpy-2.5.4 opencv-python-5.0.0.93 opentelemetry-api-1.45.2 packaging-26.3 pillow-13.0.0 pydantic-2.14.2 pydantic-core-2.50.2 pymupdf-1.28.2 pyparsing-3.3.3 python-dateutil-3.0.0 shapely-2.2.0 six-1.17.0 starlette-1.10.0 svgwrite-1.4.3 typing-inspection-0.4.4 typing_extensions-4.16.0 tzdata-2026.6 uvicorn-0.54.0 vtracer-0.6.15 |  |
|  | [notice] A new release of pip is available: 25.3 -> 26.2.2 |  |
|  | [notice] To update, run: python.exe -m pip install --upgrade pip |  |
|  | (venv) PS C:\work\Projects\Sanwa\01.Document\find_data_integration> uvicorn server:app --reload |  |
|  | INFO:     Will watch for changes in these directories: ['C:\\work\\Projects\\Sanwa\\01.Document\\find_data_integration'] |  |
|  | INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit) |  |
|  | INFO:     Started reloader process [6788] using StatReload |  |
|  | INFO:     Started server process [17424] |  |
|  | INFO:     Waiting for application startup. |  |
|  | Entity KHÔNG được vẽ: {'HATCH': 13} |  |
|  | Tổng số đoạn thẳng: 123,921 |  |
|  | kích thước DXF: 57.0833320574214 31.49333262940247 |  |
|  | prepare_assets xong sau 13.8s |  |
|  | Sẵn sàng sau 13.8s ... |  |
|  | INFO:     Application startup complete. |  |
|  | INFO:     127.0.0.1:58025 - "GET / HTTP/1.1" 307 Temporary Redirect |  |
|  | INFO:     127.0.0.1:58025 - "GET /banve.svg HTTP/1.1" 200 OK |  |
|  | INFO:     127.0.0.1:58025 - "GET /api/regions HTTP/1.1" 200 OK |  |
|  | INFO:     127.0.0.1:58025 - "GET /favicon.ico HTTP/1.1" 404 Not Found |  |
|  | INFO:     127.0.0.1:58050 - "POST /api/find HTTP/1.1" 200 OK |  |
|  | INFO:     127.0.0.1:58058 - "GET /.well-known/appspecific/com.chrome.devtools.json HTTP/1.1" 404 Not Found |  |
|  | INFO:     127.0.0.1:58092 - "POST /api/find HTTP/1.1" 200 OK |  |
|  | INFO:     127.0.0.1:58314 - "GET /banve.svg HTTP/1.1" 200 OK |  |
|  | INFO:     127.0.0.1:58315 - "GET /.well-known/appspecific/com.chrome.devtools.json HTTP/1.1" 404 Not Found |  |
|  | INFO:     127.0.0.1:58314 - "GET /api/regions HTTP/1.1" 200 OK |  |
|  | INFO:     127.0.0.1:58414 - "POST /api/find HTTP/1.1" 200 OK |  |
|  | INFO:     127.0.0.1:58546 - "POST /api/find HTTP/1.1" 200 OK |  |
|  | INFO:     127.0.0.1:58827 - "POST /api/find HTTP/1.1" 200 OK |  |
|  | INFO:     127.0.0.1:58871 - "POST /api/find HTTP/1.1" 200 OK |  |
|  | DXF_PATH = "1.dxf" |  |
|  | SVG_PATH = BASE_DIR / "banve.svg"  # SVG nền do matplotlib vẽ |  |
|  | MAPPING_PATH = BASE_DIR / "mapping.json"  # ma trận DXF <-> banve.svg |  |
## Sheet: StartBenchMark
| <<Overview |  |  |  |
| --- | --- | --- | --- |
|  | Benchmark model YOLO |  |  |
|  | Bước 1: Tạo thư mục dự án & Môi trường ảo (venv) |  |  |
|  |  | Mở Terminal (trên Linux/Mac) hoặc Command Prompt / PowerShell (trên Windows) và thực hiện các lệnh sau: |  |
|  |  | Tạo thư mục dự án và di chuyển vào trong: |  |
|  |  |  | mkdir benchmark |
|  |  |  | cd benchmark |
|  |  | Khởi tạo môi trường ảo venv: |  |
|  |  |  | python -m venv venv |
|  |  | Kích hoạt (Activate) môi trường ảo: |  |
|  |  |  | venv/Scripts/activate |
|  | Bước 2: Tạo file requirements.txt & Cài đặt thư viện |  |  |
|  |  | python -m pip install --upgrade pip |  |
|  |  | pip install -r requirements.txt |  |
|  | Bước 3: Chuẩn bị cấu trúc thư mục dữ liệu |  |  |
|  |  | Tạo sẵn các thư mục để chứa dữ liệu đầu vào và kết quả đầu ra: |  |
|  |  | Cấu trúc dự án của bạn lúc này sẽ như sau: |  |
|  |  |  | benchmark/ |
|  |  |  | ├── venv/                 # Thư mục môi trường ảo (không đụng vào) |
|  |  |  | ├── data/ |
|  |  |  | │   └── images/          # 👈 Đặt các ảnh test (.jpg / .png) của NOZAWA vào đây |
|  |  |  | ├── models/              # Chứa weights (.pt) |
|  |  |  | ├── results/             # Chứa file kết quả xuất ra (.csv) |
|  |  |  | ├── run_yolo_benchmark.py    # Script chính để chạy |
|  |  |  | └── requirements.txt |
|  |  | Copy ảnh thực tế dán vào thư mục data/images/ để chuẩn bị test. |  |
|  | Bước 4: Viết mã nguồn Benchmark |  |  |
|  | Bước 5: Thực thi & Đọc kết quả |  |  |
|  |  |  | python .\run_bmv2.py |
## Sheet: Tesseract
| <<Overview |  |
| --- | --- |
|  | Teseract nhị phân |
|  | Thuật ngữ **"Tesseract nhị phân"** (dịch từ tiếng Anh: **"Tesseract Binary"** hoặc *Tesseract Executable*) dùng để chỉ **phần mềm / tệp chương trình thực thi đã được biên dịch sẵn** (file `.exe` trên Windows hoặc file chạy trên Linux/macOS) của công cụ Tesseract OCR, chứ **không phải** là mã thư viện Python. |
|  | Cụ thể, bạn có thể hiểu đơn giản qua 3 điểm sau: |
|  | --- |
|  | ### 1. Phân biệt giữa `pytesseract` và `Tesseract binary` |
|  | * **`pytesseract` (gói Python):** Khi bạn gõ `pip install pytesseract`, gói này thực chất chỉ là một **lớp vỏ bọc (wrapper)** viết bằng Python. Bản thân nó **không thể tự đọc chữ trên ảnh**. |
|  | * **`Tesseract binary` (phần mềm gốc):** Đây là chương trình OCR cốt lõi do HP/Google phát triển, được viết bằng ngôn ngữ **C/C++** và đã biên dịch thành file mã máy (nhị phân). |
|  |   * Trên **Windows**: Đó là tệp `tesseract.exe` (thường nằm tại `C:\Program Files\Tesseract-OCR\tesseract.exe`). |
|  |   * Trên **Linux / Ubuntu**: Đó là tệp thực thi `/usr/bin/tesseract` (cài qua lệnh `sudo apt install tesseract-ocr`). |
|  |   * Trên **macOS**: Cài qua Homebrew (`brew install tesseract`). |
|  | --- |
|  | ### 2. Cách hoạt động bên dưới |
|  | Khi mã Python của bạn chạy lệnh nhận diện ảnh bằng Tesseract: |
|  | ``` |
|  | [Mã Python / pytesseract] ──(gọi ngầm)──► [tệp thực thi tesseract.exe trên hệ điều hành] ──(trả kết quả)──► [Python] |
|  | ``` |
|  | Nếu hệ điều hành của bạn chưa cài đặt phần mềm Tesseract này, Python sẽ báo lỗi quen thuộc: |
|  | > `pytesseract.TesseractNotFoundError: tesseract is not installed or it's not in your PATH` |
|  | --- |
|  | ### 3. Trong dự án Nozawa OCR này |
|  | * Engine `tesseract` chỉ là một **lựa chọn phụ (optional)** để làm mốc đối chiếu (baseline) hoặc chạy song song trên CPU trong endpoint `/ocr2`. |
|  | * Nếu dự án của bạn chỉ sử dụng các mô hình Deep Learning chính như **LiquidAI (`liquid-3b`)** hoặc **TrOCR (`trocr`)**, bạn **hoàn toàn không cần phải cài đặt Tesseract nhị phân này**. |
## Sheet: OCR
| <<Overview |  |
| --- | --- |
|  | OCR |
|  | **OCR** là viết tắt của **Optical Character Recognition** (tiếng Việt gọi là: **Nhận dạng ký tự quang học**). |
|  | Hiểu một cách đơn giản: **OCR là công nghệ giúp máy tính "nhìn" vào một bức ảnh và "đọc" được chữ/số có trong bức ảnh đó thành văn bản kỹ thuật số (text) mà máy tính có thể lưu trữ, chỉnh sửa hoặc tìm kiếm được.** |
|  | --- |
|  | ### 1. Ví dụ trực quan |
|  | * **Trước khi có OCR:** Máy tính chỉ xem bức ảnh như một tập hợp các điểm màu (pixel) vô nghĩa. Nó không biết đâu là số `8`, đâu là chữ `A`. |
|  | * **Khi dùng OCR:** |
|  |   ``` |
|  |   [ Ảnh chụp nhãn mác: "185  15" ] ──(Qua bộ xử lý OCR)──► Chuỗi ký tự máy tính: "185 15" |
|  |   ``` |
|  |   Nhờ đó, hệ thống phần mềm có thể tự động lưu số `185` và `15` vào cơ sở dữ liệu (Database) mà không cần con người phải ngồi gõ lại bằng tay. |
|  | --- |
|  | ### 2. Các ứng dụng thực tế phổ biến của OCR |
|  | * **Tự động hóa tài liệu:** Quét hóa đơn đỏ, hợp đồng, chứng minh thư/CCCD, hộ chiếu (eKYC ngân hàng). |
|  | * **Công nghiệp & Giao thông:** Đọc biển số xe tự động qua camera giao thông, đọc mã vạch, đọc số seri trên linh kiện/sản phẩm trên băng chuyền. |
|  | * **Số hóa sách báo:** Biến sách in hoặc tài liệu scan thành tệp Word/PDF có thể bôi đen copy chữ và tìm kiếm được. |
|  | --- |
|  | ### 3. Trong dự án Nozawa OCR này |
|  | Dự án này sử dụng OCR chuyên sâu cho bài toán **nhận diện số (Numeric OCR)** từ ảnh chụp thực tế của sản phẩm: |
|  | * **Phương pháp truyền thống (Tesseract):** Tìm kiếm và nhận dạng các đường nét hình học của ký tự (nhanh, nhẹ nhưng dễ sai nếu ảnh mờ hoặc lóa sáng). |
|  | * **Phương pháp Trí tuệ nhân tạo / Deep Learning (TrOCR, LiquidAI, Qwen-VL):** Sử dụng các mô hình thị giác máy tính hiện đại được huấn luyện với hàng triệu bức ảnh để "hiểu" được hình dạng con số ngay cả khi ảnh chụp bị góc nghiêng, mờ nhòe, đổ bóng hay biến dạng phức tạp. |
## Sheet: Sanwa_5
| <<Overview |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | SANWA - 5_TYD-0063539201-01_★ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | No | Hạng mục lớn | Hạng mục kiểm tra | Kết quả phán định |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 1 | Kích thước | W trùng khớp | Trường hợp trên bản vẽ mặt đứng có ghi W=970 và trên bản vẽ chi tiết cũng có ghi giá trị W |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 2 | Kích thước | Kích thước phần chừa kéo trùng khớp | Trường hợp trên bản vẽ mặt đứng ghi 150 và trên bản vẽ chi tiết phần chừa kéo cũng có ghi giá trị số |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 3 | Kích thước | Kích thước lỗ mở hữu dụng trùng khớp | Trường hợp trên bản vẽ mặt đứng ghi 820 và trên bản vẽ chi tiết phần lỗ mở hữu dụng cũng có ghi giá trị số |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 4 | Kích thước | H trùng khớp | Trường hợp trên bản vẽ mặt đứng ghi H=2000 và trên bản vẽ chi tiết cũng có ghi giá trị H |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 5 | Kích thước | Kích thước lọt khung trùng khớp | Bản vẽ mặt đứng : Bản vẽ chi tiết = 131 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 6 | Kích thước | Kích thước cửa sổ W trùng khớp | Tính toán và xác nhận từ kích thước DW |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 8 | Kích thước | Kích thước W của ô kính trùng khớp | Giống như phần lỗ mở |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 7 | Kích thước | Kích thước cửa sổ H trùng khớp | Kiểm tra bằng cách tính từ H=2000 và các kích thước trên bản vẽ chi tiết |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 9 | Kích thước | Kích thước H của ô kính trùng khớp | Giống như phần lỗ mở |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 10 | Tay mở | Tay mở R/L trùng khớp | Xác nhận tổng số lượng bằng cách đối chiếu bảng kim khí với hình chiếu bằng |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 11 | Tay mở | Vị trí cửa kiểm tra trùng khớp | Khớp với ký hiệu cửa kiểm tra trên bản vẽ mặt đứng và hướng mở lấy đó làm điểm xuất phát |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 12 | Kim khí | Mã sản phẩm khóa trùng khớp | Trường hợp là khóa xi lanh: khóa, xi lanh khóa và bộ khóa. Trường hợp là khóa chốt: chỉ có 1 dòng mã sản phẩm của khóa chốt. Tuy nhiên hình dạng cao su đầu hộp trên bản vẽ chi tiết là khác nhau |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 13 | Kim khí | Mã sản phẩm tay kéo trùng khớp | Kiểm tra xem có bị thiếu ghi mã sản phẩm hay không |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 14 | Cửa | Vật liệu bề mặt trùng khớp | Xác nhận kích thước W・H khả dụng từ bảng danh sách tồn kho theo từng loại vật liệu bề mặt |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 手配区分
Trạng thái cấp phát / đặt hàng | 連携
Liên kết | 品名
Tên vật tư |  | メーカー
Nhà sản xuất |  |  | 品番
Mã sản phẩm/Thông số kĩ thuật |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 工場付金具 (Phụ kiện lắp sẵn tại nhà máy) | o | レール | Ray trượt | リョービ | Ryobi | Hãng Ryobi | SWSL-1-WA1 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 工場付金具 (Phụ kiện lắp sẵn tại nhà máy) | o | レール取付ねじセット | Bộ vít lắp ray | リョービ | Ryobi | Hãng Ryobi | SWSL-1-WA2 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 工場付金具 (Phụ kiện lắp sẵn tại nhà máy) | o | ラックユニット | Cụm rack unit | リョービ | Ryobi | Hãng Ryobi | SWSL-1-WA3 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | o | 戸車セット | Bộ bánh xe cửa trượt | リョービ | Ryobi | Hãng Ryobi | SWSL-1-TO |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | o | 戸先ゴム（凸） | Gioăng cao su đầu cánh (lồi) | 三ツ星 | Mitsuboshi | Hãng Mitsuboshi | TR-A(BG) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | o | 戸当ゴム（戸尻） | Gioăng chặn cửa (phía đuôi cánh) | 北星ゴム | Hokusei Gomu | Công ty Cao su Hokusei | TAG30 BG扉用 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | o | ガードゴムA | Gioăng bảo vệ A | 北星ゴム | Hokusei Gomu | Công ty Cao su Hokusei | GG-A BG |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | ロッド錠 | Khóa rod (khóa chốt dọc) | 美和 | Miwa | Hãng khóa MIWA | SW1SD11 (L=1313) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | o | ロッドガイド | Thanh dẫn hướng rod | 美和 | Miwa | Hãng khóa MIWA | SWSP-GBT |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 工場付金具 (Phụ kiện lắp sẵn tại nhà máy) | o | LS用ビスセット | Bộ vít dành cho LS | 三和型 | Sanwa-gata | Loại/Bộ tiêu chuẩn Sanwa | LS3ビスセットボード（12.5） |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 現場付金具 (Phụ kiện lắp tại công trường) |  | 制動装置 | Bộ giảm chấn | リョービ | Ryobi | Hãng Ryobi | SWSL-1-GE |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | フル止メローラー | Con lăn chặn cuối hành trình | リョービ | Ryobi | Hãng Ryobi | SWGT-20LV2 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | ロッド錠ストライク | Miếng nhận khóa rod (strike plate) | 美和 | Miwa | Hãng khóa MIWA | SWSD-SKT |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | ユリアねじ | Vít Urea | テクノアソシエ | Techno Associe | Công ty Techno Associe | M5×8 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | エンドストッパー | Chặn cuối hành trình | リョービ | Ryobi | Hãng Ryobi | SWST-01 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | スムードS注意ステッカー | Tem cảnh báo Smooth S | アトリエ・K | Atelier K | Công ty Atelier K | SSGS |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 引き棒 | Tay kéo / Thanh kéo | シブタニ | Shibutani | Hãng Shibutani | S725G-H-P425 (D+40) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | ロッド錠用シリンダー | Xi lanh dùng cho khóa rod | 美和 | Miwa | Hãng khóa MIWA | U9SWM40-1 dt 40-トゥイキー |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | ロッド錠用シリンダー | Xi lanh dùng cho khóa rod | 美和 | Miwa | Hãng khóa MIWA | U9SWM40-1 dt 40-コンベキー |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | BẢNG TỒN KHO VẬT LIỆU BỀ MẶT |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | Kích thước

Tấm thép
và
Mã màu |  |  |  | 0.4 × 914 × 2134 | 0.6 × 958 × 2079 | 0.6 × 958 × 2179 | 0.6 × 958 × 2180 | 0.6 × 958 × 2230 | 0.6 × 980 × 2200 | 0.6 × 1045 × 2179 | 0.6 × 1050 × 2390 | 0.6 × 1209 × 2230 | 0.6 × 1219 × 2230 | 0.6 × 1490 × 2230 | 0.6 × 1500 × 2230 | 0.6 × 967 × 2939 | 0.6 × 1265 × 2939 | 0.6 × 855 × 2160 | 0.6 × 914 × 2160 | 0.6 × 1000 × 2160 | 0.6 × 1000 × 2230 | 0.6 × 1219 × 2160 | 0.6 × 1219 × 2230 | 0.6 × 1219 × 2438 | 0.6 × 1524 × 2230 | 0.6 × 1524 × 2491 | 0.6 × 1219 × 2560 | 0.8 × 914 × 2161 | 0.8 × 1219 × 2439 | 0.8 × 1219 × 2901 | 0.8 × 1524 × 2250 | 0.8 × 1524 × 2900 | 0.8 × 1219 × 2438 | 0.8 × 1219 × 3000 | 0.6 × 1500 × 2760 | 0.6 × 1219 × 2050 | 0.6 × 1219 × 2760 | 0.6 × 1260 × 2939 | 0.5 × 1219 × 3000 |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | EK-603 (họa tiết ngang) |  |  |  |  | C |  |  |  |  | B |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | EK-601 (họa tiết ngang) |  |  |  |  | C |  |  |  |  | B |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | EK-602 (họa tiết ngang) |  |  |  |  | C |  |  |  |  | B |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | Elegant Ivory (Ngà thanh lịch) |  |  |  |  | B |  |  |  |  | B |  | B |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | Kem |  |  |  |  | B |  |  |  |  | B |  | B |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | Dai Nippon
Printing

Thép
Elio |  |  | SSH Kem |  |  |  |  | A |  |  |  |  | A |  | B |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | SSH Trắng – thép Elio |  |  |  |  | A |  |  |  |  | A |  | B |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | SSH Xanh dương – thép Elio |  |  |  |  | B |  |  |  |  | B |  | B |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | SSH Xanh lá – thép Elio |  |  |  |  | B |  |  |  |  | B |  | B |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | SSH Hồng – thép Elio |  |  |  |  | B |  |  |  |  | B |  | B |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | NSP | Đơn sắc | NSP-Trắng |  |  |  |  | A |  |  |  |  | A |  | A |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | C |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | NSP-Trắng kháng virus |  |  |  |  |  |  |  |  |  | C |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | NSP-Kem |  |  |  |  | A |  |  |  |  | A |  | A |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | C |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | NSP-Xám |  |  |  |  | C |  |  |  |  | C |  | C |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | C |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | Nhà vệ sinh | Đơn sắc | SSH Trắng |  |  |  |  |  |  |  |  |  |  |  |  | B | B |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | Vân gỗ | EK-211T |  |  |  |  |  |  |  |  |  |  |  |  | B | B |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | EK-217T |  |  |  |  |  |  |  |  |  |  |  |  | B | B |  | Lưu ý: Các màu thép khác sẽ đặt hàng mỗi lần phát sinh (sau khi đặt hàng, thép về mất khoảng 1 tháng…) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | EK-238T |  |  |  |  |  |  |  |  |  |  |  |  |  | C |  | Lưu ý: Kích thước tấm: ① 0.6×967×2939  ② 0.6×1265×2939 (gồm 2 kích thước…) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | EK-404T |  |  |  |  |  |  |  |  |  |  |  |  |  | C |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | Yodogawa

Dai Nippon
Printing

Thép Elio | SPS | Đơn sắc | SP Trắng |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | C |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | SP Kem |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | C |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | Vân gỗ | Màu gỗ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | C |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | Light Karia Teak (Tếch Karia nhạt) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | C |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | Gỗ sồi (Oak) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | C |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 1. Dai Nippon Printing mất khoảng 1 tháng để sản xuất. Với Toppan, Nippon Steel (Nittetsu) và Yodogawa, thời gian giao hàng có thể mất từ 3 tháng trở lên. Vui lòng đặt hàng trước sớm. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 2. Việc nộp “Đơn yêu cầu đặt trước vật liệu bề mặt” như sau: Hạng A ~ từ 100 tấm trở lên; Hạng B ~ từ 50 tấm trở lên; Hạng C ~ từ 20 tấm trở lên; Hạng D ~ tùy từng lần (theo số tấm thép sử dụng). |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |     Tuy nhiên, đối với các loại từ ký hiệu ○ đến Silver Alloy, chỉ nộp đơn đặt trước khi sử dụng từ 300 tấm trở lên. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
## Sheet: Phase1_Note
| <<Overview |  |  |
| --- | --- | --- |
|  | Phase 1 note |  |
|  | Tài liệu 1 |  |
|  |  | 1# |
|  |  | kỳ đầu họ gửi bộ dữ liệu ở path như hình |
|  |  | 2#  |
|  |  | →  lúc đó họ yêu cầu |
|  |  | đối chiếu thông tin ở instruction sheet (do 1 bên khác đặt hàng SANWA làm) như là specs kỹ thuật của bên đặt hàng gửi cho SANWA gia công với file thiết kế trước gia công, do SANWA thực hiện |
|  |  | ①指示書（1タイプ）là file instruction sheet |
|  |  | đoạn ni họ tổ chức instruction sheet ra 1 file PDF riêng |
|  |  | ②図面（４タイプ） |
|  |  | là file thiết kế cửa cuốn (shutter) |
|  |  | nhiệm vụ là kiểm tra xem specs vs thiết kế có chi sai lệch không |
|  |  | hình ảnh instruction sheet |
|  |  | hình ảnh 1 thiết kế |
## Sheet: Drawing
| <<Overview |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | Cách đọc bản vẽ |  |  |  |
|  |  | Đây là bản vẽ mặt bằng (plan) của một cửa đi một cánh mở quay trong bản vẽ kiến trúc Nhật Bản. Mình giải thích từng phần: |  |  |
|  |  | 1. Thông tin phòng và cửa |  |  |
|  |  | 501・604: số phòng/số hiệu cửa áp dụng cho bản vẽ này (phòng 501 và 604, tức cùng loại cửa ở các tầng). |  |  |
|  |  | 5–6F: áp dụng cho tầng 5 đến tầng 6. |  |  |
|  |  | R×2: Right (cửa mở phải) × 2 bộ, tức có 2 cửa loại này. |  |  |
|  |  | 2. Hai phòng hai bên cửa |  |  |
|  |  | 寝室踏込 (Shinshitsu fumikomi): phần "bước vào" phòng ngủ (khu vực ngay sau cửa phía phòng ngủ). |  |  |
|  |  | (FL+2): cao độ sàn cao hơn mặt sàn chuẩn (FL) 2 mm. |  |  |
|  |  | Ghi chú dưới: 床: ビニル床シート t2.0 – Sàn: tấm vinyl dày 2.0 mm. |  |  |
|  |  | 廊下 (Rōka): hành lang. |  |  |
|  |  | (FL+7.5): cao độ sàn cao hơn FL 7.5 mm. |  |  |
|  |  | Ghi chú dưới: 床: タイルカーペット t7.5 – Sàn: thảm tấm (carpet tile) dày 7.5 mm. |  |  |
|  |  | → Hai bên cửa có chênh cao độ sàn 5.5 mm do vật liệu hoàn thiện khác nhau (7.5 − 2). |  |  |
|  |  | 3. Kích thước và trục |  |  |
|  |  | W=800: bề rộng thông thủy (lỗ cửa) 800 mm. |  |  |
|  |  | 470: khoảng cách từ trục X4a đến mép cạnh cửa (màu hồng, kích thước cần lưu ý). |  |  |
|  |  | 390: khoảng cách từ trục Y2 đến mặt tường/khuôn cửa. |  |  |
|  |  | X4a, Y2: các trục lưới của công trình (grid lines), dùng làm mốc định vị. |  |  |
|  |  | 136: kích thước độ dày/bề rộng phần tường hoặc khung ở phía bản lề (đo theo phương đứng, gần ký hiệu サ・シ). |  |  |
|  |  | 4. Ký hiệu サ, シ |  |  |
|  |  | Là ký hiệu tham chiếu chi tiết (ví dụ chi tiết サ, チ... trong bản vẽ chi tiết khuôn cửa), chỉ ra các mặt cắt/chi tiết liên quan tới cửa này. |  |  |
|  |  | 5. Hình vẽ |  |  |
|  |  | Hai đoạn tường có vạch xanh lá/vàng: tường, khuôn cửa và lớp hoàn thiện hai bên. |  |  |
|  |  | Cung tròn màu vàng: quỹ đạo quay của cánh cửa, cho thấy cánh mở về phía hành lang (mở ra ngoài). |  |  |
|  |  | Hình chữ nhật nhỏ ở cạnh cửa: tay nắm/khóa hoặc tấm cánh cửa khi mở. |  |  |
|  |  | 戸当り (Totari): cản cửa/chặn cửa (door stopper), gắn ở vị trí chỉ mũi tên để cánh cửa không đập vào tường. |  |  |
|  |  | Tóm tắt |  |  |
|  |  | Cửa phòng ngủ rộng 800 mm, mở ra phía hành lang, có cản cửa; sàn phòng ngủ là vinyl dày 2 mm, hành lang là thảm tấm dày 7.5 mm, tạo chênh cao nhỏ giữa hai bên. Cửa được định vị theo trục X4a và Y2. |  |  |
|  |  | Nếu bạn có thêm bản vẽ chi tiết (サ, シ) hoặc bảng ký hiệu cửa đi kèm, mình có thể giải thích sâu hơn về cấu tạo khuôn và cánh cửa nhé. |  |  |
|  |  | File 3 |  |  |
|  |  |  | 1. 開閉方向一致 (Hướng mở quay: Đẩy ra ngoài / Kéo vào trong - 外開き/内開き) |  |
|  |  |  | Vì sao không có: Cửa này là cửa trượt ngang lùa vào hộc vách thạch cao (片引き), cánh cửa trượt tịnh tiến theo phương ngang trên ray, hoàn toàn không có bán kính quét hay cung tròn mở quay. |  |
|  |  |  | 2. 親子扉勝手一致 (Tay mở cánh mẹ / cánh con) |  |
|  |  |  | Vì sao không có: Cửa chỉ có đúng 1 cánh đơn duy nhất (片引き L: 1 bộ). Không phải là cửa 2 cánh mẹ con (cánh lớn + cánh nhỏ) nên không thể kiểm tra tỷ lệ hay tay mở mẹ con. |  |
|  |  |  | 3. DC取付側一致 (Phía lắp đặt tay co thủy lực quay - 内観/外観) |  |
|  |  |  | Vì sao không có: Cửa không dùng tay co quay (Door Closer) gắn nổi trên mặt cánh/khung. Cơ cấu tự đóng của cửa được giấu âm hoàn toàn bên trong ray trượt trên trần. |  |
|  |  |  | 4. 通電金具取付一致 (Phụ kiện tiếp điện âm qua bản lề - TEK) |  |
|  |  |  | Vì sao không có: Cửa này hoạt động hoàn toàn bằng cơ cấu cơ học & lò xo bán tự động, không dùng khóa thẻ từ, không dùng chốt điện và không có hệ thống điện cấp vào cánh, nên không cần bản lề tiếp điện (TEK-9CC). |  |
|  |  |  | 5. DC品番一致 (Mã sản phẩm tay co thủy lực quay) |  |
|  |  |  | Vì sao không có: Cửa không dùng tay co của Ryobi/Miwa dạng tay gập tròn thông thường (như B1002P ở File 2). Bộ phận tạo lực kéo và hãm lùi là bộ cơ cấu trượt âm trần chuyên dụng của hệ SAT (引戸ｸﾛｰｻﾞｰ: 三和制定品, gồm 駆動装置 SWSL-2ENT-KU050 và 制動装置 SWSL-1-GE). |  |
|  |  |  | 6. 吊金物一致 (Khe hở và phụ kiện treo cánh: Bản lề lá 丁番 / Pivot Hinge) |  |
|  |  |  | Vì sao không có: Quy tắc kiểm tra ở mục này là đo khe chêm bản lề lá 吊元チリ = 4mm hoặc bản lề cối PH = 3mm. Cửa lùa File (3) được treo bằng cụm con lăn bánh xe (戸車セット SWSL-1-TO) chạy trong ray nhôm treo âm trần (SWSL-1-WA1), không dùng bản lề quay. |  |
|  |  | File 5 |  |  |
|  |  |  | Nắm thăm kĩ thuật |  |
|  |  |  | Tay co thủy lực |  |
|  |  |  | Cối xoay chịu lực |  |
|  |  |  | Hướng mở cánh mẹ, con |  |
|  |  |  |  | Thuật ngữ シ-サ (hay viết liền là シーサ) trong ghi chú: |
|  |  |  |  | 平面のシ-サの方向も確認 (Đối chiếu cả hướng của シ-サ trên mặt bằng) |
|  |  |  |  | 1. Giải mã: シ-サ thực chất là gì? |
|  |  |  |  | Trước đây trong một số bản nháp dịch máy (như ở sheet DryRun) từng có chỗ dịch nhầm thành "hướng vân (sheet)". Điều đó hoàn toàn không chính xác! |
|  |  |  |  | Trong chuyên ngành cửa và khóa kiến trúc Nhật Bản: |
|  |  |  |  | シ = Viết tắt của シリンダー (Cylinder): Ổ cắm chìa khóa (mặt tra chìa). |
|  |  |  |  | サ = Viết tắt của サムターン (Thumbturn): Núm vặn chốt cơ học bằng tay từ bên trong. |
|  |  |  |  | Bằng chứng rõ nhất nằm ngay ở tiêu chí số ⑨ (錠前品番一致) trong tài liệu No.7: |
|  |  |  |  | 美和の場合、 LA－１がシーサ、-2 がシー空等 |
|  |  |  |  | (Đối với khóa hãng MIWA: mã LA-1 là loại khóa có 1 đầu chìa (シ) và 1 đầu núm vặn (サ); còn LA-2 là loại chìa ngoài - trống trong). |
|  |  |  |  | 2. Ký hiệu (シ) và (サ) hiển thị ở đâu trên bản vẽ? |
|  |  |  |  | Nếu quan sát trích đoạn mặt bằng nằm dưới hình dáng mặt đứng (姿図) trên các sheet bản vẽ chi tiết: |
|  |  |  |  | Ở hai bên cánh cửa, người thiết kế luôn vẽ 2 vòng tròn nhỏ có chữ bên trong: |
|  |  |  |  | Vòng tròn có chữ シ: Đặt ở phía ngoài phòng / hành lang (phía người muốn vào phải tra chìa khóa). |
|  |  |  |  | Vòng tròn có chữ サ: Đặt ở phía trong phòng (phía người bên trong chỉ cần xoay núm vặn chốt là mở được cửa thoát ra). |
|  |  |  |  | 3. Mục đích kiểm tra: "平面のシ-サの方向も確認" là làm gì? |
|  |  |  |  | Đối với cửa 2 cánh mẹ con (親子扉), tiêu chí này kiểm tra 3 vấn đề an toàn và công năng cốt tử: |
|  |  |  |  | 1. Kiểm tra không bị lắp lộn mặt Trong ↔ Ngoài (Indoor vs. Outdoor): |
|  |  |  |  | Đảm bảo ổ cắm chìa (シ) phải quay ra phía hành lang/sảnh ngoài, và núm vặn chốt (サ) phải quay vào lòng phòng. |
|  |  |  |  | Nếu vẽ ngược: Người ngoài hành lang không khóa được cửa, còn người bên trong nếu không có chìa sẽ bị nhốt bên trong (vi phạm tiêu chuẩn phòng cháy chữa cháy). |
|  |  |  |  | 2. Xác định cánh mẹ gắn khóa nằm ở đâu: |
|  |  |  |  | Cặp ký hiệu (シ) và (サ) luôn được đặt ngay tại vị trí mép khóa của cánh mẹ (cánh mở chính), chứ không nằm ở cánh con (cánh phụ chốt âm). Nhìn vào vị trí chữ シ và サ là AI biết ngay cánh mẹ nằm bên trái hay bên phải. |
|  |  |  |  | 3. Đối chiếu đồng nhất giữa Key Plan và Sheet chi tiết: |
|  |  |  |  | Đảm bảo hướng quay của (シ) và (サ) trên mặt bằng chi tiết phải khớp 100% với hướng quy ước trên mặt bằng tổng thể toà nhà (Key Plan), không bị xoay ngược hướng khi xoay bản vẽ 90 độ. |
|  |  |  |  | 🎯 Ý nghĩa đối với bài toán phát triển AI: |
|  |  |  |  | Đây là bài toán nhận diện ký hiệu hình ảnh (Symbol Detection / VLM) kết hợp suy luận không gian: |
|  |  |  |  | AI cần bóc tách được tọa độ của 2 ký hiệu hình tròn (シ) và (サ). |
|  |  |  |  | So sánh vị trí của (シ) và (サ) so với đường biên tường để xác định chính xác đâu là mặt ngoài, đâu là mặt trong, từ đó xác nhận tay mở của cánh mẹ con là hoàn toàn đúng kỹ thuật. |
|  |  |  |  | 1. Nghiệp vụ kiểm tra ((シ) Cylinder ngoài / (サ) Thumbturn trong): |
|  |  |  |  | Hướng Trong ↔ Ngoài: Đảm bảo (シ) quay ra hành lang, (サ) quay vào trong phòng. |
|  |  |  |  | Xác định cánh mẹ: Cặp (シ)-(サ) nằm ở cánh nào thì cánh đó là cánh mẹ (cánh mở chính). |
|  |  |  |  | Khớp Key Plan: Hướng xoay của (シ)-(サ) trên chi tiết phải khớp 100% với mặt bằng tổng thể. |
|  |  |  |  | 2. Phương thức AI thực hiện: |
|  |  |  |  | Kết hợp Symbol Detection (VLM) nhận diện tọa độ (シ), (サ) và Suy luận không gian (Spatial Reasoning) so với tường/Key Plan. |
## Sheet: DoorInfo
| <<Overview |  |  |
| --- | --- | --- |
|  | Thông tin các cửa |  |
|  |  | File5: 検図対象項目と読取先（No.5_SD-1） |
|  |  | Loại cửa: Cửa lùa học đường hệ ray treo nhẹ スムードLS3（手動） |
|  |  | Đặc điểm: Cửa trượt 1 cánh (片引き), có ô kính quan sát (窓あり), có nắp thăm kỹ thuật ray (点検口), dùng tay kéo 引き棒: シブタニ S725G-H-P425 |
|  |  | File 7:  |
|  |  | 第9回 八潮市立新設小学校(LD 1F) |
|  |  | 検図対象項目と読取先（No.7） |
|  |  | Loại cửa: Cửa thép mở quay hai cánh lệch mẹ con có ô nan chớp (LD - 鋼製開き戸 親子扉 ガラリ付) |
|  |  | Đặc điểm: Cửa mở quay ngoài (外開き), chia tỷ lệ cánh mẹ con (DW1/DW2), có ô nan chớp thông gió rất lớn (ガラリあり), dùng khóa điện kèm phụ kiện tiếp điện bản lề (通電金具 TEK-9CC). |
## Sheet: Smood
| <<Overview |  |  |  |
| --- | --- | --- | --- |
|  | Sanwa Lightweight Sliding Doors |  |  |
|  | Sanwa Lightweight Sliding Doors - Cửa trượt trọng lượng nhẹ Sanwa |  |  |
|  |  | Smooth S Series |  |
|  |  |  | LS3 type |
|  |  |  | S type |
|  |  |  | Loại bỏ không gian chết |
|  |  |  | Không có khung đáy |
|  |  |  | Tự động đóng lại |
|  |  |  | 引残し |
|  |  |  | Cửa sổ và cửa chớp |
|  |  |  | Ổ khóa |
|  |  | Nút chặn cuối |  |
|  |  | Cửa sổ RG |  |
|  |  | RG Galari |  |
|  |  | Loại tích hợp RG |  |
|  |  | 戸袋ボード納まり |  |
|  |  | Chi tiết lắp đặt tấm ốp cho hốc chứa cửa trượt |  |
|  |  |  | ※［　］内は引き残し110mmの場合を示し、 窓・ガラリなしの場合に適用できます。 |
|  |  |  | ※ Phần trong dấu ［　］ áp dụng cho trường hợp để lại khoảng hở 110mm, |
|  |  |  | và có thể áp dụng khi không có cửa sổ hoặc cửa chớp. |
|  |  |  | Note: chỗ này xem lại vụ phần chừa có thể 150mm hoặc 110mm |
|  |  |  | ※［　］内は引き残し110mmの場合を示し、 窓・ガラリなしの場合に適用できます |
|  |  |  | ※ Các thông số trong dấu ［　］ áp dụng cho trường hợp khoảng hở còn lại là 110mm, |
|  |  |  | và có thể áp dụng khi không có cửa sổ hoặc cửa chớp. |
|  |  | Cửa đôi |  |
## Sheet: 引残し
| <<Overview |  |  |
| --- | --- | --- |
|  | Smood  |  |
|  |  | Thực tế chính catalog đã tự chứng minh điều đó bằng các công thức có cả: |
|  |  | 150 mm (chuẩn) |
|  |  | 110 mm (exception khi không có window/grille) |
|  |  | 105/115 mm ở các series khác. |
|  |  | 1. Về phía Instruction: |
|  |  | Trên Phiếu chỉ thị (Instruction) hoàn toàn KHÔNG CÓ mục 引残し. |
|  |  | Do đó, đây không phải là bài toán so sánh Instruction ↔ Drawing, mà là bài toán Drawing ↔ Master Spec / Bộ tiêu chuẩn (hoặc Drawing ↔ Drawing): |
|  |  | Đối chiếu kích thước 引残し vẽ trên mặt đứng/mặt cắt (姿図/詳細図) với công thức quan hệ chuẩn (関係式: 有効開口 = W - 引残し). |
|  |  | 2. Có phải "luôn luôn kiểm tra 引残し = 150 (hardcode)" được không? |
|  |  | 👉 Với 80–90% trường hợp thông thường: CÓ THỂ coi 150mm là giá trị mặc định (Default Standard), NHƯNG KHÔNG NÊN HARDCODE CHẾT 100% CHO MỌI LOẠI CỬA. |
|  |  | Lý do nằm ngay trong các trang quy chuẩn của catalogue D-183.pdf: |
|  |  | 1. Khi cửa CÓ ô kính / chớp thoáng (窓・ガラリ有): |
|  |  | Đúng như trang 11 D-183.pdf mô tả: Để tránh nguy cơ người dùng bị kẹt ngón tay vào khe hộc tường (戸袋) khi mở cửa, tiêu chuẩn an toàn quốc gia (自動ドア安全ガイドライン) bắt buộc 引残し = 150mm. |
|  |  | Lúc này công thức bắt buộc là: 有効開口 = W - 150. |
|  |  | 2. Khi cửa KHÔNG CÓ ô kính / chớp (窓・ガラリなし): |
|  |  | Catalogue cho phép lựa chọn option hẹp hơn: 引残し = 110mm (hoặc 105mm), để tăng độ mở thông thủy. |
|  |  | Lúc này công thức trong catalogue đổi thành: 有効開口 = W - 110. |
|  |  | 3. Các dòng cửa trượt đặc thù khác (Special Models): |
|  |  | Dòng mở toàn phần (フルオープン - Trang 26): 引残し cố định là 220mm. |
|  |  | Dòng khoang rộng (広幅間 - Trang 27): 引残し là 175mm. |
|  |  | Dòng cửa góc (コーナータイプ - Trang 25): 引残し là 160mm. |
|  |  | Dòng cửa chung cư (悠楽 - Trang 30): 引残し tiêu chuẩn là 115mm. |
|  |  | 3. Logic kiểm tra tối ưu nhất cho AI Pipeline: |
|  |  | Thay vì hardcode cứng số 150 vào code: |
|  |  | Rule kiểm tra: |
|  |  | 1. Trích xuất giá trị 引残し dóng kích thước trên bản vẽ chi tiết (姿図/詳細図). |
|  |  | 2. Trích xuất thông số chiều rộng cửa W và độ mở thông thủy 有効開口. |
|  |  | 3. Kiểm tra tính toàn vẹn quan hệ toán học: |
|  |  | \[\mathbf{W - 有効開口 == 引残し}\] |
|  |  | 4. Nếu cửa có 窓 hoặc ガラリ, kiểm tra thêm điều kiện an toàn: \(\mathbf{引残し \ge 150mm}\). |
|  |  | ✍️ Gợi ý câu note ngắn gọn vào ô Comment của Pipeline: |
|  |  | "Instruction không có mục 引残し. Tiêu chuẩn an toàn tự động (D-183 P.11) quy định mặc định 引残し = 150mm (khi có ô kính/chớp để chống kẹt tay). AI kiểm tra kích thước 引残し trên bản vẽ chi tiết (姿図/詳細図) và đối chiếu với công thức quan hệ 有効開口 = W - 引残し. Không nên hardcode cứng vì dòng không ô kính có thể là 110mm, dòng đặc thù có thể là 175/220mm." |
## Sheet: LSD
| <<Overview |  |  |
| --- | --- | --- |
|  | LSD |  |
|  | Cửa sổ |  |
|  | Garali |  |
## Sheet: Run_Build
| <<Overview |  |  |  |
| --- | --- | --- | --- |
|  | Run & Build |  |  |
|  | Restart lại Backend Spring Boot |  |  |
|  |  | Mở powershell |  |
|  |  |  | cd c:\work\Projects\Jewelry\02.GIT\spring-modulith-demo |
|  |  |  | .\mvnw.cmd spring-boot:run |
|  |  |  Trong trường hợp sau này port 8080 bị chiếm và bạn muốn tắt đi rồi bật lại ngay trong 1 lần gõ, bạn có thể dùng tổ hợp lệnh này trong PowerShell |  |
|  |  |  | # 1. Tắt tiến trình đang chạy ở port 8080 (nếu có) |
|  |  |  | Stop-Process -Id (Get-NetTCPConnection -LocalPort 8080 -State Listen -ErrorAction SilentlyContinue).OwningProcess -Force -ErrorAction SilentlyContinue |
|  |  |  | # 2. Khởi động lại Spring Boot |
|  |  |  | .\mvnw.cmd spring-boot:run |
|  |  | Hoặc nếu bạn dùng IDE (VS Code / IntelliJ IDEA): chỉ cần mở file  |  |
|  |  |  | JewelryApplication.java và bấm nút Run (mũi tên màu xanh) là được. |
|  | Xung đột JDK 25, 21 khi build báo lỗi sau |  |  |
|  |  | [INFO] BUILD FAILURE |  |
|  |  | [INFO] ------------------------------------------------------------------------ |  |
|  |  | [INFO] ------------------------------------------------------------------------ |  |
|  |  | [INFO] ------------------------------------------------------------------------ |  |
|  |  | [INFO] ------------------------------------------------------------------------ |  |
|  |  | [INFO] Total time:  3.622 s                                                                                                                                               work.boot:spring-boo |  |
|  |  | [INFO] Finished at: 2026-10-15T08:48:07+07:00 |  |
|  |  | [INFO] ------------------------------------------------------------------------ |  |
|  |  | [ERROR] Failed to execute goal org.springframework.boot:spring-boot-maven-plugin:3.2.4:run (default-cli) on project jewelry: Execution default-cli of goal org.springframemework.boot:spring-boot-maven-plugin:3.2.4:run failed: Unsupported class file major version 69 -> [Help 1] |  |
|  |  | [ERROR] |  |
|  |  | [ERROR] To see the full stack trace of the errors, re-run Maven with the -e switch. |  |
|  |  | [ERROR] Re-run Maven using the -X switch to enable full debug logging. |  |
|  |  | [ERROR] |  |
|  |  | [ERROR] For more information about the errors and possible solutions, please read the following articles: |  |
|  | Cách xử lí |  |  |
|  |  | Dọn dẹp và biên dịch lại toàn bộ bằng JDK 21: |  |
|  |  | powershell |  |
|  |  | .\mvnw.cmd clean compile |  |
|  |  | Sau khi clean, toàn bộ class file đã được biên dịch lại chuẩn Java 21 (major version: 65). |  |
|  |  | Kiểm tra chạy thử ứng dụng: Ứng dụng đã được chạy thử nghiệm thành công: |  |
|  |  | text |  |
|  |  | Tomcat started on port 8080 (http) with context path '' |  |
|  |  | Started JewelryApplication in 3.338 seconds |  |
|  |  | Cách chạy lại dự án |  |
|  |  | Bây giờ bạn có thể khởi động lại ứng dụng bình thường bằng lệnh: |  |
|  |  | powershell |  |
|  |  | .\mvnw.cmd spring-boot:run |  |