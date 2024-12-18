from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QPushButton, QStackedLayout, QHBoxLayout, QWidget, QVBoxLayout, QLabel, \
    QGraphicsDropShadowEffect
from dialogs.employees import EmployeeDetailDialog
from models import NhanVien


class EmployeeSummary(QPushButton):
    def __init__(self, employee: NhanVien, parent=None):
        super(EmployeeSummary, self).__init__(parent)
        self.parent = parent
        self.clicked.connect(self.show_detail)
        self.setStyleSheet("background-color: transparent;")
        self.setFixedSize(500, 150)
        self.employee = employee
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
        self.top_left_container.setFixedWidth(150)
        self.top_left_container.setLayout(self.top_left)
        self.top.addWidget(self.top_left_container)

        self.img = QLabel(self)
        self.img.setPixmap(QPixmap("resources/person.png"))
        self.top_left.addWidget(self.img, alignment=Qt.AlignmentFlag.AlignCenter)

        self.id_label = QLabel("ID: 1")
        self.id_label.setStyleSheet("font-size: 12px; color: #716EEE; background-color: transparent; font-weight: bold;")
        self.top_left.addWidget(self.id_label, alignment=Qt.AlignmentFlag.AlignCenter)

        self.top_right = QVBoxLayout()
        self.top_right_container = QWidget()
        self.top_right_container.setLayout(self.top_right)
        self.top.addWidget(self.top_right_container)

        self.name = QLabel("HỌ VÀ TÊN")
        self.name.setStyleSheet("font-size: 18px; color: #000000; background-color: transparent; font-weight: bold;")
        self.top_right.addWidget(self.name, alignment=Qt.AlignmentFlag.AlignLeft)

        self.role = QLabel("Vai trò")
        self.role.setStyleSheet("font-size: 14px; color: #716EEE; background-color: transparent; font-weight: bold;")
        self.top_right.addWidget(self.role, alignment=Qt.AlignmentFlag.AlignLeft)

        self.phone = QLabel("0901234567")
        self.phone.setStyleSheet("font-size: 14px; color: #000000; background-color: transparent;")
        self.top_right.addWidget(self.phone, alignment=Qt.AlignmentFlag.AlignLeft)

        self.email = QLabel("Email")
        self.email.setStyleSheet("font-size: 14px; color: #000000; background-color: transparent;")
        self.top_right.addWidget(self.email, alignment=Qt.AlignmentFlag.AlignLeft)

        self.shadow = QGraphicsDropShadowEffect()
        self.shadow.setBlurRadius(30)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)

        self.frame = QLabel(self)
        self.frame.setStyleSheet("border: 1px solid #000000; border-radius: 10px; background-color: #ffffff; margin: 10px;")
        self.layout.addWidget(self.frame)
        self.frame.setGraphicsEffect(self.shadow)

        if self.employee is not None:
            self.name.setText(self.employee.ten_nv)
            self.role.setText(self.employee.vai_tro)
            self.phone.setText(self.employee.sdt)
            self.email.setText(self.employee.email)
            self.id_label.setText(f"ID: {self.employee.id}")
        else:
            self.setVisible(False)

    def show_detail(self):
        dialog = EmployeeDetailDialog(self.employee, self.parent)
        dialog.exec()
        self.parent.update_employees()
