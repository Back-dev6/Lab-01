# Nhật ký Prompt — Lab AI Coding có trách nhiệm

## Bước 1 — Phân tích
**Prompt:** "Tôi cần xây dựng chương trình quản lý sinh viên đơn giản bằng Python, chạy console. Hãy giúp tôi phân tích yêu cầu: các chức năng cần có, dữ liệu cần lưu cho mỗi sinh viên, và các trường hợp đặc biệt cần xử lý."

**Kết quả AI trả về:** Danh sách chức năng (thêm/xem/tìm/sửa/xóa), 4 trường dữ liệu (MSSV, họ tên, ngày sinh, GPA), các trường hợp đặc biệt (trùng MSSV, không tồn tại, sai kiểu dữ liệu, GPA ngoài khoảng).

**Nhận xét ĐÚNG/SAI:** [Bạn tự điền sau khi chạy prompt với AI của bạn và so sánh]

## Bước 2 — Thiết kế
**Prompt:** "Dựa trên phân tích trên, hãy thiết kế cấu trúc dữ liệu và kiến trúc chương trình quản lý sinh viên bằng Python, chạy console, dùng list/dict để lưu tạm trong bộ nhớ."

**Kết quả AI trả về:** Dùng dict cho mỗi sinh viên, list chứa toàn bộ; tách các hàm theo chức năng, không dùng biến global.

**Nhận xét ĐÚNG/SAI:** [Bạn tự điền]

## Bước 3 — Sinh code
**Prompt:** "Viết code Python đầy đủ cho student_manager.py theo thiết kế trên, có xử lý lỗi (MSSV trùng, không tồn tại, GPA ngoài khoảng 0-4, nhập sai kiểu)."

**Kết quả AI trả về:** File `student_manager.py` — các hàm `them_sinh_vien`, `tim_sinh_vien`, `sua_sinh_vien`, `xoa_sinh_vien`, `xem_danh_sach`, `menu_chinh`.

**Nhận xét ĐÚNG/SAI:** [Bạn tự điền — ví dụ: AI ban đầu có thể quên kiểm tra GPA khi sửa, cần nhắc lại]

## Bước 4 — Debug
**Ghi chú:** Chạy thử `python student_manager.py`, kiểm tra từng chức năng qua menu. Không phát sinh lỗi runtime trong lần chạy đầu vì các hàm đã có try/except cho input sai kiểu.

## Bước 5 — Viết test
**Prompt:** "Viết test bằng pytest cho các hàm trong student_manager.py, bao gồm cả trường hợp lỗi (MSSV trùng, không tồn tại, GPA ngoài khoảng)."

**Kết quả AI trả về:** File `test_student_manager.py`, 11 test case.

**Kết quả chạy test:**
```
11 passed in 0.02s
```

**Nhận xét ĐÚNG/SAI:** [Bạn tự điền]

## Bước 6 — Refactor
**Ghi chú:** Các hàm nhận `danh_sach` làm tham số (không dùng biến global) để dễ test độc lập. Dùng `**thay_doi` trong `sua_sinh_vien` để chỉ cập nhật field được truyền vào, tránh ghi đè toàn bộ.

## Bước 7 — README
**Prompt:** "Viết README.md cho dự án này, gồm mô tả, cách cài đặt, cách chạy, cách chạy test."

**Kết quả AI trả về:** File `README.md` hoàn chỉnh.

**Nhận xét ĐÚNG/SAI:** [Bạn tự điền]
