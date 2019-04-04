# -*- coding:utf-8 -*-

import sys
from PySide2 import QtCore, QtGui, QtWidgets

class LCDRange(QtWidgets.QWidget):

    valueChanged = QtCore.Signal(int)
    def __init__(self,parent=None):
        QtWidgets.QWidget.__init__(self,parent)

        lcd = QtWidgets.QLCDNumber(2)

        self.slider = QtWidgets.QSlider(QtCore.Qt.Horizontal)
        self.slider.setRange(0,99)
        self.slider.setValue(0)
        
        self.connect(self.slider,QtCore.SIGNAL('valueChanged(int)'),lcd,QtCore.SLOT('display(int)'))
        self.connect(self.slider,QtCore.SIGNAL('valueChanged(int)'),self,QtCore.SIGNAL('valueChanged(int)'))

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(lcd)
        layout.addWidget(self.slider)
        self.setLayout(layout)


    def value(self):
        return self.slider.value()

    @QtCore.Slot(int)
    def setValue(self,value):
        self.slider.setValue(value)

class MyWidget(QtWidgets.QWidget):
    def __init__(self,parent=None):
        QtWidgets.QWidget.__init__(self,parent)

        quit = QtWidgets.QPushButton("Quit")
        quit.setFont(QtGui.QFont("Times", 18, QtGui.QFont.Bold))

        self.connect(quit, QtCore.SIGNAL("clicked()"),QtWidgets.qApp, QtCore.SLOT("quit()"))
        grid = QtWidgets.QGridLayout()
        previousRange = None

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(quit)
        layout.addLayout(grid)
        self.setLayout(layout)

        for row in range(3):
            for column in range(3):
                lcdRange = LCDRange()
                grid.addWidget(lcdRange, row, column)
                if previousRange:
                    self.connect(lcdRange, QtCore.SIGNAL("valueChanged(int)"),previousRange.setValue)
                previousRange = lcdRange

app = QtWidgets.QApplication(sys.argv)
widget = MyWidget()
widget.show()
sys.exit(app.exec_())