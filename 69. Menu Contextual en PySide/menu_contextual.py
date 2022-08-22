import sys
from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QAction, QIcon
from PySide6.QtWidgets import QApplication, QMainWindow, QMenu, QStatusBar


class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Menu Contextual')
    
    def contextMenuEvent(self, evento):
        menu_contextual = QMenu(self)
        
        boton_nuevo = QAction(QIcon('69. Menu Contextual en PySide\\nuevo.png'), 'Nuevo', self)
        boton_guardar = QAction(QIcon('69. Menu Contextual en PySide\\guardar.png'), 'Guardar', self)
        boton_salir = QAction(QIcon('69. Menu Contextual en PySide\\salir.png'), 'Salir', self)
        
        boton_nuevo.triggered.connect(self.click_boton_nuevo)
        boton_guardar.triggered.connect(self.click_guardar)
        boton_salir.triggered.connect(self.click_salir)
        
        menu_contextual.addAction(boton_nuevo)
        menu_contextual.addAction(boton_guardar)
        menu_contextual.addSeparator()
        menu_contextual.addAction(boton_salir)
        
        menu_contextual.exec(evento.globalPos())
        
 
    def click_boton_nuevo(self, s):
        print(f'Nuevo archivo: {s}')
        
    def click_guardar(self, s):
        print(f'Archivo guardado: {s}')

    def click_salir(self):
        print('Bye')
        sys.exit()

if __name__ == '__main__':
    app = QApplication([])
    ventana = VentanaPrincipal()
    ventana.show()
    app.exec()