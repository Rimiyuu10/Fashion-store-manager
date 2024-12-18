import os
import shutil
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QDialog, QStackedLayout, QLabel, QVBoxLayout, QPushButton, QLineEdit, \
    QGraphicsDropShadowEffect, QWidget, QFileDialog, QMessageBox, QHBoxLayout
from models import SanPham, QuyenHan
from states import UserState


class ProductDetailDialog(QDialog):
    def __init__(self, product: SanPham = None, parent=None):
        super(ProductDetailDialog, self).__init__(parent)
        self.product = product
        self.image_path = ""
        self.setFixedSize(600, 800)
        self.setGeometry(100, 100, 600, 800)
        self.setStyleSheet("background-color: #ffffff;")
        self.layout = QStackedLayout()
        self.layout.setStackingMode(QStackedLayout.StackingMode.StackAll)
        self.setLayout(self.layout)
        self.bg = QLabel(self)
        self.bg.setStyleSheet("background-color: transparent; background-image: url('resources/form-bg.png'); margin: 120px 50px 50px; border-radius: 10px; background-repeat: no-repeat; background-position: center;")
        self.top = QVBoxLayout()
        self.top.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.top.setSpacing(10)
        self.setWindowTitle("Sản phẩm")

        self.img = QLabel(self)
        self.img.setPixmap(QPixmap("products/default.jpg").scaled(200, 200, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation))
        self.img.setStyleSheet("background-color: #ffffff; padding: 10px; border-radius: 10px; border: 1px solid #000000;")
        self.top.addWidget(self.img, alignment=Qt.AlignmentFlag.AlignCenter)

        self.img_chooser = QPushButton("Chọn ảnh", self)
        self.img_chooser.setStyleSheet("background-color: #398cfb; color: #ffffff; font-size: 18px; padding: 10px 20px; border-radius: 10px; font-weight: bold;")
        self.img_chooser.setCursor(Qt.CursorShape.PointingHandCursor)
        self.img_chooser.setFixedHeight(45)
        self.top.addWidget(self.img_chooser, alignment=Qt.AlignmentFlag.AlignCenter)

        self.img_chooser.clicked.connect(self.choose_image)

        self.name = QLineEdit(self)
        self.name.setPlaceholderText("Tên sản phẩm")
        self.name.setStyleSheet("border-radius: 10px; font-size: 18px; border: 1px solid #398cfb; background-color: #eff4fa; padding: 10px;")
        self.name.setFixedWidth(350)
        self.name.setFixedHeight(50)
        self.top.addWidget(self.name)

        self.description = QLineEdit(self)
        self.description.setPlaceholderText("Mô tả")
        self.description.setStyleSheet("border-radius: 10px; font-size: 18px; border: 1px solid #398cfb; background-color: #eff4fa; padding: 10px;")
        self.description.setFixedWidth(350)
        self.description.setFixedHeight(50)
        self.top.addWidget(self.description)

        self.color = QLineEdit(self)
        self.color.setPlaceholderText("Màu sắc")
        self.color.setStyleSheet("border-radius: 10px; font-size: 18px; border: 1px solid #398cfb; background-color: #eff4fa; padding: 10px;")
        self.color.setFixedWidth(350)
        self.color.setFixedHeight(50)
        self.top.addWidget(self.color)

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

        self.price = QLineEdit(self)
        self.price.setPlaceholderText("Giá bán")
        self.price.setStyleSheet(
            "border-radius: 10px; font-size: 18px; border: 1px solid #398cfb; background-color: #eff4fa; padding: 10px;")
        self.price.setFixedWidth(350)
        self.price.setFixedHeight(50)
        self.top.addWidget(self.price)

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

        self.delete = QPushButton("Xoá bỏ", self)
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

        if product is None:
            self.delete.setVisible(False)

        container = QWidget()
        container.setLayout(self.top)
        self.layout.addWidget(container)
        self.layout.addWidget(self.bg)
        container.setStyleSheet("background-color: rgba(255, 255, 255, 0.45);")

        if product is not None:
            self.name.setText(product.ten_sp)
            self.description.setText(product.mo_ta)
            self.color.setText(product.mau_sac)
            self.quantity_s.setText(str(product.so_luong_s))
            self.quantity_m.setText(str(product.so_luong_m))
            self.quantity_l.setText(str(product.so_luong_l))
            self.quantity_xl.setText(str(product.so_luong_xl))
            self.price.setText(str(product.gia))
            self.img.setPixmap(QPixmap(f"products/{product.hinh_anh}").scaled(200, 200, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation))

        self.save.clicked.connect(self.save_product)
        self.delete.clicked.connect(self.delete_product)

        if UserState.get_user().quyen_han != QuyenHan["QUAN_LY"]:
            self.name.setReadOnly(True)
            self.description.setReadOnly(True)
            self.color.setReadOnly(True)
            self.quantity_s.setReadOnly(True)
            self.quantity_m.setReadOnly(True)
            self.quantity_l.setReadOnly(True)
            self.quantity_xl.setReadOnly(True)
            self.price.setReadOnly(True)
            self.img_chooser.setVisible(False)
            self.save.setVisible(False)
            self.delete.setVisible(False)

    def choose_image(self):
        file = QFileDialog.getOpenFileName(self, "Chọn ảnh", "", "Image Files (*.png *.jpg *.jpeg *.bmp)")
        if file[0] != "":
            self.img.setPixmap(QPixmap(file[0]).scaled(200, 200, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation))
            self.image_path = file[0]

    def save_product(self):
        if (self.name.text() == "" or self.description.text() == "" or self.color.text() == "" or not self.quantity_s.text().isdigit() or not self.quantity_m.text().isdigit() or not self.quantity_l.text().isdigit() or not self.quantity_xl.text().isdigit() or not self.price.text().isdigit()):
            QMessageBox.warning(self, "Thông báo", "Vui lòng điền đầy đủ thông tin")
            return
        if self.product is not None:
            if len(self.image_path) and os.path.exists(self.image_path):
                if "default" not in self.product.hinh_anh:
                    os.remove(f"products/{self.product.hinh_anh}")
                shutil.copyfile(self.image_path, f"products/{self.product.id}.{self.image_path.split('.')[-1]}")
                self.product.update(hinh_anh=f"{self.product.id}.{self.image_path.split('.')[-1]}")
            self.product.update(ten_sp=self.name.text(), mo_ta=self.description.text(), mau_sac=self.color.text(), so_luong_s=int(self.quantity_s.text()), so_luong_m=int(self.quantity_m.text()), so_luong_l=int(self.quantity_l.text()), so_luong_xl=int(self.quantity_xl.text()), gia=int(self.price.text()))
        else:
            product = SanPham(ten_sp=self.name.text(), mo_ta=self.description.text(), mau_sac=self.color.text(), so_luong_s=int(self.quantity_s.text()), so_luong_m=int(self.quantity_m.text()), so_luong_l=int(self.quantity_l.text()), so_luong_xl=int(self.quantity_xl.text()), gia=int(self.price.text()), hinh_anh="default.jpg")
            product.save()
            if len(self.image_path) and os.path.exists(self.image_path):
                shutil.copyfile(self.image_path, f"products/{product.id}.{self.image_path.split('.')[-1]}")
                product.update(hinh_anh=f"{product.id}.{self.image_path.split('.')[-1]}")
        self.accept()

    def delete_product(self):
        if self.product is not None:
            if "default" not in self.product.hinh_anh:
                os.remove(f"products/{self.product.hinh_anh}")
            self.product.delete()
        self.accept()
