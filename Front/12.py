# -*- coding:utf-8 -*-
from PySide2 import QtGui, QtWidgets, QtCore
import sys

text = '''经典台词
1.不管前方的路有多苦，只要走的方向正确，不管多么崎岖不平，都比站在原地更接近幸福。
2.我不知道离别的滋味是这样凄凉，我不知道说声再见要这么坚强。
3.我不知道将去何方，但我已在路上。
4.人永远不知道，谁哪次不经意的跟你说了再见之后，就真的不会再见了。
5.曾经发生过的事情不可能忘记，只不过是想不起而已。
6.我只能送你到这里了，剩下的路你要自己走，不要回头。
7.不管你曾经被伤害得有多深，总会有一个人的出现，让你原谅之前生活对你所有的刁难。
8.已经走到尽头的东西，重生也不过是再一次的消亡。就像所有的开始，其实都只是一个写好了的结局。
9.世界这么大，人生这么长，总会有这么一个人，让你想要温柔地对待。
10.生命可以随心所欲，但不能随波逐流。

'''


class MyWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)

        self.setFixedSize(400, 300)

        self.btn_dialog = QtWidgets.QPushButton(u'弹出对话框')
        self.textLineEdit = QtWidgets.QLineEdit()
        self.textEdit = QtWidgets.QTextEdit()

        self.document = QtGui.QTextDocument(text)

        self.textEdit.setDocument(self.document)

        self.connect(self.btn_dialog, QtCore.SIGNAL('clicked()'), self, QtCore.SLOT('openFileDialog()'))

        self.layout = QtWidgets.QVBoxLayout()
        self.layout.addWidget(self.btn_dialog)
        self.layout.addWidget(self.textLineEdit)
        self.layout.addWidget(self.textEdit)
        self.setLayout(self.layout)

    @QtCore.Slot()
    def openFileDialog(self):
        dialog = QtWidgets.QFileDialog()
        dialog.setFileMode(QtWidgets.QFileDialog.AnyFile)
        dialog.setViewMode(QtWidgets.QFileDialog.Detail)
        if dialog.exec_():
            fileNames = dialog.selectedFiles()
            self.textLineEdit.setText(fileNames[0])


app = QtWidgets.QApplication()
widget = MyWidget()
widget.show()
sys.exit(app.exec_())