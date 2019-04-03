# -*- coding:utf-8 -*-


import sys
from PySide2 import QtCore,QtGui,QtWidgets

app = QtWidgets.QApplication(sys.argv)

quit = QtWidgets.QPushButton('quit')
quit.resize(75,30)
quit.setFont(QtGui.QFont('Times',18,QtGui.QFont.Bold))

QtCore.QObject.connect(quit,QtCore.SIGNAL('clicked()'),app,QtCore.SLOT('quit()'))

quit.show()
sys.exit(app.exec_())