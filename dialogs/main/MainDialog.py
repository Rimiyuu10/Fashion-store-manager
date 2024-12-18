from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QDialog, QStackedLayout, QLabel, QHBoxLayout, QVBoxLayout, QPushButton, \
    QGraphicsDropShadowEffect, QWidget, QMessageBox, QGridLayout

from dialogs.orders.OrderDialog import OrderDialog
from dialogs.employees.EmployeeDialog import EmployeeDialog
from dialogs.products.ProductDialog import ProductDialog
from models import DonHang, SanPham, NhanVien
from states import UserState


class MainDialog(QDialog):
    def __init__(self, parent=None):
        super(MainDialog, self).__init__(parent)
        self.setWindowTitle("Quản lý cửa hàng")
        self.setFixedSize(1200, 675)
        self.setGeometry(100, 100, 1200, 675)
        self.setStyleSheet("background-color: #ffffff;")
        self.layout = QStackedLayout()
        self.layout.setStackingMode(QStackedLayout.StackingMode.StackAll)
        self.setLayout(self.layout)
        self.bg = QLabel(self)
        self.bg.setStyleSheet(
            "background-image: url('resources/shop-bg.png'); margin: 50 50 50 300; background-repeat: no-repeat; background-position: center;")
        self.top = QHBoxLayout()
        self.top.setAlignment(Qt.AlignmentFlag.AlignJustify)
        self.setWindowTitle("Quản lý cửa hàng")

        self.left = QVBoxLayout()
        self.left.setContentsMargins(50, 50, 100, 50)
        self.left.setSpacing(50)

        self.product = QPushButton("Sản phẩm", self)
        self.product.setStyleSheet(
            "background-color: #88BAFD; color: #ffffff; font-size: 24px; border-radius: 10px; font-weight: bold; border: 1px solid #398cfb; padding: 10px 20px;")
        self.product.setCursor(Qt.CursorShape.PointingHandCursor)
        self.product.setFixedWidth(220)
        self.product.setFixedHeight(90)
        self.product.setIcon(QIcon("resources/sp.png"))
        self.product.setIconSize(QSize(50, 50))
        self.product.shadow = QGraphicsDropShadowEffect()
        self.product.shadow.setBlurRadius(30)
        self.product.shadow.setXOffset(0)
        self.product.shadow.setYOffset(0)
        self.product.setGraphicsEffect(self.product.shadow)
        self.left.addWidget(self.product)

        self.order = QPushButton("Đơn hàng", self)
        self.order.setStyleSheet(
            "background-color: #88BAFD; color: #ffffff; font-size: 24px; border-radius: 10px; font-weight: bold; border: 1px solid #398cfb; padding: 10px 20px;")
        self.order.setCursor(Qt.CursorShape.PointingHandCursor)
        self.order.setFixedWidth(220)
        self.order.setFixedHeight(90)
        self.order.setIcon(QIcon("resources/dh.png"))
        self.order.setIconSize(QSize(50, 50))
        self.order.shadow = QGraphicsDropShadowEffect()
        self.order.shadow.setBlurRadius(30)
        self.order.shadow.setXOffset(0)
        self.order.shadow.setYOffset(0)
        self.order.setGraphicsEffect(self.order.shadow)
        self.left.addWidget(self.order)

        self.employee = QPushButton("Nhân viên", self)
        self.employee.setStyleSheet(
            "background-color: #88BAFD; color: #ffffff; font-size: 24px; border-radius: 10px; font-weight: bold; border: 1px solid #398cfb; padding: 10px 20px;")
        self.employee.setCursor(Qt.CursorShape.PointingHandCursor)
        self.employee.setFixedWidth(220)
        self.employee.setFixedHeight(90)
        self.employee.setIcon(QIcon("resources/nv.png"))
        self.employee.setIconSize(QSize(50, 50))
        self.employee.shadow = QGraphicsDropShadowEffect()
        self.employee.shadow.setBlurRadius(30)
        self.employee.shadow.setXOffset(0)
        self.employee.shadow.setYOffset(0)
        self.employee.setGraphicsEffect(self.employee.shadow)
        self.left.addWidget(self.employee)

        self.logout = QPushButton(self)
        self.logout.setStyleSheet(
            "background-color: transparent;")
        self.logout.setCursor(Qt.CursorShape.PointingHandCursor)
        self.logout.setIcon(QIcon("resources/logout.png"))
        self.logout.setIconSize(QSize(80, 80))
        self.logout.shadow = QGraphicsDropShadowEffect()
        self.logout.shadow.setBlurRadius(30)
        self.logout.shadow.setXOffset(0)
        self.logout.shadow.setYOffset(0)
        self.logout.setGraphicsEffect(self.logout.shadow)
        self.logout.clicked.connect(self.logout_clicked)
        self.left.addWidget(self.logout, alignment=Qt.AlignmentFlag.AlignBottom | Qt.AlignmentFlag.AlignLeft)

        left_container = QWidget()
        left_container.setLayout(self.left)
        self.top.addWidget(left_container)

        self.right = QGridLayout()
        self.right.setContentsMargins(50, 150, 50, 150)

        self.right_incomebox_layout = QStackedLayout()
        self.right_incomebox_layout.setStackingMode(QStackedLayout.StackingMode.StackAll)
        self.right_incomebox_layout_bg = QWidget()
        self.right_incomebox_layout_bg.setStyleSheet("background-color: #ffffff; border-radius: 10px; margin: 30px 0 0 0")
        self.right_incomebox_layout_bg.setFixedWidth(240)
        self.right_incomebox_layout_bg.setFixedHeight(150)
        self.right_incomebox_layout_bg.shadow = QGraphicsDropShadowEffect()
        self.right_incomebox_layout_bg.shadow.setBlurRadius(25)
        self.right_incomebox_layout_bg.shadow.setXOffset(5)
        self.right_incomebox_layout_bg.shadow.setYOffset(5)
        self.right_incomebox_layout_bg.setGraphicsEffect(self.right_incomebox_layout_bg.shadow)
        self.right_incomebox_layout.addWidget(self.right_incomebox_layout_bg)
        self.right_incomebox_layout_lbl = QLabel("DOANH THU", self)
        self.right_incomebox_layout_lbl.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.right_incomebox_layout_lbl.setStyleSheet("font-size: 18px; color: #7E7E7E; padding: 40px 70px; font-weight: bold; background-color: transparent;")
        self.right_incomebox_layout.addWidget(self.right_incomebox_layout_lbl)
        self.right_incomebox_layout_icon = QLabel()
        self.right_incomebox_layout_icon.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.right_incomebox_layout_icon.setStyleSheet("background-image: url('resources/income.png'); background-repeat: no-repeat; background-position: center; background-color: #716EEE; border-radius: 10px; margin: 0 0 0 20px;")
        self.right_incomebox_layout_icon.setFixedWidth(90)
        self.right_incomebox_layout_icon.setFixedHeight(70)
        self.right_incomebox_layout.addWidget(self.right_incomebox_layout_icon)
        self.right_incomebox_layout_val = QLabel("100,000 Đ", self)
        self.right_incomebox_layout_val.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.right_incomebox_layout_val.setStyleSheet(
            "font-size: 28px; color: #000000; padding: 100px 70px 0 0; font-weight: bold; background-color: transparent;")
        self.right_incomebox_layout.addWidget(self.right_incomebox_layout_val)

        self.right_incomebox = QWidget()
        self.right_incomebox.setLayout(self.right_incomebox_layout)
        self.right.addWidget(self.right_incomebox, 0, 0, 1, 1)

        self.right_orderbox_layout = QStackedLayout()
        self.right_orderbox_layout.setStackingMode(QStackedLayout.StackingMode.StackAll)
        self.right_orderbox_layout_bg = QWidget()
        self.right_orderbox_layout_bg.setStyleSheet("background-color: #ffffff; border-radius: 10px; margin: 30px 0 0 0")
        self.right_orderbox_layout_bg.setFixedWidth(240)
        self.right_orderbox_layout_bg.setFixedHeight(150)
        self.right_orderbox_layout_bg.shadow = QGraphicsDropShadowEffect()
        self.right_orderbox_layout_bg.shadow.setBlurRadius(25)
        self.right_orderbox_layout_bg.shadow.setXOffset(5)
        self.right_orderbox_layout_bg.shadow.setYOffset(5)
        self.right_orderbox_layout_bg.setGraphicsEffect(self.right_orderbox_layout_bg.shadow)
        self.right_orderbox_layout.addWidget(self.right_orderbox_layout_bg)
        self.right_orderbox_layout_lbl = QLabel("ĐƠN HÀNG", self)
        self.right_orderbox_layout_lbl.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.right_orderbox_layout_lbl.setStyleSheet("font-size: 18px; color: #7E7E7E; padding: 40px 70px; font-weight: bold; background-color: transparent;")
        self.right_orderbox_layout.addWidget(self.right_orderbox_layout_lbl)
        self.right_orderbox_layout_icon = QLabel()
        self.right_orderbox_layout_icon.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.right_orderbox_layout_icon.setStyleSheet("background-image: url('resources/order.png'); background-repeat: no-repeat; background-position: center; background-color: #716EEE; border-radius: 10px; margin: 0 0 0 20px;")
        self.right_orderbox_layout_icon.setFixedWidth(90)
        self.right_orderbox_layout_icon.setFixedHeight(70)
        self.right_orderbox_layout.addWidget(self.right_orderbox_layout_icon)
        self.right_orderbox_layout_val = QLabel("1", self)
        self.right_orderbox_layout_val.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.right_orderbox_layout_val.setStyleSheet(
            "font-size: 28px; color: #000000; padding: 100px 70px 0 0; font-weight: bold; background-color: transparent;")
        self.right_orderbox_layout.addWidget(self.right_orderbox_layout_val)

        self.right_orderbox = QWidget()
        self.right_orderbox.setLayout(self.right_orderbox_layout)
        self.right.addWidget(self.right_orderbox, 1, 0, 1, 1)

        self.right_employeebox_layout = QStackedLayout()
        self.right_employeebox_layout.setStackingMode(QStackedLayout.StackingMode.StackAll)
        self.right_employeebox_layout_bg = QWidget()
        self.right_employeebox_layout_bg.setStyleSheet(
            "background-color: #ffffff; border-radius: 10px; margin: 30px 0 0 0")
        self.right_employeebox_layout_bg.setFixedWidth(240)
        self.right_employeebox_layout_bg.setFixedHeight(150)
        self.right_employeebox_layout_bg.shadow = QGraphicsDropShadowEffect()
        self.right_employeebox_layout_bg.shadow.setBlurRadius(25)
        self.right_employeebox_layout_bg.shadow.setXOffset(5)
        self.right_employeebox_layout_bg.shadow.setYOffset(5)
        self.right_employeebox_layout_bg.setGraphicsEffect(self.right_employeebox_layout_bg.shadow)
        self.right_employeebox_layout.addWidget(self.right_employeebox_layout_bg)
        self.right_employeebox_layout_lbl = QLabel("NHÂN VIÊN", self)
        self.right_employeebox_layout_lbl.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.right_employeebox_layout_lbl.setStyleSheet(
            "font-size: 18px; color: #7E7E7E; padding: 40px 70px; font-weight: bold; background-color: transparent;")
        self.right_employeebox_layout.addWidget(self.right_employeebox_layout_lbl)
        self.right_employeebox_layout_icon = QLabel()
        self.right_employeebox_layout_icon.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.right_employeebox_layout_icon.setStyleSheet(
            "background-image: url('resources/employee.png'); background-repeat: no-repeat; background-position: center; background-color: #716EEE; border-radius: 10px; margin: 0 0 0 20px;")
        self.right_employeebox_layout_icon.setFixedWidth(90)
        self.right_employeebox_layout_icon.setFixedHeight(70)
        self.right_employeebox_layout.addWidget(self.right_employeebox_layout_icon)
        self.right_employeebox_layout_val = QLabel("10", self)
        self.right_employeebox_layout_val.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.right_employeebox_layout_val.setStyleSheet(
            "font-size: 28px; color: #000000; padding: 100px 70px 0 0; font-weight: bold; background-color: transparent;")
        self.right_employeebox_layout.addWidget(self.right_employeebox_layout_val)

        self.right_employeebox = QWidget()
        self.right_employeebox.setLayout(self.right_employeebox_layout)
        self.right.addWidget(self.right_employeebox, 0, 1, 1, 1)

        self.right_productbox_layout = QStackedLayout()
        self.right_productbox_layout.setStackingMode(QStackedLayout.StackingMode.StackAll)
        self.right_productbox_layout_bg = QWidget()
        self.right_productbox_layout_bg.setStyleSheet(
            "background-color: #ffffff; border-radius: 10px; margin: 30px 0 0 0")
        self.right_productbox_layout_bg.setFixedWidth(240)
        self.right_productbox_layout_bg.setFixedHeight(150)
        self.right_productbox_layout_bg.shadow = QGraphicsDropShadowEffect()
        self.right_productbox_layout_bg.shadow.setBlurRadius(25)
        self.right_productbox_layout_bg.shadow.setXOffset(5)
        self.right_productbox_layout_bg.shadow.setYOffset(5)
        self.right_productbox_layout_bg.setGraphicsEffect(self.right_productbox_layout_bg.shadow)
        self.right_productbox_layout.addWidget(self.right_productbox_layout_bg)
        self.right_productbox_layout_lbl = QLabel("SẢN PHẨM", self)
        self.right_productbox_layout_lbl.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.right_productbox_layout_lbl.setStyleSheet(
            "font-size: 18px; color: #7E7E7E; padding: 40px 70px; font-weight: bold; background-color: transparent;")
        self.right_productbox_layout.addWidget(self.right_productbox_layout_lbl)
        self.right_productbox_layout_icon = QLabel()
        self.right_productbox_layout_icon.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.right_productbox_layout_icon.setStyleSheet(
            "background-image: url('resources/product.png'); background-repeat: no-repeat; background-position: center; background-color: #716EEE; border-radius: 10px; margin: 0 0 0 20px;")
        self.right_productbox_layout_icon.setFixedWidth(90)
        self.right_productbox_layout_icon.setFixedHeight(70)
        self.right_productbox_layout.addWidget(self.right_productbox_layout_icon)
        self.right_productbox_layout_val = QLabel("10", self)
        self.right_productbox_layout_val.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.right_productbox_layout_val.setStyleSheet(
            "font-size: 28px; color: #000000; padding: 100px 70px 0 0; font-weight: bold; background-color: transparent;")
        self.right_productbox_layout.addWidget(self.right_productbox_layout_val)

        self.right_productbox = QWidget()
        self.right_productbox.setLayout(self.right_productbox_layout)
        self.right.addWidget(self.right_productbox, 1, 1, 1, 1)

        right_container = QWidget()
        right_container.setLayout(self.right)
        right_container.setFixedWidth(700)
        self.top.addWidget(right_container)

        container = QWidget()
        container.setLayout(self.top)
        self.layout.addWidget(container)
        self.layout.addWidget(self.bg)
        container.setStyleSheet("background-color: rgba(255, 255, 255, 0.3);")

        self.employee.clicked.connect(self.show_employee_dialog)
        self.product.clicked.connect(self.show_product_dialog)
        self.order.clicked.connect(self.show_order_dialog)

        self.update_total()

    def update_total(self):
        self.right_incomebox_layout_val.setText(f"{DonHang.tong_doanh_thu():,} Đ")
        self.right_orderbox_layout_val.setText(f"{DonHang.count(where={'trang_thai': 3}):,}")
        self.right_employeebox_layout_val.setText(f"{NhanVien.count():,}")
        self.right_productbox_layout_val.setText(f"{SanPham.count():,}")

    def show_product_dialog(self):
        product_dialog = ProductDialog(self)
        product_dialog.show()

    def show_order_dialog(self):
        order_dialog = OrderDialog(self)
        order_dialog.show()

    def show_employee_dialog(self):
        employee_dialog = EmployeeDialog(self)
        employee_dialog.show()

    def logout_clicked(self):
        r = QMessageBox.question(self, 'Xác nhận', 'Bạn có chắc chắn muốn đăng xuất?', QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        if r == QMessageBox.StandardButton.No:
            return

        UserState.set_user(None)
        self.accept()
