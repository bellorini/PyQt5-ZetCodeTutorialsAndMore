"""
    Apresenta uma janela de aplicação em tela com
    - Barra de Status
    - Barra de Menus com submenus
    - Menu de contexto
    - toolbar

    A Janela é centralizada

    Autor original: Jan Bodnar
    website: zetcode.com    
"""

from PyQt5.QtWidgets import (QApplication, QWidget, QMainWindow, QMenu,
                             QPushButton, QToolTip, QDesktopWidget, QAction)
from PyQt5.QtCore import QFileInfo
from PyQt5.QtGui import QIcon


import sys

class JanelaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        # ponto central da tela disponível
        centro = QDesktopWidget().availableGeometry().center()
        # setGeometry == move + resize
        #                 x0, y0, xf, yf
        largura = 800
        altura = 600
        self.setGeometry((centro.x() - int(largura/2)),centro.y() - int(altura/2),largura,altura)
        self.setWindowTitle('Exemplo para Barra de Status, Barra de Menus e centralização')

        # barra de status
        # busca a Barra de Status de Objeto QMainWindow e mostra mensagem
        self.statusBar().showMessage('Barra de Status: pronta!')

        # barra de menus
        # cria menu 'Arquivo'
        #              QMainWindow contém MenuBar e é adicionado 'Arquivo' com hotkey (&)
        menuArquivo = self.menuBar().addMenu('&Arquivo')
        # cria-se uma action, que é a ação de um item de menu
        sairAction = QAction('Sair', self)
        sairAction.setShortcut('Ctrl+Q')
        sairAction.setStatusTip('Sair da Aplicação')
        sairAction.triggered.connect(self.encerraApp)
        menuArquivo.addAction(sairAction)

        menuVisao = self.menuBar().addMenu('&Visualização')
        # Action para Ocultar ou Mostrar Barra de Status
        ocultarMostrarAction = QAction('Mostrar Barra de Status', self, checkable=True)
        ocultarMostrarAction.setStatusTip('Oculta Barra de Status')
        ocultarMostrarAction.setChecked(True)
        ocultarMostrarAction.triggered.connect(self.hideShowStatusBarr)
        menuVisao.addAction(ocultarMostrarAction)

        # Menu Janela
        menuJanela = self.menuBar().addMenu('&Janela')
        # Submenu Janela -> Opções
        submenuJanelaOpcoes = QMenu('Opções', self)
        menuJanela.addMenu(submenuJanelaOpcoes)
        # Ações do submenuJanela
        maximizarAction = QAction('Maximizar', self)
        maximizarAction.triggered.connect(self.maximizarJanela)
        minimizarAction = QAction('Minimizar', self)
        minimizarAction.triggered.connect(self.minimizarJanela)
        restaurarAction = QAction('Restaurar', self)
        restaurarAction.triggered.connect(self.restaurarJanela)
        # adição no submenu menuJanela
        submenuJanelaOpcoes.addActions([maximizarAction, minimizarAction,restaurarAction])

        # chamada ao método para criar uma Barra de Ferramentas
        # tentativa de organizar melhor o código
        self.criaToolBar()

        self.show()
        pass

    # Action com 'checkable' envia estado como segundo parâmetro
    def hideShowStatusBarr(self, estado):
        if estado:
            self.statusBar().show()
            self.statusBar().showMessage('Barra de Status: pronta!')
        else:
            self.statusBar().hide()


    def maximizarJanela(self):
        self.showMaximized()
    
    def minimizarJanela(self):
        self.showMinimized()

    def restaurarJanela(self):
        self.showNormal()

    def encerraApp(self):
        QApplication.instance().quit()

    # Menu de Contexto
    # Reimplementar método contextMenuEvent
    def contextMenuEvent(self, event):
        menuContexto = QMenu(self)
        novoAction = menuContexto.addAction('Novo')
        abrirAction = menuContexto.addAction('Abrir')
        sairAction = menuContexto.addAction('Sair')

        # para executar o menu, usa-se .exec_(QPoint)
        # .mapToGlobal traduz QPoint local para Global em tela
        # event.pos() captura o local do evento com retorno QPoint
        action = menuContexto.exec_(self.mapToGlobal(event.pos()))

        # possível problema: menu é mostrado em qq local do App (excessão: Barra de título)

        if action == sairAction:
            self.encerraApp()

    def criaToolBar(self):
        # cria uma ação, possivelmente, pode ser uma genérica para 
        # - contextmenu, menus, toolbar (Verificar)
        iconSair = QIcon(QFileInfo(__file__).absolutePath() + '/recursos/iconSair.png')
        toolSairAction = QAction(iconSair, 'Sair', self)
        toolSairAction.triggered.connect(self.encerraApp)

        # simples como barra de menus
        # cria-se uma toolbar e posteriormente, adiciona-se a ação
        self.toolbar = self.addToolBar('Barra de Ferramentas')
        self.toolbar.addAction(toolSairAction)


def main():
    app = QApplication(sys.argv)
    janela = JanelaPrincipal()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()