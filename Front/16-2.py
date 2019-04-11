from PySide2 import QtGui, QtWidgets, QtCore
import sys


class MyWidget01(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.layout = QtWidgets.QGridLayout(self)
        for i in range(4):
            for j in range(4):
                self.layout.addWidget(QtWidgets.QCheckBox(str(i) + '-' + str(j)), i, j, QtCore.Qt.AlignCenter)


class MyWidget02(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.layout = QtWidgets.QGridLayout(self)
        for i in range(3):
            for j in range(3):
                self.layout.addWidget(QtWidgets.QCheckBox(str(i) + '-' + str(j)), i, j, QtCore.Qt.AlignCenter)


class MyWidget03(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.layout = QtWidgets.QGridLayout(self)
        for i in range(2):
            for j in range(2):
                self.layout.addWidget(QtWidgets.QCheckBox(str(i) + '-' + str(j)), i, j, QtCore.Qt.AlignCenter)


app = QtWidgets.QApplication()

window = QtWidgets.QWidget()
window.setFixedSize(400, 300)

tabwidget = QtWidgets.QTabWidget(window)

tabwidget.addTab(MyWidget01(), u'电影类别')
tabwidget.addTab(MyWidget02(), u'书籍类别')
tabwidget.addTab(MyWidget03(), u'动物类型')

layout = QtWidgets.QVBoxLayout()
layout.addWidget(tabwidget)
window.setLayout(layout)
window.show()
sys.exit(app.exec_())