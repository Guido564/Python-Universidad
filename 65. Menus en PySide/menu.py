from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QAction, QIcon
from PySide6.QtWidgets import QMainWindow, QApplication, QLabel, QToolBar, QStatusBar
import sys


class Ventana(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Soy una ventana')
        self.setFixedWidth(600)
        self.setFixedHeight(600)
        
        etiqueta = QLabel('Soy una etiqueta')
        etiqueta.setAlignment(Qt.AlignCenter)
        self.setCentralWidget(etiqueta)
        
        barra = QToolBar('Soy una barra de herramientas')
        barra.setIconSize(QSize(16,16))
        
        
        boton_nuevo = QAction(QIcon('64. Barras de Herramientas y Menus en PySide\Barra de Herramientas\\nuevo.png'), 'Nuevo', self)

        boton_guardado = QAction(QIcon('64. Barras de Herramientas y Menus en PySide\Barra de Herramientas\guardar.png'), 'Guardar', self)
        
        boton_salir = QAction(QIcon('65. Menus en PySide\salir.png'), 'Salir', self)
        
        boton_ayuda = QAction(QIcon('65. Menus en PySide\\acerca.png'), 'Acerca de', self)

        self.setStatusBar(QStatusBar(self))
        
        boton_nuevo.setStatusTip('Hola esta por presionar el boton de nuevo, que se le ofrece?')
        boton_guardado.setStatusTip('Hola esta por presionar el boton de guardado, que se le ofrece?')
        boton_salir.setStatusTip('Con esto salis del programa')
        boton_ayuda.setStatusTip('Usted esta a punto de recibir informacion basica acerca de la funcionalidad de mi humilde programa')
        
        boton_nuevo.triggered.connect(self.click_boton_nuevo)
        boton_guardado.triggered.connect(self.click_guardado)
        boton_salir.triggered.connect(self.click_salir)
        boton_ayuda.triggered.connect(self.click_acerca)
        
        barra.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        
        menu = self.menuBar()
        menu_archivo = menu.addMenu('Archivo')
        menu_archivo.addAction(boton_nuevo)
        menu_archivo.addAction(boton_guardado)
        menu_archivo.addSeparator()
        menu_archivo.addAction(boton_salir)
        
        menu_ayuda = menu.addMenu('Ayuda')
        menu_ayuda.addAction(boton_ayuda)
        
    def click_boton_nuevo(self, s):
        print(f'Nuevo archivo: {s}')
        
    def click_guardado(self, s):
        print(f'Archivo guardado: {s}')
        
    def click_salir(self):
        print('Bye')
        sys.exit()
        
    def click_acerca(self):
        print('De momento poco y nada')

if __name__ == '__main__':    
    app = QApplication([])
    ventana = Ventana()
    ventana.show()
    app.exec()