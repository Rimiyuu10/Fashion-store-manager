from PySide6.QtWidgets import *
from dialogs.login import LoginDialog
from dialogs.main import MainDialog

if __name__ == '__main__':
    app = QApplication([])
    while True:
        login = LoginDialog()
        if login.exec() == QDialog.DialogCode.Accepted:
            main = MainDialog()
            if main.exec() == QDialog.DialogCode.Rejected:
                break
        else:
            break
    app.quit()
