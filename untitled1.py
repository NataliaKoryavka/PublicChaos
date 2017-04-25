# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 01:41:46 2017

@author: Наталья
"""

import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QToolTip)
from PyQt5.QtGui import QIcon,QFont
from PyQt5.QtCore import QCoreApplication


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):
        QToolTip.setFont(QFont('SansSerif', 10))
        self.setToolTip('This is a <b>QWidget</b> widget')

        btn = QPushButton('Quit', self)
        btn.clicked.connect(QCoreApplication.instance().quit)
        btn.setToolTip('This is a <b>QPushButton</b> widget')
        btn.resize(btn.sizeHint())
        btn.move(50, 50)

        self.setGeometry(1000, 300, 700, 500)
        self.setWindowTitle('MyApplication')
        self.setWindowIcon(QIcon('E:\дз2курс\инфа\Тренировка\крест.jpg'))

        self.show()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    app.exec_()