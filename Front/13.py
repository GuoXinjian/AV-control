# -*- coding:utf-8 -*-
#! usr/bin/env python3

import sys
from PySide2 import QtGui,QtWidgets,QtCore

class Mywidget(QtWidgets.QWidget):
    def __init__(self,parent=None):
        QtWidgets.QWidget.__init__(self,parent)

        self.setFixedSize(400,300)

        self.btn_dialog = QtWidgets.QPushButton(u'打开文件')
        self.textLineEdit = QtWidgets.QLineEdit()
        self.textEdit = QtWidgets.QTextEdit()

        self.connect(self.btn_dialog,QtCore.SIGNAL('clicked()'),self,QtCore.SLOT('openFileDialog()'))

        self.layout = QtWidgets.QVBoxLayout()
        self.layout.addWidget(self.btn_dialog)
        self.layout.addWidget(self.textLineEdit)
        self.layout.addWidget(self.textEdit)
        self.setLayout(self.layout)

    @QtCore.Slot()
    def openFileDialog(self):
        dialog = QtWidgets.QFileDialog()

        dialog.fileSelected.connect(self.showtext)

        dialog.setFileMode(QtWidgets.QFileDialog.AnyFile)
        dialog.setViewMode(QtWidgets.QFileDialog.Detail)
        if dialog.exec_():
            self.textLineEdit.setText(dialog.selectedFiles()[0])

    @QtCore.Slot()
    def showtext(self,path):
        self.textEdit.setText(u'')
        fd = QtCore.QFile(path)
        if not fd.open(QtCore.QIODevice.ReadOnly | QtCore.QIODevice.Text):
            return
        data = QtCore.QTextStream(fd)
        while not data.atEnd():
            line = data.readLine()
            self.textEdit.append(line)
        fd.close()

app=QtWidgets.QApplication()
widget=Mywidget()
widget.show()
sys.exit(app.exec_())