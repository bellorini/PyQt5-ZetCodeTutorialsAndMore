
from PyQt5.QtWidgets import QApplication, QAction, QMessageBox
from PyQt5.QtGui import QIcon

class AcoesUSeT():
    def __init__(self,icone_path, os_sep):
        # dicionário de ações
        self.acoes = dict()
        self.icone_path = icone_path
        self.os_sep = os_sep
        self.criaAcoes()
        self.conectaAcoes()
    
    def criaAcoes(self):
        
        iconPath = self.icone_path + self.os_sep + 'arquivo' + self.os_sep
        self.acoes['novo'] = QAction(QIcon(iconPath + 'novo.png'),'Novo')
        self.acoes['novo'].setShortcut('Ctrl+N')
        self.acoes['abrir'] = QAction(QIcon(iconPath + 'abrir.png'),'Abrir ...')
        self.acoes['abrir'].setShortcut('Ctrl+A')
        self.acoes['salvar'] = QAction(QIcon(iconPath + 'salvar.png'),'Salvar')
        self.acoes['salvar'].setShortcut('Ctrl+S')
        self.acoes['salvarComo'] = QAction(QIcon(iconPath + 'salvarComo.png'),'Salvar Como ...')

        self.acoes['sair'] = QAction(QIcon(iconPath + 'sair.png'),'Sair') 
        self.acoes['sair'].setShortcut('Ctrl+Q')

        iconPath = self.icone_path + self.os_sep + 'editar' + self.os_sep
        self.acoes['undo'] = QAction(QIcon(iconPath + 'undo.png'),'Desfazer') 
        self.acoes['undo'].setShortcut('Ctrl+Z')
        self.acoes['redo'] = QAction(QIcon(iconPath + 'redo.png'),'Refazer') 
        self.acoes['redo'].setShortcut('Ctrl+Y')
        self.acoes['cortar'] = QAction(QIcon(iconPath + 'cortar.png'),'Cortar') 
        self.acoes['cortar'].setShortcut('Ctrl+X')
        self.acoes['copiar'] = QAction(QIcon(iconPath + 'copiar.png'),'Copiar') 
        self.acoes['copiar'].setShortcut('Ctrl+C')
        self.acoes['colar'] = QAction(QIcon(iconPath + 'colar.png'),'Colar') 
        self.acoes['colar'].setShortcut('Ctrl+V')

        iconPath = self.icone_path + self.os_sep + 'sobre' + self.os_sep
        self.acoes['sobre'] = QAction(QIcon(iconPath + 'iconMaster.png'),'Sobre')


    def conectaAcoes(self):
        # TODO: Conectar ações
        self.acoes['sair'].triggered.connect(self.acaoEncerrar)

    def getAcao(self,nome):
        return self.acoes[nome]

    def mensagemGenerica(self):
        pass

    def acaoEncerrar(self):
        # TODO: verificar arquivo não salvo! 
        QApplication.instance().quit()