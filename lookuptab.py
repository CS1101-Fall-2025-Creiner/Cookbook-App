import sys
import PyQt6.QtCore as qc
from PyQt6.QtCore import Qt as qt
from PyQt6 import QtWidgets as qw
from PyQt6 import QtGui as qg

# class RecipeSelection(qw.QListWidget):
#     def __init__(self, parent, recipes_dict):
#         super().__init__(parent)
#         if recipes_dict: 
#             self.addItems(recipes_dict.keys())

        # ????
        # self.setEditTriggers(
        #     qw.QAbstractItemView.EditTrigger.SelectedClicked |
        #     qw.QAbstractItemView.EditTrigger.EditKeyPressed
        # )
        # for name in recipes_dict:
        #     item = qw.QListWidgetItem(name)
        #     item.setFlags(item.flags() | qt.ItemFlag.ItemIsEditable)
        #     self.addItem(item)

class LookupTab(qw.QWidget):
    def __init__(self):
        super().__init__()
        layout = qw.QVBoxLayout()
        self.recipes_dict = self.get_recipes()
        # self.recipes_selection = RecipeSelection(self, self.recipes_dict)
        self.recipes_selection = qw.QListWidget()
        if self.recipes_dict: 
            self.recipes_selection.addItems(self.recipes_dict.keys())

        self.label = qw.QLabel("Your Recipes")
        self.recipe_display = qw.QTextBrowser()
        self.recipe_display.setAlignment(qt.AlignmentFlag.AlignLeft)
        if self.recipes_dict: 
            self.recipe_display.setText(self.recipes_dict[list(enumerate(self.recipes_dict.keys()))[0][1]])

        self.bottom_options = qw.QWidget()
        bottom_layout = qw.QHBoxLayout()

        self.refresh_button = qw.QPushButton("Refresh Recipes (F5)")
        self.refresh_button.clicked.connect(self.refresh_recipes)
        self.delete_button = qw.QPushButton("Delete Selected Recipe (Del)")
        # self.delete_button.clicked.connect(self.delete_recipe)

        bottom_layout.addWidget(self.refresh_button)
        bottom_layout.addWidget(self.delete_button)
        self.bottom_options.setLayout(bottom_layout)

        layout.addWidget(self.label)
        layout.addWidget(self.recipes_selection)
        layout.addWidget(self.recipe_display, stretch=2)
        layout.addWidget(self.bottom_options)

        self.recipes_selection.currentTextChanged.connect(self.display_recipe)
        # self.recipes_selection.setContextMenuPolicy(qt.ContextMenuPolicy.CustomContextMenu)
        # self.recipes_selection.customContextMenuRequested.connect(self.recipes_context_menu)
        # self.recipes_selection.itemChanged.connect(self.rename_recipe)

        self.setLayout(layout)

    def display_recipe(self, recipe):
        if not recipe: return # happens when the refresh button is pressed, cleared recipes cause the currentTextChanged signal to be emitted
        self.recipe_display.setMarkdown(self.recipes_dict[recipe])
    
    def get_recipes(self) -> dict:
        with open("recipes.txt", "r") as fin:
            recipes_dict = {}
            test = fin.readlines()
            if len(test) == 0: return recipes_dict
            n = len(test)
            fin.seek(0,0)
            fin.readline()
            name = fin.readline().strip()
            while name != "":
                recipe = ""
                fin.readline() # skip ###Recipe
                next_line = fin.readline()
                while next_line != "%%%\n":
                    recipe += next_line
                    next_line = fin.readline()
                recipes_dict[name] = recipe
                fin.readline()
                name = fin.readline().strip()
            return recipes_dict

    def refresh_recipes(self):
        self.recipes_dict = self.get_recipes()
        print(f"New recipes dict: {self.recipes_dict}")
        self.recipes_selection.clear()
        self.recipes_selection.addItems(self.recipes_dict)

    # def delete_recipe(self):
    #     name = self.recipes_selection.currentItem().text()
    #     with open("recipes.txt", "w") as fout:
            # while recipes
 
    def recipes_context_menu(self, pos):
        item = self.recipes_selection.itemAt(pos)
        if not item: return
        menu = qw.QMenu(self)
        rename_option = menu.addAction("Rename")
        action = menu.exec(self.recipes_selection.mapToGlobal(pos))
        if action is rename_option:
            index = self.recipes_selection.indexFromItem(item)
            self.recipes_selection.edit(index)

    def rename_recipe(self, test):
        print(test)
