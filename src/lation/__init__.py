from pprint import pprint
from typing import List

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

from lation.manager import Manager


class LationWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        QMainWindow.__init__(self, *args, **kwargs)
        self.setWindowTitle("Lation")
        self.combo_box = QComboBox(self)

    def set_combo_options(self, options: List[str]):
        self.combo_box.addItems(options)
        self.setCentralWidget(self.combo_box)


def main():
    manager = Manager("/home/josue/PycharmProjects/lation/test.js")
    pprint(manager.topics.topics)
    # app = QApplication(sys.argv)
    # window = LationWindow()
    # window.show()
    # app.exec_()


if __name__ == '__main__':
    main()
