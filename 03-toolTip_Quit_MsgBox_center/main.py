"""
    Apresenta uma janela de aplicação em tela com
    - ícone
    - botão
    - texto de ajuda para o botão

    O Botão encerra a aplicação

    A Janela é centralizada

    Autor original: Jan Bodnar
    website: zetcode.com    
"""

from PyQt5.QtWidgets import (QApplication, QWidget, 
                             QPushButton, QToolTip,
                            QMessageBox, QDesktopWidget)
from PyQt5.QtGui import QFont
import sys

class JanelaPrincipal(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        # ponto central da tela disponível
        centro = QDesktopWidget().availableGeometry().center()
        # setGeometry == move + resize
        #                 x0, y0, xf, yf
        largura = 500
        altura = 200
        self.setGeometry((centro.x() - largura/2),centro.y() - altura/2,largura,altura)
        self.setWindowTitle('Exemplo para Tooltip, signal+slot, MsgBox e centralização')
        
        # QPushButton('texto', parent(Widget))
        botao = QPushButton('click-me to close!',self)
        # .resize()
        # - configura o tamanho do botão
        # .sizeHint()
        # - retorna o que seria o tamanho recomendado para o botão
        botao.resize(botao.sizeHint())

        # Configura tooltip para botão
        QToolTip.setFont(QFont('SansSerif',10))
        botao.setToolTip('Este é um <b>QPushButton</b> que encerrará a aplicação!')

        # conecta o sinal 'clicked' com o slot 'fecharApp'
        botao.clicked.connect(self.fecharApp)

        self.show()

    def fecharApp(self):
        # QMessageBox.question
        # p1 -> parent
        # p2 -> título
        # p3 -> texto da mensagem
        # p4 -> botões de opções
        # p5 -> botão em foco ??
        resp = QMessageBox.question(self, 'Encerrar', 'Deseja encerrar a aplicação?', 
                                     QMessageBox.Yes|QMessageBox.No, QMessageBox.No)

        if resp == QMessageBox.Yes:
            QApplication.instance().quit()


    
def main():
    app = QApplication(sys.argv)
    janela = JanelaPrincipal()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()