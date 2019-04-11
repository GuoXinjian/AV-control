# -*- coding:utf-8 -*-
from PySide2 import QtGui, QtWidgets, QtCore
import sys


class MyWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.setFixedSize(300, 200)

    def paintEvent(self, event):
        painter = QtGui.QPainter(self)
        painter.setPen(QtCore.Qt.blue)
        rectangle = QtCore.QRect(10, 20, 80, 60)
        painter.drawRect(rectangle)


app = QtWidgets.QApplication()
window = MyWidget()
window.show()
sys.exit(app.exec_())