from PyQt5.QtWidgets import QLabel, QMainWindow, QApplication, QWidget, QPushButton, QAction, QLineEdit, QGraphicsColorizeEffect, QMessageBox
from PyQt5.QtGui import QIcon, QColor
from PyQt5.QtCore import pyqtSlot, Qt
from controller.secret_controller import SecretController

class App(QMainWindow):
    def __init__(self, controller: SecretController) -> None:
        super().__init__()

        self.controller = controller

        self.title = 'Secret key validator'
        self.left = 10
        self.top = 10
        self.width = 400
        self.height = 140

        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.initUI()

    def initUI(self) -> None:
        '''Inits main UI forms'''
        self.lable = QLabel(self)
        self.lable_accepted = QLabel(self)

        self.textbox = QLineEdit(self)

        self.ok_button = QPushButton('Ок', self)
        self.cancel_button = QPushButton('Cancel', self)

        self.set_content()
        self.show()

    def set_content(self) -> None:
        '''Sets size and content for main UI forms'''
        self.lable.move(100, 20)
        self.lable.setText(self.controller.show_key_fragment())

        self.lable_accepted.move(250, 20)

        self.textbox.setMaxLength(2)
        self.textbox.move(180, 20)
        self.textbox.resize(30,25)

        self.ok_button.move(100, 80)
        self.ok_button.resize(40, 35)
        self.ok_button.clicked.connect(self.on_ok_click)

        self.cancel_button.move(150, 80)
        self.cancel_button.resize(80, 35)
        self.cancel_button.clicked.connect(self.on_cancel_click)

    @pyqtSlot()
    def on_ok_click(self):
        '''Sets onClick actions for ok button'''
        textboxValue = self.textbox.text()

        input_correct = self.controller.validate_intput(input=textboxValue)
        self.color_effect = QGraphicsColorizeEffect()

        if input_correct:
            self.color_effect.setColor(Qt.GlobalColor.green)
            self.lable_accepted.setText("Correct!")
            self.lable_accepted.setGraphicsEffect(self.color_effect)
        else:
            self.color_effect.setColor(Qt.GlobalColor.red)
            self.lable_accepted.setText("Error!")
            self.lable_accepted.setGraphicsEffect(self.color_effect)

    @pyqtSlot()
    def on_cancel_click(self):
        '''Sets onClick actions for cancel button'''
        self.textbox.setText("")
        self.lable_accepted.setText("")
