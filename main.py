from PyQt6 import (
	QtCore as qc,
	QtWidgets as qw,
	QtGui as qg
)
import sys, typing
from NewRecipesWidget import *
from ViewRecipesWidget import *
import yaml

class MainWindow(qw.QMainWindow):
	def __init__(self, title, recipes_dict):
		super().__init__()

		self.recipes = self.get_recipes(recipes_dict)
		print(self.recipes)

		self.setWindowTitle(title)
		self.resize(350, 600) # <- first argument is x-size, second is y-size
		# self.setGeometry(300, 100, 350, 600) # <- alternative, first arguments set positioning of the window

		# making a central widget
		tabs = qw.QTabWidget()

		record_widget = NewRecipesWidget(self.recipes)
		record_widget.emit_new_recipe.connect(self.add_recipe)
		tabs.addTab(record_widget, "Add new recipe")
		tabs.addTab(ViewRecipesWidget(self.recipes), "View recipes")

		self.setCentralWidget(tabs)

	def keyPressEvent(self, a0):
		if a0.key() == 16777216:
			qw.QApplication.exit()
		return super().keyPressEvent(a0)

	def get_recipes(self, recipes_dict):
		# this returns a dictionary of existing recipes
		recipes = {}
		for yaml_name in recipes_dict:
			name = recipes_dict[yaml_name]["name"]
			desc = recipes_dict[yaml_name]["desc"]

			recipes[name] = desc

		return recipes

	def add_recipe(self, name, desc):
		
		# update the dictionary
		self.recipes[name] = desc
#		try:
		with open("recipes_list.yml", "w") as f:
			yaml.safe_dump(self.recipes, f)



if __name__ == "__main__":
	app = qw.QApplication(sys.argv)

	# need to load an existing recipes file and pass it to the window object
	# or create one if first time user
	try:
		with open("recipes_list.yaml", "r") as f:
			recipes_dict = yaml.safe_load(f)
	except OSError:
		with open("recipes_list.yaml", "w") as f:
			recipes_dict = {}
			pass


	window = MainWindow("Cookbook App", recipes_dict)
	window.show()

	app.exec()
