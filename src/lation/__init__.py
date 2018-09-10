import sys

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

from lation.parser import parse_js


class LationWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        QMainWindow.__init__(self, *args, **kwargs)
        self.setWindowTitle("Lation")

        self.combo_box = QComboBox(self)
        self.combo_box.addItems(["test", "test"])
        self.setCentralWidget(self.combo_box)


def main():
    app = QApplication(sys.argv)
    window = LationWindow()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
