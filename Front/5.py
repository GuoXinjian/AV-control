# -*- coding:utf-8 -*-

import sys
from PySide2 import QtCore,QtGui,QtWidgets

class MyWidget(QtWidgets.QWidget):
    def __init__(self,parent=None):
        QtWidgets.QWidget.__init__(self,parent)

        quit = QtWidgets.QPushButton('Quit',self)
        quit.setFont(QtGui.QFont("Times", 18, QtGui.QFont.Bold))

        lcd = QtWidgets.QLCDNumber(2,self)

        slider = QtWidgets.QSlider(QtCore.Qt.Vertical,self)
        slider.setRange(0,99)
        slider.setValue(0)

        self.connect(quit,QtCore.SIGNAL('clicked()'),QtWidgets.qApp,QtCore.SLOT('quit()'))
        self.connect(slider,QtCore.SIGNAL('valueChanged(int)'),lcd,QtCore.SLOT('display(int)'))

        layout = QtWidgets.QVBoxLayout(self)
        layout.addWidget(quit)
        layout.addWidget(lcd)
        layout.addWidget(slider)
        self.setLayout(layout)

app = QtWidgets.QApplication(sys.argv)
widget =  MyWidget()
widget.show()
sys.exit(app.exec_())