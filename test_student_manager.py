"""Test cho student_manager.py — chạy: pytest test_student_manager.py -v"""
import pytest
from student_manager import (
    them_sinh_vien, tim_sinh_vien, sua_sinh_vien, xoa_sinh_vien, xem_danh_sach
)


@pytest.fixture
def danh_sach():
    return []


def test_them_sinh_vien_thanh_cong(danh_sach):
    ok, msg = them_sinh_vien(danh_sach, "SV001", "Nguyễn Văn A", "01/01/2005", 3.5)
    assert ok is True
    assert len(danh_sach) == 1


def test_them_mssv_trung(danh_sach):
    them_sinh_vien(danh_sach, "SV001", "A", "01/01/2005", 3.5)
    ok, msg = them_sinh_vien(danh_sach, "SV001", "B", "02/02/2005", 3.0)
    assert ok is False
    assert "đã tồn tại" in msg


def test_them_gpa_ngoai_khoang(danh_sach):
    ok, msg = them_sinh_vien(danh_sach, "SV002", "B", "01/01/2005", 5.0)
    assert ok is False


def test_tim_sinh_vien_ton_tai(danh_sach):
    them_sinh_vien(danh_sach, "SV001", "A", "01/01/2005", 3.5)
    sv = tim_sinh_vien(danh_sach, "SV001")
    assert sv is not None
    assert sv["ho_ten"] == "A"


def test_tim_sinh_vien_khong_ton_tai(danh_sach):
    assert tim_sinh_vien(danh_sach, "SV999") is None


def test_sua_sinh_vien_thanh_cong(danh_sach):
    them_sinh_vien(danh_sach, "SV001", "A", "01/01/2005", 3.5)
    ok, msg = sua_sinh_vien(danh_sach, "SV001", gpa=4.0)
    assert ok is True
    assert tim_sinh_vien(danh_sach, "SV001")["gpa"] == 4.0


def test_sua_sinh_vien_khong_ton_tai(danh_sach):
    ok, msg = sua_sinh_vien(danh_sach, "SV999", gpa=4.0)
    assert ok is False


def test_xoa_sinh_vien_thanh_cong(danh_sach):
    them_sinh_vien(danh_sach, "SV001", "A", "01/01/2005", 3.5)
    ok, msg = xoa_sinh_vien(danh_sach, "SV001")
    assert ok is True
    assert len(danh_sach) == 0


def test_xoa_sinh_vien_khong_ton_tai(danh_sach):
    ok, msg = xoa_sinh_vien(danh_sach, "SV999")
    assert ok is False


def test_xem_danh_sach_trong(danh_sach):
    assert xem_danh_sach(danh_sach) == "Danh sách trống."


def test_xem_danh_sach_co_du_lieu(danh_sach):
    them_sinh_vien(danh_sach, "SV001", "A", "01/01/2005", 3.5)
    ket_qua = xem_danh_sach(danh_sach)
    assert "SV001" in ket_qua
