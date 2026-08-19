# Chương trình Quản lý Sinh viên

Chương trình CLI đơn giản bằng Python để quản lý danh sách sinh viên: thêm, xem, tìm, sửa, xóa.

## Cài đặt

Yêu cầu Python 3.8+. Không cần thư viện ngoài để chạy chương trình chính.

```bash
git clone https://github.com/Back-dev6/Lab-01.git
cd Lab-01
```

## Chạy chương trình

```bash
python student_manager.py
```

Làm theo menu hiện ra trên màn hình để thêm/xem/tìm/sửa/xóa sinh viên.

## Chạy test

```bash
pip install pytest
pytest test_student_manager.py -v
```

## Cấu trúc dữ liệu

Mỗi sinh viên gồm: MSSV (duy nhất), họ tên, ngày sinh, GPA (0–4).

## Ghi chú về việc dùng AI

Dự án này được xây dựng theo quy trình 7 bước có dùng AI hỗ trợ ở mỗi bước
(phân tích, thiết kế, sinh code, debug, viết test, refactor, viết README).
Chi tiết prompt đã dùng và nhận xét AI làm đúng/sai được ghi trong `PROMPT_LOG.md`.

## License

MIT — xem file `LICENSE`.
