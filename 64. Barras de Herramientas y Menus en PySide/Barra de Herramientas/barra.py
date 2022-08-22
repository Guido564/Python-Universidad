from PySide6.QtCore import Qt
from PySide6.QtGui import QAction
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
        self.addToolBar(barra)
        
        boton = QAction('Boton', self)
        barra.addAction(boton)
        
        self.setStatusBar(QStatusBar(self))
        
        boton.setStatusTip('Buen dia, que se le ofrece?')
        
        boton.triggered.connect(self.click_boton)
        
        boton.setCheckable(True)
        
    def click_boton(self, s):
        print(f'Recibiendo click: {s}')

if __name__ == '__main__':    
    app = QApplication([])
    ventana = Ventana()
    ventana.show()
    app.exec()
