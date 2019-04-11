from PySide2 import QtGui, QtWidgets, QtCore
import sys


app = QtWidgets.QApplication()
image = QtGui.QPixmap('/Users/wzh/Downloads/IMG_0197.jpg') #生成一个QPixmap对象，QPixmap类是对图像显示经过了专门的优化和设计的类
painter = QtGui.QPainter()
painter.begin(image)
rectangle = QtCore.QRect(50, 50, 200, 200)
painter.drawRect(rectangle)
painter.end()
label = QtWidgets.QLabel()
label.setGeometry(50, 50, 1024, 1024) # 设置标签起始位置和大小
label.setPixmap(image) # 用来设置图像
label.show()
sys.exit(app.exec_())