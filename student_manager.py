"""Chương trình quản lý sinh viên đơn giản (CLI)."""


def them_sinh_vien(danh_sach, mssv, ho_ten, ngay_sinh, gpa):
    """Thêm sinh viên mới. Trả về (True, msg) hoặc (False, msg)."""
    if tim_sinh_vien(danh_sach, mssv) is not None:
        return False, f"MSSV {mssv} đã tồn tại."
    if not (0 <= gpa <= 4):
        return False, "GPA phải trong khoảng 0-4."
    danh_sach.append({
        "mssv": mssv,
        "ho_ten": ho_ten,
        "ngay_sinh": ngay_sinh,
        "gpa": gpa,
    })
    return True, f"Đã thêm sinh viên {ho_ten}."


def tim_sinh_vien(danh_sach, mssv):
    """Trả về dict sinh viên nếu tìm thấy, ngược lại None."""
    for sv in danh_sach:
        if sv["mssv"] == mssv:
            return sv
    return None


def sua_sinh_vien(danh_sach, mssv, **thay_doi):
    """Sửa thông tin sinh viên theo MSSV. thay_doi là các field cần đổi."""
    sv = tim_sinh_vien(danh_sach, mssv)
    if sv is None:
        return False, f"Không tìm thấy MSSV {mssv}."
    if "gpa" in thay_doi and not (0 <= thay_doi["gpa"] <= 4):
        return False, "GPA phải trong khoảng 0-4."
    sv.update(thay_doi)
    return True, f"Đã cập nhật MSSV {mssv}."


def xoa_sinh_vien(danh_sach, mssv):
    """Xóa sinh viên theo MSSV."""
    sv = tim_sinh_vien(danh_sach, mssv)
    if sv is None:
        return False, f"Không tìm thấy MSSV {mssv}."
    danh_sach.remove(sv)
    return True, f"Đã xóa MSSV {mssv}."


def xem_danh_sach(danh_sach):
    """Trả về danh sách dạng chuỗi để in ra màn hình."""
    if not danh_sach:
        return "Danh sách trống."
    dong = []
    for sv in danh_sach:
        dong.append(
            f"{sv['mssv']} | {sv['ho_ten']} | {sv['ngay_sinh']} | GPA: {sv['gpa']}"
        )
    return "\n".join(dong)


def menu_chinh():
    """Vòng lặp menu console chính."""
    danh_sach = []
    menu = """
--- QUẢN LÝ SINH VIÊN ---
1. Thêm sinh viên
2. Xem danh sách
3. Tìm sinh viên
4. Sửa sinh viên
5. Xóa sinh viên
6. Thoát
Chọn: """

    while True:
        chon = input(menu).strip()

        if chon == "1":
            mssv = input("MSSV: ").strip()
            ho_ten = input("Họ tên: ").strip()
            ngay_sinh = input("Ngày sinh (dd/mm/yyyy): ").strip()
            try:
                gpa = float(input("GPA (0-4): ").strip())
            except ValueError:
                print("Lỗi: GPA phải là số.")
                continue
            ok, msg = them_sinh_vien(danh_sach, mssv, ho_ten, ngay_sinh, gpa)
            print(msg)

        elif chon == "2":
            print(xem_danh_sach(danh_sach))

        elif chon == "3":
            mssv = input("Nhập MSSV cần tìm: ").strip()
            sv = tim_sinh_vien(danh_sach, mssv)
            print(sv if sv else f"Không tìm thấy MSSV {mssv}.")

        elif chon == "4":
            mssv = input("Nhập MSSV cần sửa: ").strip()
            ho_ten = input("Họ tên mới (Enter để bỏ qua): ").strip()
            thay_doi = {}
            if ho_ten:
                thay_doi["ho_ten"] = ho_ten
            gpa_str = input("GPA mới (Enter để bỏ qua): ").strip()
            if gpa_str:
                try:
                    thay_doi["gpa"] = float(gpa_str)
                except ValueError:
                    print("Lỗi: GPA phải là số.")
                    continue
            ok, msg = sua_sinh_vien(danh_sach, mssv, **thay_doi)
            print(msg)

        elif chon == "5":
            mssv = input("Nhập MSSV cần xóa: ").strip()
            ok, msg = xoa_sinh_vien(danh_sach, mssv)
            print(msg)

        elif chon == "6":
            print("Tạm biệt!")
            break

        else:
            print("Lựa chọn không hợp lệ.")


if __name__ == "__main__":
    menu_chinh()
