from PyQt6 import (
	QtCore as qc,
	QtWidgets as qw,
	QtGui as qg
)
import sys, typing
from NewRecipesWidget import *
from ViewRecipesWidget import *

class MainWindow(qw.QMainWindow):
	def __init__(self, title):
		super().__init__()
		self.setWindowTitle(title)
		self.resize(350, 600) # <- first argument is x-size, second is y-size
		# self.setGeometry(300, 100, 350, 600) # <- alternative, first arguments set positioning of the window

		# making a central widget
		tabs = qw.QTabWidget()

		tabs.addTab(NewRecipesWidget(), "Add new recipe")
		tabs.addTab(ViewRecipesWidget(), "View recipes")

		self.setCentralWidget(tabs)

	def keyPressEvent(self, a0):
		if a0.key() == 16777216:
			qw.QApplication.exit()
		return super().keyPressEvent(a0)

if __name__ == "__main__":
	app = qw.QApplication(sys.argv)

	window = MainWindow("Cookbook App")
	window.show()

	app.exec()
