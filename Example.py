from PyQt5.QtWidgets import QWidget, QPushButton, QLabel
from PyQt5 import QtCore


class EndGameScreen(QWidget):
    def __init__(self):
        super().__init__()

        self.youAreDeadLabel = QLabel(f'Вы умерли.', self)

        self.initUI()

    def initUI(self):
        self.setGeometry(425, 125, 300, 500)
        self.setWindowTitle('Конец игры')

        self.youAreDeadLabel.move(10, 242)
        self.youAreDeadLabel.resize(280, 16)
        self.youAreDeadLabel.setAlignment(QtCore.Qt.AlignCenter)
