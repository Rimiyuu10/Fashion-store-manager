from db import DbConnection
from models import SimpleModel, SanPham, ChiTietDonHang

TrangThaiDonHang = {
    "DANG_XU_LY": 1,
    "DANG_GIAO": 2,
    "DA_GIAO": 3,
    "DA_HUY": 4
}


class DonHang(SimpleModel):
    _table_name = "DonHang"
    _properties = ["id", "nguoi_mua", "sdt_nguoi_mua", "dia_chi_giao_hang", "trang_thai", "tong_tien", "created_at", "updated_at"]

    def __init__(self, nguoi_mua: str = None, sdt_nguoi_mua: str = None, dia_chi_giao_hang: str = None):
        super().__init__()
        self.nguoi_mua = nguoi_mua
        self.sdt_nguoi_mua = sdt_nguoi_mua
        self.dia_chi_giao_hang = dia_chi_giao_hang
        self.ds_sp = []
        self.tong_tien = 0
        self.trang_thai = TrangThaiDonHang["DANG_XU_LY"]

    def __str__(self):
        return f"{self.id} - {self.nguoi_mua} - {self.sdt_nguoi_mua} - {self.dia_chi_giao_hang}"

    def update(self, nguoi_mua: str = None, sdt_nguoi_mua: str = None, dia_chi_giao_hang: str = None, with_save = True):
        if nguoi_mua:
            self.nguoi_mua = nguoi_mua
        if sdt_nguoi_mua:
            self.sdt_nguoi_mua = sdt_nguoi_mua
        if dia_chi_giao_hang:
            self.dia_chi_giao_hang = dia_chi_giao_hang
        if with_save:
            self.save()

    def dang_giao_hang(self):
        self.trang_thai = TrangThaiDonHang["DANG_GIAO"]
        self.save()

    def da_giao_hang(self):
        self.trang_thai = TrangThaiDonHang["DA_GIAO"]
        self.save()

    def huy_don_hang(self):
        self.trang_thai = TrangThaiDonHang["DA_HUY"]
        self.save()
        ds = ChiTietDonHang.fetch_all({"id_don_hang": self.id})
        for chi_tiet in ds:
            san_pham = SanPham.fetch_all({"id": chi_tiet.id_san_pham})[0]
            san_pham.so_luong_s += chi_tiet.so_luong_s
            san_pham.so_luong_m += chi_tiet.so_luong_m
            san_pham.so_luong_l += chi_tiet.so_luong_l
            san_pham.so_luong_xl += chi_tiet.so_luong_xl
            san_pham.save()

    def them_sp(self, id_san_pham: str, so_luong_s: int, so_luong_m: int, so_luong_l: int, so_luong_xl: int, don_gia: float):
        chi_tiet = ChiTietDonHang(self.id, id_san_pham, so_luong_s, so_luong_m, so_luong_l, so_luong_xl, don_gia)
        self.tong_tien += don_gia
        chi_tiet.save()
        sp = SanPham.fetch_all({"id": id_san_pham})[0]
        sp.so_luong_s -= so_luong_s
        sp.so_luong_m -= so_luong_m
        sp.so_luong_l -= so_luong_l
        sp.so_luong_xl -= so_luong_xl
        sp.save()
        self.save()

    def cap_nhat_sp(self, id_san_pham: str, so_luong_s: int, so_luong_m: int, so_luong_l: int, so_luong_xl: int, don_gia: float):
        chi_tiet = ChiTietDonHang.fetch_all({"id_don_hang": self.id, "id_san_pham": id_san_pham})
        if not chi_tiet:
            return
        chi_tiet = chi_tiet[0]
        sl_s_cu = chi_tiet.so_luong_s
        sl_m_cu = chi_tiet.so_luong_m
        sl_l_cu = chi_tiet.so_luong_l
        sl_xl_cu = chi_tiet.so_luong_xl
        self.tong_tien -= chi_tiet.don_gia
        chi_tiet.update(so_luong_s, so_luong_m, so_luong_l, so_luong_xl, don_gia)
        self.tong_tien += don_gia
        self.save()
        sp = SanPham.fetch_all({"id": id_san_pham})[0]
        sp.so_luong_s += sl_s_cu - so_luong_s
        sp.so_luong_m += sl_m_cu - so_luong_m
        sp.so_luong_l += sl_l_cu - so_luong_l
        sp.so_luong_xl += sl_xl_cu - so_luong_xl
        sp.save()


    def xoa_sp(self, id_san_pham: str):
        chi_tiet = ChiTietDonHang.fetch_all({"id_don_hang": self.id, "id_san_pham": id_san_pham})
        if not chi_tiet:
            return
        chi_tiet = chi_tiet[0]
        self.tong_tien -= chi_tiet.don_gia
        sp = SanPham.fetch_all({"id": id_san_pham})[0]
        sp.so_luong_s += chi_tiet.so_luong_s
        sp.so_luong_m += chi_tiet.so_luong_m
        sp.so_luong_l += chi_tiet.so_luong_l
        sp.so_luong_xl += chi_tiet.so_luong_xl
        sp.save()
        chi_tiet.delete()
        self.save()

    def delete(self):
        self.huy_don_hang()

    @classmethod
    def tong_doanh_thu(cls):
        return DbConnection.sum(cls, "tong_tien", where={"trang_thai": TrangThaiDonHang["DA_GIAO"]})
