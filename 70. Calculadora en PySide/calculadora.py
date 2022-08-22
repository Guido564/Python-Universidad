from PySide6.QtCore import Qt
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import *


class Calculadora(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Soy una calcu')
        self.setWindowIcon(QIcon('70. Calculadora en PySide\calculadora.png'))
        self.setFixedSize(240, 230)
        
        self.componente_general = QWidget(self)
        self.setCentralWidget(self.componente_general)
        
        self.layout_principal = QVBoxLayout()
        self.componente_general.setLayout(self.layout_principal)
        
        self._caja_texto()
        self._creacion_botones()
        
    def _caja_texto(self):
        self.caja = QLineEdit()
        self.caja.setFixedHeight(35)
        self.caja.setAlignment(Qt.AlignRight)
        self.caja.setReadOnly(True)
        
        self.layout_principal.addWidget(self.caja)
        
    def _creacion_botones(self):
        self.botones = {}
        layout_botones = QGridLayout()
        botones = {
            '7':(0,0),
            '8':(0,1),
            '9':(0,2),
            '/':(0,3),
            '4':(1,0),
            '5':(1,1),
            '6':(1,2),
            '*':(1,3),
            '1':(2,0),
            '2':(2,1),
            '3':(2,2),
            '-':(2,3),
            '0':(3,0),
            '.':(3,1),
            'C':(3,2),
            '+':(3,3),
            '=':(3,4)
        }
        
        for texto, posicion in botones.items():
            self.botones[texto] = QPushButton(texto)
            self.botones[texto].setFixedSize(40,40)
            layout_botones.addWidget(self.botones[texto], posicion[0],posicion[1])
        
        self.layout_principal.addLayout(layout_botones)  
        

if __name__ == '__main__':    
    app = QApplication([])
    ventana = Calculadora()
    ventana.show()
    app.exec()
