import sys
from PyQt5 import QtWidgets
from PyQt5 import QtGui

def basicWindow():
    app = QtWidgets.QApplication(sys.argv)
    windowExample = QtWidgets.QWidget()
    windowExample.setGeometry(0, 0, 400, 400)
    windowExample.setWindowTitle('Basic Window Example')
    windowExample.setWindowIcon(QtGui.QIcon("img.png"))
    windowExample.show()
    sys.exit(app.exec_())

basicWindow()
