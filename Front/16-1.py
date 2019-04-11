# -*- coding:utf-8 -*-
from PySide2 import QtGui, QtWidgets, QtCore
import sys


app = QtWidgets.QApplication()
tabwidget = QtWidgets.QTabWidget()
tabwidget.addTab(QtWidgets.QPushButton('tab1'), 'tab1')
tabwidget.addTab(QtWidgets.QPushButton('tab2'), 'tab2')
tabwidget.show()
sys.exit(app.exec_())