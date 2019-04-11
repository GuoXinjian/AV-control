from PySide2 import QtGui, QtWidgets, QtCore
import sys


app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setFixedSize(400, 300)

# 生成一个view
listview = QtWidgets.QListView(window)
# 生成一个model
model = QtCore.QStringListModel()

# model添加数据
model.setStringList(['1', '2', '3', '4', '5'])

# view设置model
listview.setModel(model)

layout = QtWidgets.QVBoxLayout(window)
layout.addWidget(listview)

window.setLayout(layout)
window.show()
sys.exit(app.exec_())
