# This Python file uses the following encoding: utf-8
# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtWidgets import QApplication, QMainWindow

from ui_register import Ui_RegisterWindow

class RegisterWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_RegisterWindow()
        self.ui.setupUi(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = RegisterWindow()
    # -----------------------------------
    # -----------------------------------
    widget.show()
    sys.exit(app.exec())
