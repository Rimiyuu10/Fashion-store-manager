from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QDialog, QStackedLayout, QLabel, QVBoxLayout, QHBoxLayout, QLineEdit, QComboBox, \
    QGridLayout, QPushButton, QGraphicsDropShadowEffect, QWidget, QMessageBox
from dialogs.orders import OrderDetailDialog, OrderSummary
from models import QuyenHan, DonHang
from states import UserState


class OrderDialog(QDialog):
    def __init__(self, parent=None):
        super(OrderDialog, self).__init__(parent)
        self.setWindowTitle("Quản lý đơn hàng")
        self.setFixedSize(1200, 675)
        self.setGeometry(100, 100, 1200, 675)
        self.setStyleSheet("background-color: #ffffff;")
        self.layout = QStackedLayout()
        self.layout.setStackingMode(QStackedLayout.StackingMode.StackAll)
        self.setLayout(self.layout)
        self.bg = QLabel(self)
        self.bg.setStyleSheet(
            "background-color: #ffffff; background-image: url('resources/shop-bg.png'); background-repeat: no-repeat; background-position: center;")
        self.top = QVBoxLayout()
        self.top.setAlignment(Qt.AlignmentFlag.AlignJustify)
        self.top.setSpacing(5)

        self.top_top = QHBoxLayout()
        self.top_top.setAlignment(Qt.AlignmentFlag.AlignJustify)
        self.top_top.setSpacing(200)

        self.search_box = QLineEdit(self)
        self.search_box.setPlaceholderText("Nhập từ khoá hoặc ID")
        self.search_box.setStyleSheet(
            "border-radius: 10px; font-size: 14px; border: 1px solid #398cfb; background-color: #eff4fa; padding: 10px;")
        self.search_box.setClearButtonEnabled(True)
        self.search_box.addAction(QIcon("resources/lookup.png"), QLineEdit.ActionPosition.LeadingPosition)
        self.search_box.setFixedWidth(400)
        self.search_box.setFixedHeight(50)
        self.top_top.addWidget(self.search_box)

        self.sort_box = QComboBox(self)
        self.sort_box.addItem("Sắp xếp: ID (A-Z)")
        self.sort_box.addItem("Sắp xếp: ID (Z-A)")
        self.sort_box.addItem("Sắp xếp: Tên (A-Z)")
        self.sort_box.addItem("Sắp xếp: Tên (Z-A)")
        self.sort_box.setStyleSheet(
            "border-top-left-radius: 10px; border-bottom-left-radius: 10px; font-size: 14px; border: 1px solid #398cfb; background-color: #eff4fa; padding: 10px;")
        self.sort_box.setFixedWidth(160)
        self.sort_box.setFixedHeight(50)
        self.top_top.addWidget(self.sort_box)

        self.top_mid = QGridLayout()
        self.top_mid.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.top_mid.setSpacing(10)

        self.top_bot = QHBoxLayout()
        self.top_bot.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.top_bot.setSpacing(20)

        self.begin_btn = QPushButton("1", self)
        self.begin_btn.setStyleSheet(
            "background-color: #398CFB; color: #ffffff; font-size: 18px; border-radius: 10px; font-weight: bold; padding: 12px 17px; margin: 0 30px 0 200px;")
        self.begin_btn.shadow = QGraphicsDropShadowEffect()
        self.begin_btn.shadow.setBlurRadius(30)
        self.begin_btn.shadow.setXOffset(0)
        self.begin_btn.shadow.setYOffset(0)
        self.begin_btn.setGraphicsEffect(self.begin_btn.shadow)
        self.top_bot.addWidget(self.begin_btn)

        self.prev_btn = QPushButton("2", self)
        self.prev_btn.setStyleSheet(
            "background-color: #398CFB; color: #ffffff; font-size: 18px; border-radius: 10px; font-weight: bold; padding: 12px 17px;")
        self.prev_btn.shadow = QGraphicsDropShadowEffect()
        self.prev_btn.shadow.setBlurRadius(30)
        self.prev_btn.shadow.setXOffset(0)
        self.prev_btn.shadow.setYOffset(0)
        self.prev_btn.setGraphicsEffect(self.prev_btn.shadow)
        self.top_bot.addWidget(self.prev_btn)

        self.current_btn = QPushButton("3", self)
        self.current_btn.setStyleSheet(
            "background-color: #716EEE; color: #ffffff; font-size: 18px; border-radius: 10px; font-weight: bold; padding: 12px 17px;")
        self.current_btn.shadow = QGraphicsDropShadowEffect()
        self.current_btn.shadow.setBlurRadius(30)
        self.current_btn.shadow.setXOffset(0)
        self.current_btn.shadow.setYOffset(0)
        self.current_btn.setGraphicsEffect(self.current_btn.shadow)
        self.top_bot.addWidget(self.current_btn)

        self.following_btn = QPushButton("4", self)
        self.following_btn.setStyleSheet(
            "background-color: #398CFB; color: #ffffff; font-size: 18px; border-radius: 10px; font-weight: bold; padding: 12px 17px;")
        self.following_btn.shadow = QGraphicsDropShadowEffect()
        self.following_btn.shadow.setBlurRadius(30)
        self.following_btn.shadow.setXOffset(0)
        self.following_btn.shadow.setYOffset(0)
        self.following_btn.setGraphicsEffect(self.following_btn.shadow)
        self.top_bot.addWidget(self.following_btn)

        self.end_btn = QPushButton("10", self)
        self.end_btn.setStyleSheet(
            "background-color: #398CFB; color: #ffffff; font-size: 18px; border-radius: 10px; font-weight: bold; padding: 12px 17px; margin: 0 200px 0 30px;")
        self.end_btn.shadow = QGraphicsDropShadowEffect()
        self.end_btn.shadow.setBlurRadius(30)
        self.end_btn.shadow.setXOffset(0)
        self.end_btn.shadow.setYOffset(0)
        self.end_btn.setGraphicsEffect(self.end_btn.shadow)
        self.top_bot.addWidget(self.end_btn)

        container = QWidget()
        container.setLayout(self.top)
        container_top = QWidget()
        container_top.setLayout(self.top_top)
        container_mid = QWidget()
        container_mid.setLayout(self.top_mid)
        container_mid.setFixedHeight(500)
        container_bottom = QWidget()
        container_bottom.setLayout(self.top_bot)
        self.top.addWidget(container_top)
        self.top.addWidget(container_mid)
        self.top.addWidget(container_bottom)

        self.prev_dialog = QPushButton(self)
        self.prev_dialog.setStyleSheet(
            "background-color: #716EEE; border-radius: 40; font-weight: bold;")
        self.prev_dialog.setCursor(Qt.CursorShape.PointingHandCursor)
        self.prev_dialog.setIcon(QIcon("resources/prev.png"))
        self.prev_dialog.setIconSize(QSize(50, 50))
        self.prev_dialog.setFixedSize(80, 80)
        self.prev_dialog.shadow = QGraphicsDropShadowEffect()
        self.prev_dialog.shadow.setBlurRadius(30)
        self.prev_dialog.shadow.setXOffset(0)
        self.prev_dialog.shadow.setYOffset(0)
        self.prev_dialog.setGraphicsEffect(self.prev_dialog.shadow)
        self.top_bot.insertWidget(0, self.prev_dialog)

        self.new_dialog = QPushButton(self)
        self.new_dialog.setStyleSheet(
            "background-color: transparent;")
        self.new_dialog.setCursor(Qt.CursorShape.PointingHandCursor)
        self.new_dialog.setFixedSize(80, 80)
        self.new_dialog.setIcon(QIcon("resources/add.png"))
        self.new_dialog.setIconSize(QSize(80, 80))
        self.new_dialog.shadow = QGraphicsDropShadowEffect()
        self.new_dialog.shadow.setBlurRadius(30)
        self.new_dialog.shadow.setXOffset(0)
        self.new_dialog.shadow.setYOffset(0)
        self.new_dialog.setGraphicsEffect(self.new_dialog.shadow)
        self.top_bot.addWidget(self.new_dialog)

        self.layout.addWidget(container)
        self.layout.addWidget(self.bg)

        container.setStyleSheet("background-color: rgba(255, 255, 255, 0.3);")

        self.current_page = 1
        self.perpage = 6
        self.total = 0
        self.max_page = 0
        self.orders = []
        self.prev_btn.clicked.connect(lambda: self.update_page(self.current_page - 1))
        self.following_btn.clicked.connect(lambda: self.update_page(self.current_page + 1))
        self.begin_btn.clicked.connect(lambda: self.update_page(1))
        self.end_btn.clicked.connect(lambda: self.update_page(self.max_page))
        self.prev_btn.setFixedWidth(50)
        self.current_btn.setFixedWidth(50)
        self.following_btn.setFixedWidth(50)
        self.begin_btn.setFixedWidth(300)
        self.end_btn.setFixedWidth(300)
        self.search_box.textChanged.connect(lambda: self.update_page(1))
        self.sort_box.currentIndexChanged.connect(lambda: self.update_page(1))
        self.prev_dialog.clicked.connect(self.back_to_main)
        self.new_dialog.clicked.connect(self.show_new_dialog)
        self.update_orders()

    def show_new_dialog(self):
        if UserState.get_user().quyen_han != QuyenHan["QUAN_LY"]:
            QMessageBox.warning(self, "Thông báo", "Bạn không có quyền truy cập")
            return
        dialog = OrderDetailDialog(None, self)
        dialog.exec()
        self.update_orders()

    def back_to_main(self):
        self.parent().update_total()
        self.accept()

    def update_page(self, page):
        self.current_page = page
        self.update_orders()

    def update_orders(self):
        order_by = "id"
        if self.sort_box.currentIndex() == 1:
            order_by = "id DESC"
        elif self.sort_box.currentIndex() == 2:
            order_by = "nguoi_mua"
        elif self.sort_box.currentIndex() == 3:
            order_by = "nguoi_mua DESC"
        if self.search_box.text() != "":
            if self.search_box.text().isdigit():
                self.orders = DonHang.fetch_all(where={"id": self.search_box.text()}, offset=(self.current_page - 1) * self.perpage, limit=self.perpage, order_by=order_by)
                self.total = DonHang.count(where={"id": self.search_box.text()})
            else:
                self.orders = DonHang.fetch_all(like={"nguoi_mua": self.search_box.text()}, offset=(self.current_page - 1) * self.perpage, limit=self.perpage, order_by=order_by)
                self.total = DonHang.count(like={"nguoi_mua": self.search_box.text()})
        else:
            self.total = DonHang.count()
            self.orders = DonHang.fetch_all(offset=(self.current_page - 1) * self.perpage, limit=self.perpage, order_by=order_by)

        self.max_page = (self.total // self.perpage + 1) if self.total % self.perpage != 0 else (self.total // self.perpage)
        self.current_btn.setText(str(self.current_page))
        self.prev_btn.setText(str(self.current_page - 1))
        self.following_btn.setText(str(self.current_page + 1))
        self.end_btn.setText(str(self.max_page))

        if self.current_page > 1 and self.current_page > self.max_page:
            self.current_page = self.max_page
            self.update_orders()
            return

        for i in reversed(range(self.top_mid.count())):
            self.top_mid.itemAt(i).widget().deleteLater()

        for i in range(3):
            for j in range(2):
                order = OrderSummary(self.orders[i * 2 + j] if (i * 2 + j < len(self.orders)) else None, self)
                self.top_mid.addWidget(order, i, j)

        if self.current_page <= 2:
            self.begin_btn.setText(" ")
            self.begin_btn.setStyleSheet("background-color: transparent;")
        else:
            self.begin_btn.setText("1")
            self.begin_btn.setStyleSheet("background-color: #398CFB; color: #ffffff; font-size: 18px; border-radius: 10px; font-weight: bold; padding: 12px 17px; margin: 0 30px 0 200px;")

        if self.current_page == 1:
            self.prev_btn.setText(" ")
            self.prev_btn.setStyleSheet("background-color: transparent;")
        else:
            self.prev_btn.setText(str(self.current_page - 1))
            self.prev_btn.setStyleSheet("background-color: #398CFB; color: #ffffff; font-size: 18px; border-radius: 10px; font-weight: bold; padding: 12px 17px;")

        if self.max_page == 0:
            self.current_btn.setText(" ")
            self.current_btn.setStyleSheet("background-color: transparent;")
        else:
            self.current_btn.setText(str(self.current_page))
            self.current_btn.setStyleSheet("background-color: #716EEE; color: #ffffff; font-size: 18px; border-radius: 10px; font-weight: bold; padding: 12px 17px;")


        if self.current_page == self.max_page or self.max_page == 0:
            self.following_btn.setText(" ")
            self.following_btn.setStyleSheet("background-color: transparent;")
        else:
            self.following_btn.setText(str(self.current_page + 1))
            self.following_btn.setStyleSheet("background-color: #398CFB; color: #ffffff; font-size: 18px; border-radius: 10px; font-weight: bold; padding: 12px 17px;")

        if self.current_page >= self.max_page - 1:
            self.end_btn.setText(" ")
            self.end_btn.setStyleSheet("background-color: transparent;")
        else:
            self.end_btn.setText(str(self.max_page))
            self.end_btn.setStyleSheet("background-color: #398CFB; color: #ffffff; font-size: 18px; border-radius: 10px; font-weight: bold; padding: 12px 17px; margin: 0 200px 0 30px;")
