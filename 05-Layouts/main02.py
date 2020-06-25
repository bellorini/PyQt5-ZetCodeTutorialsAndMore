"""
    Aplicação exemplo para QGridLayout

    Pseudo Calculadora

    Autor original: Jan Bodnar
    website: zetcode.com  
"""

import sys
from PyQt5.QtWidgets import (QWidget, QGridLayout,
                             QPushButton, QApplication)


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        grid = QGridLayout()
        self.setLayout(grid)

        # Vetor Textos dos botões
        names = ['Cls', 'Bck', '', 'Close',
                 '7', '8', '9', '/',
                 '4', '5', '6', '*',
                 '1', '2', '3', '-',
                 '0', '.', '=', '+']

        # vetor Coordenadas dos botões
        positions = [(i, j) for i in range(5) for j in range(4)]

        for position, name in zip(positions, names):

            if name == '':
                continue
            button = QPushButton(name)
            # addWidget(QWidget, posX, posY)
            if name == "Close":
                # múltiplas colunas e linhas
                # addWidget(Widget, Linha Inicial, Coluna Inicial, num Lins, num Cols)
                grid.addWidget(button, position[0], position[1]-1, 1, 2)
            else:
                grid.addWidget(button, position[0], position[1])
            
                

        self.move(300, 150)
        self.setWindowTitle('Calculator')
        self.show()


def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()