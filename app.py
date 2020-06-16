import sys
from PyQt5 import QtGui, Qt
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QGridLayout, QPushButton, \
    QLineEdit, QSizePolicy


class App(QMainWindow):
    operators = ['+', '-', 'x', '÷', 'x²']
    actions = ['C', '<-', '=']

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle('Calculadora')
        self.setFixedSize(400, 400)
        self.cw = QWidget()
        self.grid = QGridLayout(self.cw)

        # Display configuration
        self.display = QLineEdit()
        self.grid.addWidget(self.display, 0, 0, 1, 5)
        self.display.setDisabled(True)
        self.display.setStyleSheet(
            '*{background: #FFF; color: #000; font-size: 30px; font-family: Arial, Helvetica, sans-serif; border-radius: 10px; padding: 10px}'
        )
        self.display.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)

        # Buttons definition
        self.add_button(QPushButton('7'), 1, 0, 1, 1)
        self.add_button(QPushButton('8'), 1, 1, 1, 1)
        self.add_button(QPushButton('9'), 1, 2, 1, 1)
        self.add_button(QPushButton('÷'), 1, 3, 1, 1)
        self.add_button(QPushButton('C'), 1, 4, 1, 1, self.clear_display)

        self.add_button(QPushButton('4'), 2, 0, 1, 1)
        self.add_button(QPushButton('5'), 2, 1, 1, 1)
        self.add_button(QPushButton('6'), 2, 2, 1, 1)
        self.add_button(QPushButton('x'), 2, 3, 1, 1)
        self.add_button(QPushButton('<-'), 2, 4, 1, 1, self.delete_last)

        self.add_button(QPushButton('1'), 3, 0, 1, 1)
        self.add_button(QPushButton('2'), 3, 1, 1, 1)
        self.add_button(QPushButton('3'), 3, 2, 1, 1)
        self.add_button(QPushButton('-'), 3, 3, 1, 1)
        self.add_button(QPushButton('='), 3, 4, 2, 1, self.equals)

        self.add_button(QPushButton('.'), 4, 0, 1, 1)
        self.add_button(QPushButton('0'), 4, 1, 1, 1)
        self.add_button(QPushButton('x²'), 4, 2, 1, 1, self.exponential)
        self.add_button(QPushButton('+'), 4, 3, 1, 1)

        # Centralizing elements
        self.setCentralWidget(self.cw)

    def add_button(self, button, row, col, rowspan, colspan, function=None):
        self.grid.addWidget(button, row, col, rowspan, colspan)

        if function:
            button.clicked.connect(function)
        else:
            button.clicked.connect(
                lambda: self.display.setText(
                    self.display.text() + button.text())
            )

        if button.text() in self.operators:
            button.setStyleSheet(
                'border: 2px solid black; border-radius: 5px; background: #3881b8; color: #FFF;')
        elif button.text() in self.actions:
            button.setStyleSheet(
                'border: 2px solid black; border-radius: 5px; background: #c05e31; color: #FFF')
        else:
            button.setStyleSheet(
                'border: 2px solid black; border-radius: 5px; background: #212C3D; color: #FFF')

        button.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)

    def exponential(self):
        self.display.setText(self.display.text() + '**')

    def clear_display(self):
        self.display.setText('')

    def delete_last(self):
        self.display.setText(self.display.text()[:-1])

    def equals(self):
        try:
            conta = self.display.text()
            if 'x' in conta:
                conta = conta.replace('x', '*')
            if '÷' in conta:
                conta = conta.replace('÷', '/')
            self.display.setText(str(eval(conta)))
        except Exception as e:
            self.display.setText('Conta inválida.')


if __name__ == "__main__":
    qt = QApplication(sys.argv)
    app = App()
    app.setWindowIcon(QtGui.QIcon('/assets/icon.png'))
    app.setStyleSheet('background-color: #CECECE;')
    app.show()
    qt.exec_()
