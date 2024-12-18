from PySide6.QtCore import Qt
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QDialog, QStackedLayout, QLabel, QVBoxLayout, QLineEdit, QPushButton, \
    QGraphicsDropShadowEffect, QWidget, QMessageBox
from models import NhanVien
from states import UserState


class LoginDialog(QDialog):
    def __init__(self, parent=None):
        super(LoginDialog, self).__init__(parent)
        self.setFixedSize(600, 600)
        self.setGeometry(100, 100, 600, 600)
        self.setStyleSheet("background-color: #ffffff;")
        self.layout = QStackedLayout()
        self.layout.setStackingMode(QStackedLayout.StackingMode.StackAll)
        self.setLayout(self.layout)
        self.bg = QLabel(self)
        self.bg.setStyleSheet("background-color: rgba(0, 0, 0, 0.15); background-image: url('resources/login-bg.png'); margin: 120px 50px 50px; border-radius: 10px; background-repeat: no-repeat; background-position: center;")
        self.top = QVBoxLayout()
        self.top.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.top.setSpacing(50)
        self.setWindowTitle("Đăng nhập")

        self.title = QLabel("ĐĂNG NHẬP", self)
        self.title.setStyleSheet("font-size: 24px; font-weight: bold; color: #000000; padding: 20px 0; margin: 0 0 60px; background-color: transparent;")
        self.top.addWidget(self.title, alignment=Qt.AlignmentFlag.AlignCenter)

        self.username = QLineEdit(self)
        self.username.setPlaceholderText("Tên đăng nhập")
        self.username.setStyleSheet("border-radius: 10px; font-size: 18px; border: 1px solid #398cfb; background-color: #eff4fa; padding: 10px;")
        self.username.setClearButtonEnabled(True)
        self.username.addAction(QIcon("resources/username.png"), QLineEdit.ActionPosition.LeadingPosition)
        self.username.setFixedWidth(350)
        self.username.setFixedHeight(50)
        self.top.addWidget(self.username)

        self.password = QLineEdit(self)
        self.password.setPlaceholderText("Mật khẩu")
        self.password.setStyleSheet("border-radius: 10px; font-size: 18px; border: 1px solid #398cfb; background-color: #eff4fa; padding: 10px;")
        self.password.setClearButtonEnabled(True)
        self.password.addAction(QIcon("resources/password.png"), QLineEdit.ActionPosition.LeadingPosition)
        self.password.setEchoMode(QLineEdit.EchoMode.Password)
        self.password.setFixedWidth(350)
        self.password.setFixedHeight(50)
        self.top.addWidget(self.password)

        self.login = QPushButton("Đăng nhập", self)
        self.login.shadow = QGraphicsDropShadowEffect()
        self.login.shadow.setBlurRadius(30)
        self.login.shadow.setXOffset(0)
        self.login.shadow.setYOffset(0)
        self.login.setGraphicsEffect(self.login.shadow)
        self.login.setStyleSheet(
            "background-color: #398cfb; color: #ffffff; font-size: 18px; padding: 10px 20px; border-radius: 10px; font-weight: bold;")
        self.login.setCursor(Qt.CursorShape.PointingHandCursor)
        self.login.setFixedWidth(200)
        self.login.setFixedHeight(45)
        self.login.clicked.connect(self.dang_nhap)

        self.top.addWidget(self.login, alignment=Qt.AlignmentFlag.AlignCenter)
        container = QWidget()
        container.setLayout(self.top)
        self.layout.addWidget(container)
        self.layout.addWidget(self.bg)
        container.setStyleSheet("background-color: rgba(255, 255, 255, 0.15);")

    def dang_nhap(self):
        if NhanVien.dang_nhap(self.username.text(), self.password.text()):
            UserState.set_user(NhanVien.fetch_all(where={"ten_dang_nhap": self.username.text()})[0])
            self.accept()
        else:
            QMessageBox.warning(self, "Thông báo", "Đăng nhập thất bại")
