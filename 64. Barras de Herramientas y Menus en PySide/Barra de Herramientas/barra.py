from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QAction, QIcon
from PySide6.QtWidgets import QMainWindow, QApplication, QLabel, QToolBar, QStatusBar


class Ventana(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Soy una ventana')
        self.setFixedWidth(500)
        self.setFixedHeight(500)
        
        etiqueta = QLabel('Soy una etiqueta')
        etiqueta.setAlignment(Qt.AlignCenter)
        self.setCentralWidget(etiqueta)
        
        barra = QToolBar('Soy una barra de herramientas')
        barra.setIconSize(QSize(16,16))
        self.addToolBar(barra)
        
        boton_nuevo = QAction(QIcon('Barra de Herramientas\\nuevo.png'), 'Nuevo', self)
        barra.addAction(boton_nuevo)
        
        boton_guardado = QAction(QIcon('Barra de Herramientas\\guardar.png'), 'Guardar', self)
        barra.addAction(boton_guardado)
        
        self.setStatusBar(QStatusBar(self))
        
        boton_nuevo.setStatusTip('Hola ha presionado el boton de nuevo, que se le ofrece?')
        boton_guardado.setStatusTip('Hola ha presionado el boton de guardado, que se le ofrece?')
        
        boton_nuevo.triggered.connect(self.click_boton_nuevo)
        boton_guardado.triggered.connect(self.click_guardado)
        
        
    def click_boton_nuevo(self, s):
        print(f'Nuevo archivo: {s}')
        
    def click_guardado(self, s):
        print(f'Guardar archivo: {s}')

if __name__ == '__main__':    
    app = QApplication([])
    ventana = Ventana()
    ventana.show()
    app.exec()
