# -*- coding:utf-8 -*-

import sys
from PySide2 import QtGui,QtWidgets,QtCore

class MyWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self,parent)

        self.setFixedSize(200, 120)

        self.btn_dialog = QtWidgets.QPushButton(u'打开文件')

        self.connect(self.btn_dialog,QtCore.SIGNAL('clicked()'), self,QtCore.SLOT('FullScreen()'))

        self.layout = QtWidgets.QVBoxLayout()
        self.layout.addWidget(self.btn_dialog)
        self.setLayout(self.layout)

    @QtCore.Slot()
    def openFileDialog(self):
        dialog = QtWidgets.QFileDialog()
        dialog.setFileMode(QtWidgets.QFileDialog.AnyFile)
        dialog.setViewMode(QtWidgets.QFileDialog.Detail)
        if dialog.exec_():
            fileName = dialog.selectedFiles()
            print(fileName)
    
    @QtCore.Slot()
    def FullScreen(self):
        self.showFullScreen()
        widget = QtWidgets.QWidget()
        widget.setFixedSize(300,200)
        label = QtWidgets.QLabel(u'副窗口')
        la=QtWidgets.QVBoxLayout()
        la.addWidget(label)
        widget.setLayout(la)
        widget.show()
        sys.exit(widget.exec_())
        

app = QtWidgets.QApplication()
widget = MyWidget()
widget.show()
sys.exit(app.exec_())