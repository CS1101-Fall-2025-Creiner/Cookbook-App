from PyQt6 import (
	QtCore as qc,
	QtWidgets as qw,
	QtGui as qg
)

class NewRecipesWidget(qw.QWidget):
	emit_new_recipe = qc.pyqtSignal(str, str)

	def __init__(self, recipes):
		super().__init__()

		main_layout = qw.QVBoxLayout(self)
		self.recipes = recipes

		# create title widget
		title_widget = qw.QWidget()
		title_layout = qw.QHBoxLayout(title_widget)

		title_label = qw.QLabel("Name of Recipe: ")
		self.title_entry = qw.QLineEdit() # needs to be a property so we can grab text later

		title_layout.addWidget(title_label)
		title_layout.addWidget(self.title_entry)

		main_layout.addWidget(title_widget)

		self.recipe_box = qw.QTextEdit()
		main_layout.addWidget(self.recipe_box)

		save_button = qw.QPushButton("Save Recipe")
		save_button.clicked.connect(self.record_recipe)
		main_layout.addWidget(save_button)

	def record_recipe(self):
		name = self.title_entry.text()
		desc = self.recipe_box.toPlainText()

		self.emit_new_recipe.emit(name, desc)		
