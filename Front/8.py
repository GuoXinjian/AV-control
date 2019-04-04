# -*- coding:utf-8 -*-

import sys
from PySide2 import QtCore, QtGui, QtWidgets

class MyWidget(QtWidgets.QWidget):
    def __init__(self,parent=None):
        QtWidgets.QWidget.__init__(self, parent)

        self.setFixedSize(200, 120)

        self.btn_dialog = QtWidgets.QPushButton(u'弹出对话窗')

        self.connect(self.btn_dialog, QtCore.SIGNAL('clicked()'), self, QtCore.SLOT('openMessageBox()'))

        self.layout = QtWidgets.QVBoxLayout()
        self.layout.addWidget(self.btn_dialog)
        self.setLayout(self.layout)

    @QtCore.Slot()
    def openMessageBox(self):
        msgBox = QtWidgets.QMessageBox()
        msgBox.setText(u'你好世界')
        msgBox.exec_()

app = QtWidgets.QApplication()
widget= MyWidget()
widget.show()
sys.exit(app.exec_())