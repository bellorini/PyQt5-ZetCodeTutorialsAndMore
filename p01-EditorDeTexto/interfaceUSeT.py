
from PyQt5.QtWidgets import (QWidget, QMainWindow, QMenu,
                             QPushButton, QTextEdit, QToolTip, QDesktopWidget, QAction)
from PyQt5.QtCore import QFileInfo
from PyQt5.QtGui import QIcon

import sys, os

from Acoes import AcoesUSeT

class JanelaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        # localPath
        self.local_path = QFileInfo(__file__).absolutePath()
        self.os_sep = os.path.sep
        self.icone_path = self.local_path + self.os_sep + 'recursos' + self.os_sep + 'icones' + self.os_sep

        self.acoes = AcoesUSeT(self.icone_path, self.os_sep)

        self.initUI()
    
    def initUI(self):
        self.setWindowIcon(QIcon(self.icone_path + self.os_sep + 'sobre' + self.os_sep + 'iconMaster.png'))
        self.setWindowTitle('USeT: um simples editor de texto! Work in Progress')
        
        centro = QDesktopWidget().availableGeometry().center()
        largura = 800
        altura = 600
        self.setGeometry((centro.x() - int(largura/2)),centro.y() - int(altura/2),largura,altura)

        self.criaMenus()
        self.criaBarraStatus()
        self.show()

    def criaMenus(self):
        # menus Arquivo, Editar e Sobre
        menuArquivo = self.menuBar().addMenu('&Arquivo')
        menuEditar = self.menuBar().addMenu('&Editar')
        menuSobre = self.menuBar().addMenu('&Sobre')

        # subMenus de Arquivo
        menuArquivo.addAction(self.acoes.getAcao('novo'))
        
        menuArquivo.addAction(self.acoes.getAcao('abrir'))
        menuArquivo.addAction(self.acoes.getAcao('salvar'))
        menuArquivo.addSeparator()
        menuArquivo.addAction(self.acoes.getAcao('salvarComo'))
        menuArquivo.addSeparator()
        menuArquivo.addAction(self.acoes.getAcao('sair'))

        # subMenus de Editar
        menuEditar.addAction(self.acoes.getAcao('undo'))
        menuEditar.addAction(self.acoes.getAcao('redo'))
        menuEditar.addSeparator()
        menuEditar.addAction(self.acoes.getAcao('cortar'))
        menuEditar.addAction(self.acoes.getAcao('copiar'))
        menuEditar.addAction(self.acoes.getAcao('colar'))

        # subMenus de Sobre
        menuSobre.addAction(self.acoes.getAcao('sobre'))

        pass

    def criaToolBar(self):
        pass

    def criaBarraStatus(self):
        self.statusBar().showMessage('Pronto')
        pass

    def criaAreaTexto(self):
        pass
