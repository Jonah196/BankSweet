import sys

from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtCore import *
from PyQt5.QtGui  import *
from PyQt5.QtWidgets import *
from PyQt5 import QtTest

class MainWindow(QWidget):

	def __init__(self):
		super().__init__()
		
		self.setupUi()
		
	def setupUi(self):

		self.butt = True
		self.labelX = 20
		self.labelY = 40
		self.number = 0
		
		self.setGeometry(0, 0, 400, 400)
		self.setWindowTitle('Basic Window Example')
		self.setWindowIcon(QtGui.QIcon("img.png"))
		
		# Added Sione Manulea Label
		self.labelA = QtWidgets.QLabel(self)
		self.labelA.setText('Sione')
		self.labelA.move(self.labelX, self.labelY-10)
	
		self.label = QtWidgets.QLabel(self)
		pixmap = QPixmap('warrior-ninja.png')
		pixmap = pixmap.scaled(64, 64)
		self.label.setPixmap(pixmap)
		self.label.move(self.labelX, self.labelY)
		
		self.show()
	
	def keyPressEvent(self, e):
		if e.key() == QtCore.Qt.Key_Up:
			self.labelY = self.labelY - 5
			self.label.move(self.labelX, self.labelY)

		if e.key() == QtCore.Qt.Key_Down:
			self.labelY = self.labelY + 5
			self.label.move(self.labelX, self.labelY)

		if e.key() == QtCore.Qt.Key_Left:
			self.labelX = self.labelX - 5
			self.label.move(self.labelX, self.labelY)

		if e.key() == QtCore.Qt.Key_Right:
			self.labelX = self.labelX + 5
			self.label.move(self.labelX, self.labelY)			
		
		if e.key() == QtCore.Qt.Key_Space:
			labelC = QtWidgets.QLabel(self)
			pixmap = QPixmap('img.png')
			pixmap = pixmap.scaled(64, 64)
			labelC.setPixmap(pixmap)
			labelC.move(self.labelX, self.labelY)
		
			self.butt = False
			self.number = self.labelX
			self.starting = 0
			
			while self.butt is False:
				labelC.move(self.number, self.labelY)
				self.number += 5
				self.starting += 1
			
				if self.starting == 100:
					self.butt = True
		
		self.labelA.move(self.labelX, self.labelY-10)

	
if __name__ == "__main__":
    app = QApplication(sys.argv)
	
    MainWindow = MainWindow()
    MainWindow.show()
	
    sys.exit(app.exec_())
