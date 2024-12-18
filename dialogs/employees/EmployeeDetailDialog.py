from PySide6.QtCore import Qt
from PySide6.QtWidgets import QDialog, QStackedLayout, QLabel, QVBoxLayout, QLineEdit, QPushButton, \
    QGraphicsDropShadowEffect, QWidget, QMessageBox
from models import NhanVien, QuyenHan
from states import UserState


class EmployeeDetailDialog(QDialog):
    def __init__(self, employee: NhanVien = None, parent=None):
        super(EmployeeDetailDialog, self).__init__(parent)
        self.employee = employee
        self.setFixedSize(600, 600)
        self.setGeometry(100, 100, 600, 600)
        self.setStyleSheet("background-color: #ffffff;")
        self.layout = QStackedLayout()
        self.layout.setStackingMode(QStackedLayout.StackingMode.StackAll)
        self.setLayout(self.layout)
        self.bg = QLabel(self)
        self.bg.setStyleSheet("background-color: transparent; background-image: url('resources/form-bg.png'); margin: 120px 50px 50px; border-radius: 10px; background-repeat: no-repeat; background-position: center;")
        self.top = QVBoxLayout()
        self.top.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.top.setSpacing(10)
        self.setWindowTitle("Nhân viên")

        self.name = QLineEdit(self)
        self.name.setPlaceholderText("Tên nhân viên")
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

        self.email = QLineEdit(self)
        self.email.setPlaceholderText("Email")
        self.email.setStyleSheet("border-radius: 10px; font-size: 18px; border: 1px solid #398cfb; background-color: #eff4fa; padding: 10px;")
        self.email.setFixedWidth(350)
        self.email.setFixedHeight(50)
        self.top.addWidget(self.email)

        self.phone = QLineEdit(self)
        self.phone.setPlaceholderText("Số điện thoại")
        self.phone.setStyleSheet(
            "border-radius: 10px; font-size: 18px; border: 1px solid #398cfb; background-color: #eff4fa; padding: 10px;")
        self.phone.setFixedWidth(350)
        self.phone.setFixedHeight(50)
        self.top.addWidget(self.phone)

        self.role = QLineEdit(self)
        self.role.setPlaceholderText("Vai trò")
        self.role.setStyleSheet("border-radius: 10px; font-size: 18px; border: 1px solid #398cfb; background-color: #eff4fa; padding: 10px;")
        self.role.setFixedWidth(350)
        self.role.setFixedHeight(50)
        self.top.addWidget(self.role)

        self.username = QLineEdit(self)
        self.username.setPlaceholderText("Tên đăng nhập")
        self.username.setStyleSheet(
            "border-radius: 10px; font-size: 18px; border: 1px solid #398cfb; background-color: #eff4fa; padding: 10px;")
        self.username.setFixedWidth(350)
        self.username.setFixedHeight(50)
        self.top.addWidget(self.username)

        self.password = QLineEdit(self)
        self.password.setPlaceholderText("Mật khẩu (nhập nếu muốn thay đổi)")
        self.password.setStyleSheet(
            "border-radius: 10px; font-size: 18px; border: 1px solid #398cfb; background-color: #eff4fa; padding: 10px;")
        self.password.setFixedWidth(350)
        self.password.setFixedHeight(50)
        self.password.setEchoMode(QLineEdit.EchoMode.Password)
        self.top.addWidget(self.password)

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

        self.make_admin_btn = QPushButton("Đề cử làm admin", self)
        self.make_admin_btn.shadow = QGraphicsDropShadowEffect()
        self.make_admin_btn.shadow.setBlurRadius(30)
        self.make_admin_btn.shadow.setXOffset(0)
        self.make_admin_btn.shadow.setYOffset(0)
        self.make_admin_btn.setGraphicsEffect(self.make_admin_btn.shadow)
        self.make_admin_btn.setStyleSheet(
            "background-color: red; color: #ffffff; font-size: 18px; padding: 10px 20px; border-radius: 10px; font-weight: bold;")
        self.make_admin_btn.setCursor(Qt.CursorShape.PointingHandCursor)
        self.make_admin_btn.setFixedWidth(200)
        self.make_admin_btn.setFixedHeight(45)
        self.top.addWidget(self.make_admin_btn, alignment=Qt.AlignmentFlag.AlignCenter)

        if employee is None:
            self.delete.setVisible(False)
            self.make_admin_btn.setVisible(False)

        if UserState.get_user().quyen_han != QuyenHan["QUAN_LY"]:
            self.name.setReadOnly(True)
            self.address.setReadOnly(True)
            self.email.setReadOnly(True)
            self.role.setReadOnly(True)
            self.username.setReadOnly(True)
            self.phone.setReadOnly(True)
            self.password.setReadOnly(True)
            self.save.setVisible(False)
            self.delete.setVisible(False)
            self.make_admin_btn.setVisible(False)

        container = QWidget()
        container.setLayout(self.top)
        self.layout.addWidget(container)
        self.layout.addWidget(self.bg)
        container.setStyleSheet("background-color: rgba(255, 255, 255, 0.45);")

        if employee is not None:
            self.name.setText(employee.ten_nv)
            self.address.setText(employee.dia_chi)
            self.email.setText(employee.email)
            self.role.setText(employee.vai_tro)
            self.username.setText(employee.ten_dang_nhap)
            self.phone.setText(employee.sdt)

        self.save.clicked.connect(self.save_employee)
        self.delete.clicked.connect(self.delete_employee)
        self.make_admin_btn.clicked.connect(self.make_admin)

    def make_admin(self):
        if self.employee is not None:
            if self.employee.quyen_han == QuyenHan["QUAN_LY"]:
                QMessageBox.warning(self, "Thông báo", "Nhân viên này đã là admin")
                return
            self.employee.make_admin()
        self.accept()

    def save_employee(self):
        if self.name.text() == "" or self.address.text() == "" or self.email.text() == "" or self.role.text() == "" or self.username.text() == "" or self.phone.text() == "":
            QMessageBox.warning(self, "Thông báo", "Vui lòng điền đầy đủ thông tin")
            return
        if self.employee is not None:
            if len(self.password.text()) > 0:
                self.employee.update(mat_khau=self.password.text())
            self.employee.update(ten_nv=self.name.text(), dia_chi=self.address.text(), email=self.email.text(), vai_tro=self.role.text(), ten_dang_nhap=self.username.text(), sdt=self.phone.text())
        else:
            if self.password.text() == "":
                QMessageBox.warning(self, "Thông báo", "Vui lòng nhập mật khẩu")
                return
            employee = NhanVien(ten_nv=self.name.text(), dia_chi=self.address.text(), email=self.email.text(), vai_tro=self.role.text(), ten_dang_nhap=self.username.text(), mat_khau=self.password.text(), sdt=self.phone.text())
            employee.save()
        self.accept()

    def delete_employee(self):
        if self.employee is not None:
            self.employee.delete()
        self.accept()
