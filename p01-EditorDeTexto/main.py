"""
    Editor de Texto
    Baseado nos tutoriais de Jan Bodnar
    website: zetcode.com    
    
    Layout:
    - Barra de Menus
    - Barra de Ferramentas
    - Barra de Status
    - Area de Edição

    Aviso legal:
    - Icones: 
        - material-design-icons
        - https://github.com/google/material-design-icons
        - Apache License Version 2.0

"""
from PyQt5.QtWidgets import QApplication
import sys

import interfaceUSeT

class main():
    app = QApplication(sys.argv)
    janela = interfaceUSeT.JanelaPrincipal()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
