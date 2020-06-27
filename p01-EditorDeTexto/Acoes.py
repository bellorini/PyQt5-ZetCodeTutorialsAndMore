
from PyQt5.QtWidgets import QApplication, QAction, QMessageBox
from PyQt5.QtGui import QIcon

class AcoesUSeT():
    def __init__(self,icone_path, os_sep, pai):
        # dicionário de ações
        self.acoes = dict()
        self.icone_path = icone_path
        self.os_sep = os_sep
        self.pai = pai
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

        iconPath = self.icone_path + self.os_sep
        self.acoes['verToolBar'] = QAction(QIcon(iconPath + 'checkBoxTrue.png'), 'Barra de Ferramentas Padrão', checkable=True)
        self.acoes['verToolBar'].setChecked(True)


        iconPath = self.icone_path + self.os_sep + 'sobre' + self.os_sep
        self.acoes['sobre'] = QAction(QIcon(iconPath + 'iconMaster.png'),'Sobre')


    def conectaAcoes(self):
        # TODO: Conectar ações
        # menuArquivo
        self.acoes['novo'].triggered.connect(self.mensagemGenericaNaoImplementado)
        self.acoes['abrir'].triggered.connect(self.mensagemGenericaNaoImplementado)
        self.acoes['salvar'].triggered.connect(self.mensagemGenericaNaoImplementado)
        self.acoes['salvarComo'].triggered.connect(self.mensagemGenericaNaoImplementado)
        self.acoes['sair'].triggered.connect(self.acaoEncerrar)

        # menuEditar
        self.acoes['undo'].triggered.connect(self.desfazer)
        self.acoes['redo'].triggered.connect(self.refazer)
        self.acoes['cortar'].triggered.connect(self.mensagemGenericaNaoImplementado)
        self.acoes['copiar'].triggered.connect(self.mensagemGenericaNaoImplementado)
        self.acoes['colar'].triggered.connect(self.mensagemGenericaNaoImplementado)

        # menuVisualizar
        self.acoes['verToolBar'].triggered.connect(self.showToolBar)

        # menuSobre
        self.acoes['sobre'].triggered.connect(self.mostrarJanelaSobre)

    def getAcao(self,nome):
        return self.acoes[nome]

    # acoes do menu Visualizar
    def showToolBar(self):

        iconPath = self.icone_path + self.os_sep
        if self.pai.toolBar.isHidden():
            self.pai.toolBar.setVisible(True)
            self.acoes['verToolBar'].setIcon(QIcon(iconPath + 'checkBoxTrue.png'))
        else:
            self.pai.toolBar.setVisible(False)
            self.acoes['verToolBar'].setIcon(QIcon(iconPath + 'checkBoxFalse.png'))

    # plaeholder para as ações não implementadas
    def mensagemGenericaNaoImplementado(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setWindowTitle('USeT')
        msg.setText('Work in Progress')
        msg.setInformativeText('Função não implementada no momento.')
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()
        pass

    def edicaoTexto(self):
        # placeholder
        print(self.pai.areaTexto.toPlainText())

    # build in undo do QTextEdit
    # ação é gravada a cada linha
    def desfazer(self):
        self.pai.areaTexto.undo()

    # build in redo do QTextEdit
    # ação é gravada a cada linha
    def refazer(self):
        self.pai.areaTexto.redo()

    def acaoEncerrar(self):
        # TODO: verificar arquivo não salvo! 
        QApplication.instance().quit()


    def mostrarJanelaSobre(self):
        self.pai.subWSobre.show()
        pass