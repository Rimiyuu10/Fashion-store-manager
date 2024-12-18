from models import SimpleModel


class ChiTietDonHang(SimpleModel):
    _table_name = "ChiTietDonHang"
    _properties = ["id", "id_don_hang", "id_san_pham", "so_luong_s", "so_luong_m", "so_luong_l", "so_luong_xl", "don_gia", "created_at", "updated_at"]

    def __init__(self, id_don_hang: str = None, id_san_pham: str = None, so_luong_s: int = None, so_luong_m: int = None, so_luong_l: int = None, so_luong_xl: int = None, don_gia: float = None):
        super().__init__()
        self.id_don_hang = id_don_hang
        self.id_san_pham = id_san_pham
        self.so_luong_s = so_luong_s
        self.so_luong_m = so_luong_m
        self.so_luong_l = so_luong_l
        self.so_luong_xl = so_luong_xl
        self.don_gia = don_gia

    def __str__(self):
        return f"{self.id} - {self.id_don_hang} - {self.id_san_pham} - {self.so_luong_s} - {self.so_luong_m} - {self.so_luong_l} - {self.so_luong_xl} - {self.don_gia}"

    def update(self, so_luong_s = None, so_luong_m = None, so_luong_l = None, so_luong_xl = None, don_gia = None, with_save = True):
        if so_luong_s:
            self.so_luong_s = so_luong_s
        if so_luong_m:
            self.so_luong_m = so_luong_m
        if so_luong_l:
            self.so_luong_l = so_luong_l
        if so_luong_xl:
            self.so_luong_xl = so_luong_xl
        if don_gia:
            self.don_gia = don_gia
        if with_save:
            self.save()
