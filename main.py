import sys
import random
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QTextEdit, QPushButton


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.set_btn.clicked.connect(self.run)
        self.getStone_btn.clicked.connect(self.getStone)

    def run(self):
        self.stone = self.spinBox.value()
        self.getStone_Edit.setEnabled(True)
        self.getStone_btn.setEnabled(True)
        self.count_Stone.display(self.stone)

    def getStone(self):
        Flag = True
        try:
            self.getStone_value = int(self.getStone_Edit.text())
            if self.getStone_value > 3 or self.getStone_value > self.stone:
                Flag = False
                self.win.setText('Введите число не больше 3')
            else:
                Flag = True

        except Exception:
            self.win.setText('Введите число')

        self.win.setText('')
        if Flag:
            self.stone -= self.getStone_value
            self.display()

    def display(self):
        Game = True
        Flag = True
        self.listWidget.addItem(f'Игрок взял - {self.getStone_value}')
        if self.stone == 0:
            self.win.setText('Игрок выйграл')
            Game = False
        if Game:
            if self.stone < 3:
                self.getStone_value = random.randint(1, self.stone)
                self.stone -= self.getStone_value
                if self.stone == 0:
                    Flag = False
            else:
                self.getStone_value = random.randint(1, 3)
                self.stone -= self.getStone_value
                if self.stone == 0:
                    Flag = False
            self.listWidget.addItem(f'Компьютер взял - {self.getStone_value}')
            self.count_Stone.display(self.stone)

            if self.stone == 0 and Flag:
                self.win.setText('Игрок выйграл')

            elif self.stone == 0 and not Flag:
                self.win.setText('Компьютер выйграл')


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec_())
