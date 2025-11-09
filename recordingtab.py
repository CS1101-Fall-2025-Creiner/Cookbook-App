import sys
from PyQt6.QtCore import Qt as qt
from PyQt6 import QtWidgets as qw
from PyQt6 import QtGui as qg

class RecordingTab(qw.QWidget):
    def __init__(self):
        super().__init__()
        layout = qw.QVBoxLayout()

        name_layout = qw.QHBoxLayout()

        self.name_widget = qw.QWidget()
        self.new_recipe_label = qw.QLabel("New Recipe Name: ")
        self.recipe_name = qw.QLineEdit()
        self.recipe_name.textChanged.connect(self.clear_dialog)
        name_layout.addWidget(self.new_recipe_label)
        name_layout.addWidget(self.recipe_name)
        self.name_widget.setLayout(name_layout)

        self.recipe_box = qw.QTextEdit()
        self.recipe_box.textChanged.connect(self.clear_dialog)
        self.record_button = qw.QPushButton("Save Recipe")
        self.record_button.clicked.connect(self.save_recipe)
        self.dialog_label = qw.QLabel()

        layout.addWidget(self.name_widget)
        layout.addWidget(self.recipe_box)
        layout.addWidget(self.record_button)
        layout.addWidget(self.dialog_label)
        self.setLayout(layout)

    def save_recipe(self):
        if not self.recipe_name.text():
            self.dialog_label.setText("Error: Recipe must have a name!")
            return
        if not self.recipe_box.toPlainText():
            self.dialog_label.setText("Error! Recipe must have something written in it!")
            return
        with open("recipes.txt", "a") as fout:
            print("###Name", file= fout)
            name = self.recipe_name.text()
            print(name, file= fout)
            print("###Recipe", file= fout)
            recipe = self.recipe_box.toPlainText()
            print(recipe, file= fout)
            print("%%%", file= fout)
        self.recipe_box.clear()
        self.recipe_name.clear()
        self.dialog_label.setText("Success! Recipe Saved.")

    def clear_dialog(self):
        self.dialog_label.clear()


