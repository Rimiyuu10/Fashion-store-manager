from PySide6.QtCore import Qt
from PySide6.QtWidgets import QDialog, QStackedLayout, QLabel, QVBoxLayout, QLineEdit, QComboBox, QPushButton, \
    QGraphicsDropShadowEffect, QListWidget, QWidget, QMessageBox, QHBoxLayout

from models import DonHang, SanPham, ChiTietDonHang, QuyenHan
from states import UserState


class OrderDetailDialog(QDialog):
    def __init__(self, order: DonHang = None, parent=None):
        super(OrderDetailDialog, self).__init__(parent)
        self.order = order
        self.setFixedSize(600, 800)
        self.setGeometry(100, 100, 600, 800)
        self.setStyleSheet("background-color: #ffffff;")
        self.layout = QStackedLayout()
        self.layout.setStackingMode(QStackedLayout.StackingMode.StackAll)
        self.setLayout(self.layout)
        self.bg = QLabel(self)
        self.bg.setStyleSheet("background-color: transparent; background-image: url('resources/form-bg.png'); margin: 120px 50px 50px; border-radius: 10px; background-repeat: no-repeat; background-position: center;")
        self.top = QVBoxLayout()
        self.top.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.top.setSpacing(10)
        self.setWindowTitle("Đơn hàng")

        self.name = QLineEdit(self)
        self.name.setPlaceholderText("Tên khách hàng")
        self.name.setStyleSheet("border-radius: 10px; font-size: 18px; border: 1px solid #398cfb; background-color: #eff4fa; padding: 10px;")
        self.name.setFixedWidth(350)
        self.name.setFixedHeight(50)
        self.top.addWidget(self.name)

        self.address = QLineEdit(self)
        self.address.setPlaceholderText("Địa chỉ")
        self.address.setStyleSheet("border-radius: 10px; font-size: 18px; border: 1px solid #398cfb; background-color: #eff4fa; padding: 10px;")
        self.address.setFixedWidth(350)
        self.address.setFixedHeight(50)
        self.top.addWidget(self.address)

        self.phone = QLineEdit(self)
        self.phone.setPlaceholderText("Số điện thoại")
        self.phone.setStyleSheet(
            "border-radius: 10px; font-size: 18px; border: 1px solid #398cfb; background-color: #eff4fa; padding: 10px;")
        self.phone.setFixedWidth(350)
        self.phone.setFixedHeight(50)
        self.top.addWidget(self.phone)

        self.cmb_products = QComboBox(self)
        self.cmb_products.setStyleSheet(
            "font-size: 18px; border: 1px solid #398cfb; background-color: #eff4fa; padding: 10px; border-top-left-radius: 10px; border-bottom-left-radius: 10px;")
        self.cmb_products.setFixedWidth(350)
        self.cmb_products.setFixedHeight(50)
        self.top.addWidget(self.cmb_products)

        quantity_container = QHBoxLayout()
        quantity_container.setAlignment(Qt.AlignmentFlag.AlignCenter)
        quantity_container.setSpacing(10)
        self.quantity_s = QLineEdit(self)
        self.quantity_s.setPlaceholderText("S")
        self.quantity_s.setStyleSheet(
            "border-radius: 10px; font-size: 18px; border: 1px solid #398cfb; background-color: #eff4fa; padding: 10px;")
        self.quantity_s.setFixedWidth(70)
        self.quantity_s.setFixedHeight(50)
        quantity_container.addWidget(self.quantity_s)

        self.quantity_m = QLineEdit(self)
        self.quantity_m.setPlaceholderText("M")
        self.quantity_m.setStyleSheet(
            "border-radius: 10px; font-size: 18px; border: 1px solid #398cfb; background-color: #eff4fa; padding: 10px;")
        self.quantity_m.setFixedWidth(70)
        self.quantity_m.setFixedHeight(50)
        quantity_container.addWidget(self.quantity_m)

        self.quantity_l = QLineEdit(self)
        self.quantity_l.setPlaceholderText("L")
        self.quantity_l.setStyleSheet(
            "border-radius: 10px; font-size: 18px; border: 1px solid #398cfb; background-color: #eff4fa; padding: 10px;")
        self.quantity_l.setFixedWidth(70)
        self.quantity_l.setFixedHeight(50)
        quantity_container.addWidget(self.quantity_l)

        self.quantity_xl = QLineEdit(self)
        self.quantity_xl.setPlaceholderText("XL")
        self.quantity_xl.setStyleSheet(
            "border-radius: 10px; font-size: 18px; border: 1px solid #398cfb; background-color: #eff4fa; padding: 10px;")
        self.quantity_xl.setFixedWidth(70)
        self.quantity_xl.setFixedHeight(50)
        quantity_container.addWidget(self.quantity_xl)

        self.quantity = QWidget()
        self.quantity.setStyleSheet("background-color: transparent;")
        self.quantity.setLayout(quantity_container)
        self.top.addWidget(self.quantity, alignment=Qt.AlignmentFlag.AlignCenter)

        self.update = QPushButton("Cập nhật", self)
        self.update.shadow = QGraphicsDropShadowEffect()
        self.update.shadow.setBlurRadius(30)
        self.update.shadow.setXOffset(0)
        self.update.shadow.setYOffset(0)
        self.update.setGraphicsEffect(self.update.shadow)
        self.update.setStyleSheet(
            "background-color: #398cfb; color: #ffffff; font-size: 18px; padding: 10px 20px; border-radius: 10px; font-weight: bold;")
        self.update.setCursor(Qt.CursorShape.PointingHandCursor)
        self.update.setFixedHeight(45)
        self.top.addWidget(self.update, alignment=Qt.AlignmentFlag.AlignCenter)


        self.products = SanPham.fetch_all()
        for product in self.products:
            self.cmb_products.addItem(f"{product.id} - {product.ten_sp} ({product.mau_sac})")

        self.items = []

        self.item_list = QListWidget(self)
        self.item_list.setFixedWidth(350)
        self.item_list.setFixedHeight(220)
        self.item_list.setStyleSheet("border: 1px solid #398cfb; border-radius: 10px; background-color: #eff4fa; padding: 10px;")
        self.item_list.currentRowChanged.connect(self.select_item)
        self.top.addWidget(self.item_list, alignment=Qt.AlignmentFlag.AlignCenter)

        self.total_lbl = QLabel("Tổng tiền: 0 Đ")
        self.total_lbl.setStyleSheet("font-size: 18px; color: red; background-color: transparent; font-weight: bold;")
        self.top.addWidget(self.total_lbl, alignment=Qt.AlignmentFlag.AlignCenter)

        self.save = QPushButton("Lưu lại", self)
        self.save.shadow = QGraphicsDropShadowEffect()
        self.save.shadow.setBlurRadius(30)
        self.save.shadow.setXOffset(0)
        self.save.shadow.setYOffset(0)
        self.save.setGraphicsEffect(self.save.shadow)
        self.save.setStyleSheet(
            "background-color: #398cfb; color: #ffffff; font-size: 18px; padding: 10px 20px; border-radius: 10px; font-weight: bold;")
        self.save.setCursor(Qt.CursorShape.PointingHandCursor)
        self.save.setFixedWidth(200)
        self.save.setFixedHeight(45)
        self.top.addWidget(self.save, alignment=Qt.AlignmentFlag.AlignCenter)

        self.delete = QPushButton("Huỷ đơn", self)
        self.delete.shadow = QGraphicsDropShadowEffect()
        self.delete.shadow.setBlurRadius(30)
        self.delete.shadow.setXOffset(0)
        self.delete.shadow.setYOffset(0)
        self.delete.setGraphicsEffect(self.delete.shadow)
        self.delete.setStyleSheet(
            "background-color: red; color: #ffffff; font-size: 18px; padding: 10px 20px; border-radius: 10px; font-weight: bold;")
        self.delete.setCursor(Qt.CursorShape.PointingHandCursor)
        self.delete.setFixedWidth(200)
        self.delete.setFixedHeight(45)
        self.top.addWidget(self.delete, alignment=Qt.AlignmentFlag.AlignCenter)

        self.next_state = QPushButton("Trạng thái kế tiếp", self)
        self.next_state.shadow = QGraphicsDropShadowEffect()
        self.next_state.shadow.setBlurRadius(30)
        self.next_state.shadow.setXOffset(0)
        self.next_state.shadow.setYOffset(0)
        self.next_state.setGraphicsEffect(self.next_state.shadow)
        self.next_state.setStyleSheet(
            "background-color: #398cfb; color: #ffffff; font-size: 18px; padding: 10px 20px; border-radius: 10px; font-weight: bold;")
        self.next_state.setCursor(Qt.CursorShape.PointingHandCursor)
        self.next_state.setFixedWidth(200)
        self.next_state.setFixedHeight(45)
        self.top.addWidget(self.next_state, alignment=Qt.AlignmentFlag.AlignCenter)

        if order is None:
            self.delete.setVisible(False)
            self.next_state.setVisible(False)

        container = QWidget()
        container.setLayout(self.top)
        self.layout.addWidget(container)
        self.layout.addWidget(self.bg)
        container.setStyleSheet("background-color: rgba(255, 255, 255, 0.45);")

        if order is not None:
            self.name.setText(order.nguoi_mua)
            self.address.setText(order.dia_chi_giao_hang)
            self.phone.setText(order.sdt_nguoi_mua)
            self.dhsp = ChiTietDonHang.fetch_all(where={"id_don_hang": order.id})
            self.items = self.dhsp[:]
            self.recalculate_total()
            self.repaint_items()
            self.item_list.setCurrentRow(0)
            if order.trang_thai == 1:
                self.next_state.setText("Giao hàng")
            elif order.trang_thai == 2:
                self.next_state.setText("Hoàn thành")
            elif order.trang_thai == 3:
                self.next_state.setVisible(False)
            elif order.trang_thai == 4:
                self.next_state.setVisible(False)
                self.delete.setVisible(False)

        if UserState.get_user().quyen_han != QuyenHan["QUAN_LY"]:
            self.name.setReadOnly(True)
            self.address.setReadOnly(True)
            self.phone.setReadOnly(True)
            self.save.setVisible(False)
            self.delete.setVisible(False)
            self.next_state.setVisible(False)
            self.update.setVisible(False)

        self.save.clicked.connect(self.save_order)
        self.delete.clicked.connect(self.delete_order)
        self.next_state.clicked.connect(self.go_next_state)
        self.update.clicked.connect(self.update_item)


    def update_item(self):
        if self.quantity_s.text() == "" or not self.quantity_s.text().isdigit() or \
                self.quantity_m.text() == "" or not self.quantity_m.text().isdigit() or \
                self.quantity_l.text() == "" or not self.quantity_l.text().isdigit() or \
                self.quantity_xl.text() == "" or not self.quantity_xl.text().isdigit():
            QMessageBox.warning(self, "Thông báo", "Vui lòng nhập số lượng hợp lệ")
            return
        index = self.cmb_products.currentIndex()
        exist = False
        for i in range(len(self.items)):
            if self.items[i].id_san_pham == self.products[index].id:
                exist = True
                if (self.items[i].id_don_hang is not None and self.products[index].so_luong_s < int(self.quantity_s.text()) - self.items[i].so_luong_s) \
                        or (self.items[i].id_don_hang is None and self.products[index].so_luong_s < int(self.quantity_s.text())) \
                        or (self.items[i].id_don_hang is not None and self.products[index].so_luong_m < int(self.quantity_m.text()) - self.items[i].so_luong_m) \
                        or (self.items[i].id_don_hang is None and self.products[index].so_luong_m < int(self.quantity_m.text())) \
                        or (self.items[i].id_don_hang is not None and self.products[index].so_luong_l < int(self.quantity_l.text()) - self.items[i].so_luong_l) \
                        or (self.items[i].id_don_hang is None and self.products[index].so_luong_l < int(self.quantity_l.text())) \
                        or (self.items[i].id_don_hang is not None and self.products[index].so_luong_xl < int(self.quantity_xl.text()) - self.items[i].so_luong_xl) \
                        or (self.items[i].id_don_hang is None and self.products[index].so_luong_xl < int(self.quantity_xl.text())):
                    QMessageBox.warning(self, "Thông báo", "Số lượng sản phẩm không đủ")
                    return
                self.items[i].so_luong_s = int(self.quantity_s.text())
                self.items[i].so_luong_m = int(self.quantity_m.text())
                self.items[i].so_luong_l = int(self.quantity_l.text())
                self.items[i].so_luong_xl = int(self.quantity_xl.text())
                self.items[i].don_gia = self.products[index].gia * int(self.quantity_s.text()) + self.products[index].gia * int(self.quantity_m.text()) + self.products[index].gia * int(self.quantity_l.text()) + self.products[index].gia * int(self.quantity_xl.text())
                if self.items[i].so_luong_s <= 0 and self.items[i].so_luong_m <= 0 and self.items[i].so_luong_l <= 0 and self.items[i].so_luong_xl <= 0:
                    self.items.pop(i)
                break
        if not exist:
            if int(self.quantity_s.text()) < 0 or int(self.quantity_m.text()) < 0 or int(self.quantity_l.text()) < 0 or int(self.quantity_xl.text()) < 0 or int(self.quantity_s.text()) + int(self.quantity_m.text()) + int(self.quantity_l.text()) + int(self.quantity_xl.text()) == 0:
                QMessageBox.warning(self, "Thông báo", "Vui lòng nhập số lượng hợp lệ")
                return
            if self.products[index].so_luong_s < int(self.quantity_s.text()) or self.products[index].so_luong_m < int(self.quantity_m.text()) or self.products[index].so_luong_l < int(self.quantity_l.text()) or self.products[index].so_luong_xl < int(self.quantity_xl.text()):
                QMessageBox.warning(self, "Thông báo", "Số lượng sản phẩm không đủ")
                return
            self.items.append(ChiTietDonHang(
                id_san_pham=self.products[index].id,
                so_luong_s=int(self.quantity_s.text()),
                so_luong_m=int(self.quantity_m.text()),
                so_luong_l=int(self.quantity_l.text()),
                so_luong_xl=int(self.quantity_xl.text()),
                don_gia=self.products[index].gia * int(self.quantity_s.text()) + self.products[index].gia * int(self.quantity_m.text()) + self.products[index].gia * int(self.quantity_l.text()) + self.products[index].gia * int(self.quantity_xl.text())
            ))
        self.recalculate_total()
        self.repaint_items()

    def select_item(self):
        if self.item_list.currentItem() is None:
            return
        product_id = int(self.item_list.currentItem().text().split(" ")[2])
        quantity_s = int(self.item_list.currentItem().text().split(" ")[6])
        quantity_m = int(self.item_list.currentItem().text().split(" ")[8])
        quantity_l = int(self.item_list.currentItem().text().split(" ")[10])
        quantity_xl = int(self.item_list.currentItem().text().split(" ")[12])
        for i in range(len(self.products)):
            if self.products[i].id == product_id:
                self.cmb_products.setCurrentIndex(i)
                self.quantity_s.setText(str(quantity_s))
                self.quantity_m.setText(str(quantity_m))
                self.quantity_l.setText(str(quantity_l))
                self.quantity_xl.setText(str(quantity_xl))
                break

    def recalculate_total(self):
        total = 0
        for item in self.items:
            total += item.don_gia
        self.total_lbl.setText(f"Tổng tiền: {total:,} Đ")

    def repaint_items(self):
        self.item_list.clear()
        for item in self.items:
            self.item_list.addItem(f"ID = {item.id_san_pham} - SL = {item.so_luong_s} | {item.so_luong_m} | {item.so_luong_l} | {item.so_luong_xl} - {item.don_gia:,} Đ")

    def go_next_state(self):
        if self.order.trang_thai == 1:
            self.order.dang_giao_hang()
        elif self.order.trang_thai == 2:
            self.order.da_giao_hang()
        self.accept()


    def save_order(self):
        if self.item_list.count() == 0:
            QMessageBox.warning(self, "Thông báo", "Vui lòng chọn sản phẩm")
            return
        if (self.name.text() == "" or self.address.text() == "" or self.phone.text() == "" or self.quantity_s.text() == "" or not self.quantity_s.text().isdigit()
                or self.quantity_m.text() == "" or not self.quantity_m.text().isdigit() or self.quantity_l.text() == "" or not self.quantity_l.text().isdigit()
                or self.quantity_xl.text() == "" or not self.quantity_xl.text().isdigit()
                or self.cmb_products.currentIndex() == -1
        ):
            QMessageBox.warning(self, "Thông báo", "Vui lòng điền đầy đủ thông tin")
            return
        if self.order is not None:
            self.order.update(nguoi_mua=self.name.text(), dia_chi_giao_hang=self.address.text(), sdt_nguoi_mua=self.phone.text())
            for item in self.items:
                if item.id_don_hang is None:
                    item.id_don_hang = self.order.id
                    self.order.them_sp(item.id_san_pham, item.so_luong_s, item.so_luong_m, item.so_luong_l, item.so_luong_xl, item.don_gia)
                else:
                    self.order.cap_nhat_sp(item.id_san_pham, item.so_luong_s, item.so_luong_m, item.so_luong_l, item.so_luong_xl, item.don_gia)
            for item in self.dhsp:
                exist = False
                for new_item in self.items:
                    if item.id_san_pham == new_item.id_san_pham:
                        exist = True
                        break
                if not exist:
                    self.order.xoa_sp(item.id_san_pham)
        else:
            order = DonHang(nguoi_mua=self.name.text(), dia_chi_giao_hang=self.address.text(), sdt_nguoi_mua=self.phone.text())
            order.save()
            for item in self.items:
                order.them_sp(item.id_san_pham, item.so_luong_s, item.so_luong_m, item.so_luong_l, item.so_luong_xl, item.don_gia)
        self.accept()

    def delete_order(self):
        if self.order is not None:
            self.order.huy_don_hang()
        self.accept()
