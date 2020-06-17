"""
    Apresenta uma janela de aplicação em tela

    Autor original: Jan Bodnar
    website: zetcode.com    
"""

from PyQt5.QtWidgets import QApplication, QWidget

import sys

def main():

    # QApplication é o objeto principal de uma aplicação PyQt
    # TODA aplicação deve conter um único objeto QApplication
    app = QApplication(sys.argv)
    # sys.argv são parâmetros que podem ser passado para esta aplicação via linha de comando
    # caso não deseja-se ter esta feature, usar lista vazia 
    #   app = QApplication([]])

    # QWidget é a classe base para todos os objetos de interface PyQt
    window = QWidget()

    # Algumas configurações da instância 'window'
    window.resize(500,300) # largura, altura da aplicação
    window.move(200,400) # x0,y0 -> canto esquerdo superior
    window.setWindowTitle("Simple:  aplicação simples do tutorial ZetCode")

    # por padrão, os Widgets são criados em memória apenas
    # .show() indica para exibí-los
    window.show()

    # app.exec_() ativa o 'loop' principal da aplicação
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
