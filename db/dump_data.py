from models import *


def init_data():
    # NhanVien
    ds_nv = [NhanVien("Nguyễn Văn Hoàng", "32 Võ Văn Ngân, Thủ Đức, TP.HCM", "0909123456",
                      "nvhoang@company.com", "Chủ cửa hàng", "admin", "admin"),
             NhanVien("Trần Thị Thanh", "61 Lê Văn Việt, Quận 9, TP.HCM", "0909123457",
                      "ttthanh@company.com", "Quản lý chi nhánh", "ttthanh", "123456"),
             NhanVien("Lê Văn Tài", "12 Lê Văn Sỹ, Quận 3, TP.HCM", "0909123458",
                      "lvtai@company.com", "Quản lý chi nhánh", "lvtai", "123456"),
             NhanVien("Nguyễn Thị Thảo", "32 Võ Văn Ngân, Thủ Đức, TP.HCM", "0909123459",
                      "ntthao@company.com", "Nhân viên bán hàng", "ntthao", "123456"),
             NhanVien("Trần Văn Tú", "61 Lê Văn Việt, Quận 9, TP.HCM", "0909123460",
                      "tvtu@company.com", "Nhân viên bán hàng", "tvtu", "123456"),
             NhanVien("Lê Ngọc My", "12 Lê Văn Sỹ, Quận 3, TP.HCM", "0909123461",
                      "lnmy@company.com", "Nhân viên bán hàng", "lnmy", "123456"),
             NhanVien("Hoàng Mộc Lan", "99 Hồng Bàng, Quận 5, TP.HCM", "0909123462",
                      "hmlan@company.com", "Nhân viên bán hàng", "hmlan", "123456"),
             NhanVien("Trần Văn Hùng", "76/5 Lê Lai, Quận 1, TP.HCM", "0909123463",
                      "tvhung@company.com", "Nhân viên bán hàng", "tvhung", "123456")]

    for nv in ds_nv:
        nv.save()

    ds_nv[0].make_admin()

    # SanPham
    ds_sp = [SanPham("Áo thun tay ngắn", "Áo thun tay ngắn nam màu đen", 150000, 100, 100, 100, 100, "Đen", "default.jpg"),
             SanPham("Áo thun tay ngắn", "Áo thun tay ngắn nam màu trắng", 150000, 100, 100, 100, 100, "Trắng", "default.jpg"),
             SanPham("Áo thun tay ngắn", "Áo thun tay ngắn nam màu xanh", 150000, 100, 100, 100, 100, "Xanh", "default.jpg"),
             SanPham("Áo thun tay ngắn", "Áo thun tay ngắn nam màu đỏ", 150000, 100, 100, 100, 100, "Đỏ", "default.jpg"),
             SanPham("Áo thun tay ngắn", "Áo thun tay ngắn nam màu vàng", 150000, 100, 100, 100, 100, "Vàng", "default.jpg"),
             SanPham("Áo thun tay dài", "Áo thun tay dài nam màu đen", 200000, 100, 100, 100, 100, "Đen", "default.jpg"),
             SanPham("Áo thun tay dài", "Áo thun tay dài nam màu trắng", 200000, 100, 100, 100, 100, "Trắng", "default.jpg"),
             SanPham("Áo thun tay dài", "Áo thun tay dài nam màu xanh", 200000, 100, 100, 100, 100, "Xanh", "default.jpg"),
             SanPham("Áo thun tay dài", "Áo thun tay dài nam màu đỏ", 200000, 100, 100, 100, 100, "Đỏ", "default.jpg"),
             SanPham("Áo thun tay dài", "Áo thun tay dài nam màu vàng", 200000, 100, 100, 100, 100, "Vàng", "default.jpg"),
             SanPham("Áo sơ mi", "Áo sơ mi nam màu trắng", 250000, 100, 100, 100, 100, "Trắng", "default.jpg"),
             SanPham("Áo sơ mi", "Áo sơ mi nam màu xanh", 250000, 100, 100, 100, 100, "Xanh", "default.jpg"),
             SanPham("Áo sơ mi", "Áo sơ mi nam màu đen", 250000, 100, 100, 100, 100, "Đen", "default.jpg"),
             SanPham("Áo sơ mi", "Áo sơ mi nam màu đỏ", 250000, 100, 100, 100, 100, "Đỏ", "default.jpg"),
             SanPham("Áo sơ mi", "Áo sơ mi nam màu xám", 250000, 100, 100, 100, 100, "Xám", "default.jpg"),
             SanPham("Quần jean", "Quần jean nam màu đen", 300000, 100, 100, 100, 100, "Đen", "default.jpg"),
             SanPham("Quần jean", "Quần jean nam màu xanh", 300000, 100, 100, 100, 100, "Xanh", "default.jpg"),
             SanPham("Quần jean", "Quần jean nam màu đỏ", 300000, 100, 100, 100, 100, "Đỏ", "default.jpg"),
             SanPham("Quần jean", "Quần jean nam màu xám", 300000, 100, 100, 100, 100, "Xám", "default.jpg"),
             SanPham("Quần jean", "Quần jean nam màu trắng", 300000, 100, 100, 100, 100, "Trắng", "default.jpg"),
             SanPham("Quần kaki", "Quần kaki nam màu đen", 250000, 100, 100, 100, 100, "Đen", "default.jpg"),
             SanPham("Quần kaki", "Quần kaki nam màu xanh", 250000, 100, 100, 100, 100, "Xanh", "default.jpg"),
             SanPham("Quần kaki", "Quần kaki nam màu đỏ", 250000, 100, 100, 100, 100, "Đỏ", "default.jpg"),
             SanPham("Quần kaki", "Quần kaki nam màu xám", 250000, 100, 100, 100, 100, "Xám", "default.jpg"),
             SanPham("Quần kaki", "Quần kaki nam màu trắng", 250000, 100, 100, 100, 100, "Trắng", "default.jpg"),
             SanPham("Quần âu", "Quần âu nam màu đen", 350000, 100, 100, 100, 100, "Đen", "default.jpg"),
             SanPham("Quần âu", "Quần âu nam màu xanh", 350000, 100, 100, 100, 100, "Xanh", "default.jpg"),
             SanPham("Quần âu", "Quần âu nam màu đỏ", 350000, 100, 100, 100, 100, "Đỏ", "default.jpg"),
             SanPham("Quần âu", "Quần âu nam màu xám", 350000, 100, 100, 100, 100, "Xám", "default.jpg"),
             SanPham("Quần âu", "Quần âu nam màu trắng", 350000, 100, 100, 100, 100, "Trắng", "default.jpg"),
             SanPham("Quần short", "Quần short nam màu đen", 150000, 100, 100, 100, 100, "Đen", "default.jpg"),
             SanPham("Quần short", "Quần short nam màu xanh", 150000, 100, 100, 100, 100, "Xanh", "default.jpg"),
             SanPham("Quần short", "Quần short nam màu đỏ", 150000, 100, 100, 100, 100, "Đỏ", "default.jpg"),
             SanPham("Quần short", "Quần short nam màu xám", 150000, 100, 100, 100, 100, "Xám", "default.jpg"),
             SanPham("Quần short", "Quần short nam màu trắng", 150000, 100, 100, 100, 100, "Trắng", "default.jpg"),
             SanPham("Áo khoác", "Áo khoác nam màu đen", 400000, 100, 100, 100, 100, "Đen", "default.jpg"),
             SanPham("Áo khoác", "Áo khoác nam màu xanh", 400000, 100, 100, 100, 100, "Xanh", "default.jpg"),
             SanPham("Áo khoác", "Áo khoác nam màu đỏ", 400000, 100, 100, 100, 100, "Đỏ", "default.jpg"),
             SanPham("Áo khoác", "Áo khoác nam màu xám", 400000, 100, 100, 100, 100, "Xám", "default.jpg")]

    for sp in ds_sp:
        sp.save()
