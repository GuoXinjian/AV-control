#! usr/bin/env python3
# -*- coding:utf-8 -*-

from PySide2 import QtGui,QtCore,QtWidgets
import sys

class MyWidget(QtWidgets.QWidget):
    def __init__(self,parent=None):
        QtWidgets.QWidget.__init__(self,parent)
        self.setFixedSize(300,200)

    def enterEvent(self,event):
        print(event.type())
        print('in')

    def closeEvent(self,event):
        print('out')
    
    def moveEvent(self,event):
        print('move')
    
    def showEvent(self,event):
        print('show')

app = QtWidgets.QApplication()
window = MyWidget()
window.show()
sys.exit(app.exec_())