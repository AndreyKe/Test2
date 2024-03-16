from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QLabel,
    QLineEdit,
    QVBoxLayout,
    QWidget,
)

from PyQt6.QtWidgets import (
    QMainWindow,
    QApplication,
    QLabel,
    QCheckBox,
    QComboBox,
    # QListBox,
    QLineEdit,
    QLineEdit,
    QSpinBox,
    QDoubleSpinBox,
    QSlider,
)

from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton

from PyQt6.QtCore import Qt

import sys


from model import Model


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        m = Model()
        temp = m.get_secret_key()
        self.setWindowTitle("My App")

        self.label = QLabel(temp)

        self.input = QLineEdit()

        self.button_is_checked = False

        self.setWindowTitle("My App")

        self.button = QPushButton("Ok")
        self.button.setCheckable(True)
        self.button.clicked.connect(self.the_button_was_toggled)
        self.button.setChecked(self.button_is_checked)

        self.setCentralWidget(self.button)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.input)
        layout.addWidget(self.button)
        container = QWidget()
        container.setLayout(layout)

        # Устанавливаем центральный виджет Window.
        self.setCentralWidget(container)

    # def save_input(self):

    def the_button_was_toggled(self, checked):
        self.button_is_checked = checked

        print(self.button_is_checked)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
