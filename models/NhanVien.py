from db import DbConnection
from models import SimpleModel
from utils import hash_password

QuyenHan = {
    "NHAN_VIEN": 1,
    "QUAN_LY": 2
}


class NhanVien(SimpleModel):
    _table_name = "NhanVien"
    _properties = ["id", "ten_nv", "dia_chi", "sdt", "email", "vai_tro", "ten_dang_nhap", "mat_khau", "quyen_han", "created_at", "updated_at"]

    def __init__(self, ten_nv: str = None, dia_chi: str = None, sdt: str = None, email: str = None, vai_tro: str = None, ten_dang_nhap: str = None, mat_khau: str = None):
        super().__init__()
        self.ten_nv = ten_nv
        self.dia_chi = dia_chi
        self.sdt = sdt
        self.email = email
        self.vai_tro = vai_tro
        self.ten_dang_nhap = ten_dang_nhap
        self.mat_khau = hash_password(mat_khau)
        self.quyen_han = QuyenHan["NHAN_VIEN"]

    def __str__(self):
        return f"{self.id} - {self.ten_nv} - {self.dia_chi} - {self.sdt} - {self.email} - {self.vai_tro} - {self.ten_dang_nhap} - {self.quyen_han}"

    def update(self, ten_nv = None, dia_chi = None, sdt = None, email = None, vai_tro = None, ten_dang_nhap = None, mat_khau = None, with_save = True):
        if ten_nv:
            self.ten_nv = ten_nv
        if dia_chi:
            self.dia_chi = dia_chi
        if sdt:
            self.sdt = sdt
        if email:
            self.email = email
        if vai_tro:
            self.vai_tro = vai_tro
        if ten_dang_nhap:
            self.ten_dang_nhap = ten_dang_nhap
        if mat_khau:
            self.mat_khau = hash_password(mat_khau)
        if with_save:
            self.save()

    def make_admin(self):
        self.quyen_han = QuyenHan["QUAN_LY"]
        self.save()

    @classmethod
    def dang_nhap(cls, ten_dang_nhap: str, mat_khau: str) -> bool:
        if ten_dang_nhap is None or mat_khau is None:
            return False
        return DbConnection.fetch_all(cls, {"ten_dang_nhap": ten_dang_nhap, "mat_khau": hash_password(mat_khau)}) != []
