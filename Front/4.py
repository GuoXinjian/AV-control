# -*- coding:utf-8 -*-

import sys
from PySide2 import QtCore,QtGui,QtWidgets

class MyWidget(QtWidgets.QWidget):

    def __init__(self,parent=None):
        QtWidgets.QWidget.__init__(self,parent)

        self.setFixedSize(200,120)

        self.quit = QtWidgets.QPushButton('Quit',self)
        self.quit.setGeometry(62,40,75,30)
        self.quit.setFont(QtGui.QFont('Times',18,QtGui.QFont.Bold))

        self.connect(self.quit,QtCore.SIGNAL('clicked()'),QtWidgets.qApp,QtCore.SLOT('quit()'))

app = QtWidgets.QApplication(sys.argv)
widget = MyWidget()
widget.show()
sys.exit(app.exec_())