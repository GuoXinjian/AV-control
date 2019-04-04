# -*- coding:utf-8 -*-

from PySide2 import QtGui, QtWidgets, QtCore
import sys

class MyWidget(QtWidgets.QWidget):

    speak = QtCore.Signal(str)

    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)

        self.button = QtWidgets.QPushButton(u'发出信号', self)

        self.connect(self.button, QtCore.SIGNAL('clicked()'), self, QtCore.SLOT('myslot01()'))
        # self.connect(self, QtCore.SIGNAL('speak(int)'), self, QtCore.SLOT('myslot02(int)'))
        self.speak.connect(self.myslot02)

    @QtCore.Slot()
    def myslot01(self):
        s = 'hello world'
        self.speak.emit(s)

    @QtCore.Slot(str)
    def myslot02(self, words):
        print(words)


app = QtWidgets.QApplication(sys.argv)
widget = MyWidget()
widget.show()
sys.exit(app.exec_())