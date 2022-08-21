from PySide6.QtCore import Qt 
from PySide6.QtGui import QAction
from PySide6.QtWidgets import QApplication, QLabel, QMainWindow, QToolBar


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

if __name__ == '__main__':    
    app = QApplication([])
    ventana = Ventana()
    ventana.show()
    app.exec()
