import sys
from PyQt6.QtCore import Qt as qt
from PyQt6 import QtWidgets as qw
from PyQt6 import QtGui as qg
from lookuptab import LookupTab
from recordingtab import RecordingTab

class MainWindow(qw.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Cookbook App")

        tabs = qw.QTabWidget()

        tabs.addTab(RecordingTab(), "New Recipe")
        tabs.addTab(LookupTab(), "Your Recipes")

        self.setCentralWidget(tabs)

    def keyPressEvent(self, a0: qg.QKeyEvent | None): 
        if a0:
            if a0.key() == 16777216:
                sys.exit()

app = qw.QApplication([])

try:
    with open("recipes.txt", "r") as fin:
        pass
except FileNotFoundError:
    with open("recipes.txt", "w") as fin:
        pass
try:
    with open("deleted_recipes.txt", "r") as fin:
        pass
except FileNotFoundError:
    with open("deleted_recipes.txt", "w") as fin:
        pass

window = MainWindow()
window.show()

app.exec()

