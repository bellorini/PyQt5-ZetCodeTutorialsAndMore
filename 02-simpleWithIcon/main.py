"""
    Apresenta uma janela de aplicação em tela com ícone

    Autor original: Jan Bodnar
    website: zetcode.com    
"""

from PyQt5.QtWidgets import QApplication, QWidget
# para configuração do ícone
from PyQt5.QtCore import QFileInfo
from PyQt5.QtGui import QIcon

import sys

# Classe que herda de QWidgets
class JanelaPrincipal(QWidget):
    # construtor 
    def __init__(self):
        # construtor da classe pai
        super().__init__()

        self.initUI()

    # método para construir a interface da JanelaPrincipal
    def initUI(self):
        # setGeometry == move + resize
        #                 x0, y0, xf, yf
        self.setGeometry(300,300,500,200)
        self.setWindowTitle('Simple: uma simples aplicação com ícone')
        # necessário usar o endereço absoluto do ícone
        # alternativamente:
        #   enderecoAbsoluto = QFileInfo(__file__).absolutePath()
        #   icon = QIcon(enderecoAbsoluto + '/recursos/icon.png')
        #   self.setWindowIcon(icon)
        self.setWindowIcon(QIcon(QFileInfo(__file__).absolutePath() + '/recursos/icon.png'))
        self.show()


def main():
    # Objeto principal da aplicação PyQt5
    app = QApplication(sys.argv)
    # instância da JanelaPrincipal que será controlada por QApplication()
    janelaPrincipal = JanelaPrincipal()
    # execução do loop principal
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
