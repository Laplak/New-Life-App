import sys

from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWidgets import QLabel, QPushButton
from PyQt5.QtWidgets import QInputDialog
from PyQt5 import QtCore
import GlobalVariables

from TheGame import TheGame


class StartScreen(QMainWindow):
    def __init__(self):
        super().__init__()

        self.startGame = QPushButton(self)
        self.usernameLabel = QLabel(self)
        self.recordLabel = QLabel(self)
        self.gameRulesLabel = QLabel(self)

        self.lastName = GlobalVariables.lastName
        self.lastAge = GlobalVariables.lastAge
        self.lastMoney = GlobalVariables.lastMoney

        self.initUI()

    def initUI(self):
        self.setGeometry(425, 125, 300, 500)
        self.setWindowTitle('Начало игры')

        with open('TheGameRules.txt', mode='r', encoding='utf8') as f:
            gameRules = f.read()

        self.startGame.move(90, 345)
        self.startGame.setText("Начать игру")
        self.startGame.clicked.connect(self.writeUsernameFunction)
        self.startGame.resize(120, 40)

        self.usernameLabel.move(5, -210)
        self.usernameLabel.resize(450, 450)
        self.usernameLabel.setText('')

        self.gameRulesLabel.move(2, 13)
        self.gameRulesLabel.resize(300, 300)
        self.gameRulesLabel.setText(gameRules)
        self.gameRulesLabel.setAlignment(QtCore.Qt.AlignCenter)

        self.recordLabel.move(2, 274)
        self.recordLabel.resize(300, 50)
        self.recordLabel.setText(f'  Также мы предлагаем вам побить\n рекорд прошлых игроков: \n'
                    f'{self.lastName},  {self.lastAge},  {self.lastMoney}$.')
        self.recordLabel.setAlignment(QtCore.Qt.AlignCenter)

    def writeUsernameFunction(self):
        try:
            self.usernameLabel.setText('Имя персонажа')
            username, ok_pressed = QInputDialog.getText(self, "Введите имя",
                                                        "Введите имя персонажа")
            if ok_pressed:
                self.startGame.hide()

                if len(username) > 11:
                    raise ValueError
                elif username != username.capitalize() or not username.isalpha():
                    raise TypeError
                else:
                    self.hide()
                    self.game = TheGame(username)
                    self.game.show()

        except ValueError:
            self.usernameLabel.setText('Имя персонажа слишком длинное!')
            self.startGame.show()
        except TypeError:
            self.usernameLabel.setText('Введите корректное имя!')
            self.startGame.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = StartScreen()
    widget.show()
    sys.exit(app.exec_())
