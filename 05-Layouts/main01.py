"""
    Aplicação exemplo para QHBoxLayout e VBoxLayout

    Simulação de Caixa de Diálogo com "OK' e "Cancel"

    Autor original: Jan Bodnar
    website: zetcode.com  
"""


import sys
from PyQt5.QtWidgets import (QWidget, QPushButton,
                             QHBoxLayout, QVBoxLayout, QApplication)


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        okButton = QPushButton("OK")
        cancelButton = QPushButton("Cancel")

        # define um HBoxLayout
        hbox = QHBoxLayout()
        # adiciona um espaço que "empurra" (neste caso: esquerda) os próximos Widgets adicionado 
        #   para o fim do HBoxLayout
        hbox.addStretch(1)
        hbox.addWidget(okButton)
        hbox.addWidget(cancelButton)

        vbox = QVBoxLayout()
        # adiciona um espaço que "empurra" (neste caso: para baixo) o Widget adicionado
        vbox.addStretch(1)
        vbox.addLayout(hbox)

        self.setLayout(vbox)

        self.setGeometry(300, 300, 300, 150)
        self.setWindowTitle('Buttons')
        self.show()


def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()