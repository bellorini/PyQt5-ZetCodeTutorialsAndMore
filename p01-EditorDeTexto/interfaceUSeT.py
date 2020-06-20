
from PyQt5.QtWidgets import (QWidget, QMainWindow, QMenu, QMessageBox, QDesktopWidget,
                             QLabel, QPushButton, QTextEdit, QToolTip, QAction )
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

        self.acoes = AcoesUSeT(self.icone_path, self.os_sep, self)
        self.subWSobre = JanelaSobre(self.icone_path, self.os_sep, self)

        self.criaMenus()
        self.criaToolBar()
        self.criaBarraStatus()

        self.initUI()
    
    def initUI(self):
        self.setWindowIcon(QIcon(self.icone_path + self.os_sep + 'sobre' + self.os_sep + 'iconMaster.png'))
        self.setWindowTitle('USeT: um simples editor de texto! Work in Progress')
        
        centro = QDesktopWidget().availableGeometry().center()
        largura = 800
        altura = 600
        self.setGeometry((centro.x() - int(largura/2)),centro.y() - int(altura/2),largura,altura)

        self.areaTexto = QTextEdit()
        self.setCentralWidget(self.areaTexto)

        self.show()

    def criaMenus(self):
        # menus Arquivo, Editar e Sobre
        self.menuArquivo = self.menuBar().addMenu('&Arquivo')
        self.menuEditar = self.menuBar().addMenu('&Editar')
        self.menuVisualizar = self.menuBar().addMenu('&Visualizar')
        self.menuSobre = self.menuBar().addMenu('&Sobre')

        # subMenus de Arquivo
        self.menuArquivo.addAction(self.acoes.getAcao('novo'))
        
        self.menuArquivo.addAction(self.acoes.getAcao('abrir'))
        self.menuArquivo.addAction(self.acoes.getAcao('salvar'))
        self.menuArquivo.addSeparator()
        self.menuArquivo.addAction(self.acoes.getAcao('salvarComo'))
        self.menuArquivo.addSeparator()
        self.menuArquivo.addAction(self.acoes.getAcao('sair'))

        # subMenus de Editar
        self.menuEditar.addAction(self.acoes.getAcao('undo'))
        self.menuEditar.addAction(self.acoes.getAcao('redo'))
        self.menuEditar.addSeparator()
        self.menuEditar.addAction(self.acoes.getAcao('cortar'))
        self.menuEditar.addAction(self.acoes.getAcao('copiar'))
        self.menuEditar.addAction(self.acoes.getAcao('colar'))

        # subMenus de Visualizar
        self.menuVisualizar.addAction(self.acoes.getAcao('verToolBar'))
        

        # subMenus de Sobre
        self.menuSobre.addAction(self.acoes.getAcao('sobre'))

        pass

    def criaToolBar(self):
        self.toolBar = self.addToolBar('Barra de Ferramentas Padrão')
        self.toolBar.addAction(self.acoes.getAcao('novo'))
        self.toolBar.addAction(self.acoes.getAcao('abrir'))
        self.toolBar.addAction(self.acoes.getAcao('salvar'))
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.acoes.getAcao('undo'))
        self.toolBar.addAction(self.acoes.getAcao('redo'))
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.acoes.getAcao('cortar'))
        self.toolBar.addAction(self.acoes.getAcao('copiar'))
        self.toolBar.addAction(self.acoes.getAcao('colar'))

        
       # self.toolBar.setVisible
        pass

    def criaBarraStatus(self):
        self.statusBar().showMessage('Pronto')
        pass

    def criaAreaTexto(self):
        pass
    

    pass # JanelaPrincipal


class JanelaSobre(QWidget):
    def __init__(self,icone_path, os_sep, pai):
        super().__init__()

        self.icone_path = icone_path
        self.os_sep = os_sep
        self.pai = pai
        
        

        self.initUI()
    
    def initUI(self):

        self.setWindowIcon(QIcon(self.icone_path + self.os_sep + 'sobre' + self.os_sep + 'iconMaster.png'))
        self.setWindowTitle('Sobre')

        lb = QLabel()
        lb.setText('TODO')
        lb.setParent(self)
        lb.setMargin(10)
        

        pass


    pass # JanelaSobre
