from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QPushButton, QStackedLayout, QLabel, QVBoxLayout, QWidget, QGraphicsDropShadowEffect
from dialogs.products import ProductDetailDialog
from models import SanPham


class ProductSummary(QPushButton):
    def __init__(self, product: SanPham, parent=None):
        super(ProductSummary, self).__init__(parent)
        self.parent = parent
        self.clicked.connect(lambda: self.show_detail())
        self.setStyleSheet("background-color: transparent;")
        self.setFixedSize(170, 230)
        self.product = product
        self.layout = QStackedLayout()
        self.setLayout(self.layout)
        self.layout.setStackingMode(QStackedLayout.StackingMode.StackAll)

        self.quantity = QLabel("100")
        self.quantity.setStyleSheet("font-size: 16px; font-weight: bold; color: #000000; padding: 0; background-color: #716EEE; border-radius: 10px; color: #ffffff;")
        self.quantity.setFixedSize(50, 30)
        self.quantity.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.layout.addWidget(self.quantity)

        self.bellow = QVBoxLayout()
        self.bellow.setSpacing(2)
        self.bellow_container = QWidget()
        self.bellow_container.setLayout(self.bellow)
        self.layout.addWidget(self.bellow_container)

        self.img = QLabel(self)
        self.img.setPixmap(QPixmap("products/default.png").scaled(130, 130, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation))
        self.img.setFixedSize(130, 130)
        self.img.setStyleSheet("background-color: transparent; margin: 10px 5px;")
        self.bellow.addWidget(self.img, alignment=Qt.AlignmentFlag.AlignCenter)

        self.id = QLabel("ID: 1")
        self.id.setStyleSheet("font-size: 12px; color: #716EEE; background-color: transparent; font-weight: bold;")
        self.bellow.addWidget(self.id, alignment=Qt.AlignmentFlag.AlignCenter)

        self.name = QLabel("Tên Sản Phẩm")
        self.name.setStyleSheet("font-size: 12px; color: #000000; background-color: transparent;")
        self.bellow.addWidget(self.name, alignment=Qt.AlignmentFlag.AlignCenter)

        self.price = QLabel("0.000 Đ")
        self.price.setStyleSheet("font-size: 14px; font-weight: bold; color: red; background-color: transparent;")
        self.bellow.addWidget(self.price, alignment=Qt.AlignmentFlag.AlignCenter)

        self.shadow = QGraphicsDropShadowEffect()
        self.shadow.setBlurRadius(30)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)

        self.frame = QLabel(self)
        self.frame.setStyleSheet("border: 1px solid #000000; border-radius: 10px; background-color: #ffffff; margin: 10px;")
        self.layout.addWidget(self.frame)
        self.frame.setGraphicsEffect(self.shadow)

        if self.product is not None:
            self.name.setText(f"{self.product.ten_sp}")
            self.id.setText(f"ID: {self.product.id}")
            self.price.setText(f"{self.product.gia:,} Đ")
            self.quantity.setText(str(self.product.so_luong_s + self.product.so_luong_m + self.product.so_luong_l + self.product.so_luong_xl))
            self.img.setPixmap(QPixmap(f"products/{self.product.hinh_anh}").scaled(130, 130, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation))
        else:
            self.setVisible(False)

    def show_detail(self):
        dialog = ProductDetailDialog(self.product, self.parent)
        dialog.exec()
        self.parent.update_products()
