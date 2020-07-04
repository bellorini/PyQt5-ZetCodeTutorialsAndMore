"""
    Aplicação exemplo para signals and slots

    Apresenta o valor de um Slider no QLCDNumber
    Em 4 bases numéricas: BIN, OCT, DEC (padrão) e HEX

    Autor original: Jan Bodnar
    website: zetcode.com  
"""

import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QWidget, QLCDNumber, QSlider, QVBoxLayout, QApplication,
                            QGroupBox, QButtonGroup, QRadioButton, QHBoxLayout)

class Exemplo(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.lcd = QLCDNumber(self)
        self.lcd.setDigitCount(8)
        self.sld = QSlider(Qt.Horizontal, self)

        vbox = QVBoxLayout()
        vbox.addWidget(self.lcd)
        vbox.addWidget(self.sld)



        self.sld.valueChanged.connect(self.setLcdDisplay)
        # zetCode fez: 
        #ld.valueChanged.connect(lcd.display)

        rBs = self.criaRadioBase()

        vbox.addWidget(rBs)
        self.setLayout(vbox)
        self.setGeometry(300, 300, 350, 350)
        self.setWindowTitle('Signals, Slots e RadioButtons')

        self.show()

    def criaRadioBase(self):
        # pelo o que entendi, o workflow para radioButtons ou checkedButtons exclusivos é:
        # 1- cria-se os botões com suas propriedades individuais
        # 2- organiza-os em *Layout
        # 3- adiciona o *Layout em um QGroupBox (ou QGroupButton)
        # 4- adicona o QGroupBox contendo os radioButtons em um Widget (realizado fora deste método)

        # radioButtons para Base numérica
        self.rB2 = QRadioButton("BIN", self)
        self.rB8 = QRadioButton("OCT", self)
        self.rB10 = QRadioButton("DEC", self)
        self.rB10.setChecked(True)
        self.rB16 = QRadioButton("HEX", self)
        
        # Organização em HorizontalLayout
        hboxGB = QHBoxLayout()
        hboxGB.addWidget(self.rB2)
        hboxGB.addWidget(self.rB8)
        hboxGB.addWidget(self.rB10)
        hboxGB.addWidget(self.rB16)

        # QGroupBox que determina a exclusividade
        gB = QGroupBox("Base Numérica", self)
        gB.setLayout(hboxGB)
        
        # conexões 
        self.rB2.clicked.connect(self.setLcdBase)
        self.rB8.clicked.connect(self.setLcdBase)
        self.rB10.clicked.connect(self.setLcdBase)
        self.rB16.clicked.connect(self.setLcdBase)

        return gB


    def setLcdDisplay(self):
        valor = self.sld.value()
        self.lcd.display(valor)
    
    def setLcdBase(self):
        if self.rB2.isChecked():
            self.lcd.setBinMode()
        elif self.rB8.isChecked():
            self.lcd.setOctMode()
        elif self.rB10.isChecked():
            self.lcd.setDecMode()
        elif self.rB16.isChecked():
            self.lcd.setHexMode()

def main():
    app = QApplication(sys.argv)
    ex = Exemplo()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()