from models import SimpleModel


class SanPham(SimpleModel):
    _table_name = "SanPham"
    _properties = ["id", "ten_sp", "mo_ta", "gia", "so_luong_s", "so_luong_m", "so_luong_l", "so_luong_xl", "hinh_anh", "mau_sac", "created_at", "updated_at"]

    def __init__(self, ten_sp: str = None, mo_ta: str = None, gia: float = None, so_luong_s: int = None, so_luong_m: int = None, so_luong_l: int = None, so_luong_xl: int = None, mau_sac: str = None, hinh_anh: str = None):
        super().__init__()
        self.ten_sp = ten_sp
        self.mo_ta = mo_ta
        self.gia = gia
        self.so_luong_s = so_luong_s
        self.so_luong_m = so_luong_m
        self.so_luong_l = so_luong_l
        self.so_luong_xl = so_luong_xl
        self.mau_sac = mau_sac
        self.hinh_anh = hinh_anh

    def __str__(self):
        return (f"{self.id} - {self.ten_sp} - {self.gia} - {self.so_luong_s} - {self.so_luong_m} - {self.so_luong_l} - {self.so_luong_xl} - {self.mau_sac}")

    def update(self, ten_sp = None, mo_ta = None, gia = None, so_luong_s = None, so_luong_m = None, so_luong_l = None, so_luong_xl = None, mau_sac = None, hinh_anh = None, with_save = True):
        if ten_sp:
            self.ten_sp = ten_sp
        if mo_ta:
            self.mo_ta = mo_ta
        if gia:
            self.gia = gia
        if so_luong_s:
            self.so_luong_s = so_luong_s
        if so_luong_m:
            self.so_luong_m = so_luong_m
        if so_luong_l:
            self.so_luong_l = so_luong_l
        if so_luong_xl:
            self.so_luong_xl = so_luong_xl
        if mau_sac:
            self.mau_sac = mau_sac
        if hinh_anh:
            self.hinh_anh = hinh_anh
        if with_save:
            self.save()
