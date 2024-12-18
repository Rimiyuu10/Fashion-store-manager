from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QPushButton, QStackedLayout, QHBoxLayout, QWidget, QVBoxLayout, QLabel, \
    QGraphicsDropShadowEffect

from dialogs.orders.OrderDetailDialog import OrderDetailDialog
from models import DonHang


class OrderSummary(QPushButton):
    def __init__(self, order: DonHang, parent=None):
        super(OrderSummary, self).__init__(parent)
        self.parent = parent
        self.clicked.connect(self.show_detail)
        self.setStyleSheet("background-color: transparent;")
        self.setFixedSize(500, 150)
        self.order = order
        self.layout = QStackedLayout()
        self.setLayout(self.layout)
        self.layout.setStackingMode(QStackedLayout.StackingMode.StackAll)

        self.top = QHBoxLayout()
        self.top.setSpacing(10)
        self.top_container = QWidget()
        self.top_container.setLayout(self.top)
        self.layout.addWidget(self.top_container)

        self.top_left = QVBoxLayout()
        self.top_left.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.top_left_container = QWidget()
        self.top_left_container.setFixedWidth(80)
        self.top_left_container.setLayout(self.top_left)
        self.top.addWidget(self.top_left_container)

        self.img = QLabel(self)
        if self.order is not None:
            if self.order.trang_thai == 1:
                self.img.setPixmap(QPixmap("resources/status-wait.png"))
            elif self.order.trang_thai == 2:
                self.img.setPixmap(QPixmap("resources/status-deliver.png"))
            elif self.order.trang_thai == 3:
                self.img.setPixmap(QPixmap("resources/status-done.png"))
            elif self.order.trang_thai == 4:
                self.img.setPixmap(QPixmap("resources/status-cancel.png"))

        self.top_left.addWidget(self.img, alignment=Qt.AlignmentFlag.AlignCenter)

        self.id_label = QLabel("ID: 1")
        self.id_label.setStyleSheet("font-size: 12px; color: #716EEE; background-color: transparent; font-weight: bold;")
        self.top_left.addWidget(self.id_label, alignment=Qt.AlignmentFlag.AlignCenter)

        self.top_right = QVBoxLayout()
        self.top_right_container = QWidget()
        self.top_right_container.setLayout(self.top_right)
        self.top.addWidget(self.top_right_container)

        self.name = QLabel("Họ và Tên")
        self.name.setStyleSheet("font-size: 18px; color: #000000; background-color: transparent; font-weight: bold;")
        self.top_right.addWidget(self.name, alignment=Qt.AlignmentFlag.AlignLeft)

        self.phone = QLabel("0901234567")
        self.phone.setStyleSheet("font-size: 14px; color: #716EEE; background-color: transparent; font-weight: bold;")
        self.top_right.addWidget(self.phone, alignment=Qt.AlignmentFlag.AlignLeft)

        self.address = QLabel("Địa chỉ đơn hàng")
        self.address.setStyleSheet("font-size: 14px; color: #000000; background-color: transparent;")
        self.top_right.addWidget(self.address, alignment=Qt.AlignmentFlag.AlignLeft)

        self.total = QLabel("100.000 Đ")
        self.total.setStyleSheet("font-size: 18px; color: red; background-color: transparent; font-weight: bold;")
        self.top_right.addWidget(self.total, alignment=Qt.AlignmentFlag.AlignLeft)

        self.shadow = QGraphicsDropShadowEffect()
        self.shadow.setBlurRadius(30)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)

        self.frame = QLabel(self)
        self.frame.setStyleSheet("border: 1px solid #000000; border-radius: 10px; background-color: #ffffff; margin: 10px;")
        self.layout.addWidget(self.frame)
        self.frame.setGraphicsEffect(self.shadow)

        if self.order is not None:
            self.name.setText(self.order.nguoi_mua)
            self.phone.setText(self.order.sdt_nguoi_mua)
            self.address.setText(self.order.dia_chi_giao_hang)
            self.total.setText(f"{self.order.tong_tien:,} Đ")
            self.id_label.setText(f"ID: {self.order.id}")
        else:
            self.setVisible(False)

    def show_detail(self):
        dialog = OrderDetailDialog(self.order, self.parent)
        dialog.exec()
        self.parent.update_orders()
