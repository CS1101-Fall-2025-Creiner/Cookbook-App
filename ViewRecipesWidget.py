from PyQt6 import (
	QtCore as qc,
	QtWidgets as qw,
	QtGui as qg
)

class ViewRecipesWidget(qw.QWidget):
	def __init__(self, recipes):
		super().__init__()

		outer_layout = qw.QVBoxLayout(self)
		self.recipes = recipes

		self.recipes_list = qw.QListWidget()
		self.recipes_list.addItems(self.recipes.keys()) # populates the list
		self.recipes_list.currentTextChanged.connect(self.get_desc)

		outer_layout.addWidget(self.recipes_list)

		self.recipes_display = qw.QTextBrowser()
		outer_layout.addWidget(self.recipes_display)

		button_layout = qw.QHBoxLayout()
		self.refresh_button = qw.QPushButton("Refresh List")
		self.delete_button = qw.QPushButton("Delete Recipe")
		self.surprise_button = qw.QPushButton("Surprise Me")
		button_layout.addWidget(self.refresh_button)
		button_layout.addWidget(self.delete_button)
		button_layout.addWidget(self.surprise_button)

		outer_layout.addLayout(button_layout)

	def get_desc(self, name):
		self.recipes_display.setText(self.recipes[name])