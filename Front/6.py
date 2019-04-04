# -*- coding:utf-8 -*-

import sys
from PySide2 import QtCore,QtGui,QtWidgets

class LCDRange(QtWidgets.QWidget):
    def __init__(self,parent=None):
        QtWidgets.QWidget.__init__(self,parent)

        lcd = QtWidgets.QLCDNumber(2)
        slider = QtWidgets.QSlider(QtCore.Qt.Horizontal)
        slider.setRange(0,99)
        slider.setValue(0)
        self.connect(slider,QtCore.SIGNAL('valueChanged(int)'),lcd,QtCore.SLOT('display(int)'))
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(lcd)
        layout.addWidget(slider)
        self.setLayout(layout)

class MYWidget(QtWidgets.QWidget):
    def __init__(self,parent=None):
        QtWidgets.QWidget.__init__(self,parent)

        quit = QtWidgets.QPushButton('Quit')
        quit.setFont(QtGui.QFont('Times',18,QtGui.QFont.Bold))
        self.connect(quit,QtCore.SIGNAL('clicked()'),QtWidgets.qApp,QtCore.SLOT('quit()'))

        grid = QtWidgets.QGridLayout()
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(quit)
        layout.addLayout(grid)
        self.setLayout(layout)
        for row in range(3):
            for column in range(3):
                grid.addWidget(LCDRange(),row,column)

app = QtWidgets.QApplication(sys.argv)
widget = MYWidget()
widget.resize(800,600)
widget.show()
sys.exit(app.exec_())