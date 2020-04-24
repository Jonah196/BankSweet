import sys
from PyQt5 import QtWidgets
from PyQt5 import QtGui

def basicWindow():
    app = QtWidgets.QApplication(sys.argv)
    windowExample = QtWidgets.QWidget()
    windowExample.setGeometry(0, 0, 400, 400)
    windowExample.setWindowTitle('Basic Window Example')
    windowExample.setWindowIcon(QtGui.QIcon("img.png"))
	
    # Added Sione Manulea Label
    labelA = QtWidgets.QLabel(windowExample)
    labelA.setText('Sione Manulea was here! :)')
    labelA.move(100, 40)
	
    labelB = QtWidgets.QLabel(windowExample)
    labelB.setText('Hello. Just testing.')
    labelB.move(200,80)
	
    windowExample.show()
    sys.exit(app.exec_())
	
basicWindow()