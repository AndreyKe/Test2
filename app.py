import sys
from PyQt5.QtWidgets import QLabel, QMainWindow, QApplication, QWidget, QPushButton, QAction, QLineEdit, QGraphicsColorizeEffect, QMessageBox
from PyQt5.QtGui import QIcon, QColor
from PyQt5.QtCore import pyqtSlot, Qt
from controller.secret_controller import SecretController
from model.secret_model import SecretModel
from view.main_window import App


if __name__ == '__main__':
    app = QApplication(sys.argv)

    model = SecretModel()
    controller = SecretController(model=model)

    ex = App(controller=controller)
    sys.exit(app.exec_())
