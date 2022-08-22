from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel

class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Eventos')
        self.etiqueta = QLabel('Si es tan amable salude a esta ventana con un pituco click')
        self.setCentralWidget(self.etiqueta)
        
    def mouseMoveEvent(self):
        self.etiqueta.setText('Te vas a marear, tio (Click Izq)')
        
    
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.etiqueta.setText('Click! (Click Izq)')
        elif event.button() == Qt.MiddleButton:
            self.etiqueta.setText('Click! (Click Middle)')
        elif event.button() == Qt.RightButton:
            self.etiqueta.setText('Click! (Click Right)')

        
    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.etiqueta.setText('Haga click click! (Uso: Click Izq)')
        elif event.button() == Qt.MiddleButton:
            self.etiqueta.setText('Haga click click! (Uso: Click Middle)')
        elif event.button() == Qt.RightButton:
            self.etiqueta.setText('Haga click click! (Uso: Click Right)')
        
        
    def mouseDoubleClickEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.etiqueta.setText('Mucho entusiasmo (Click Izq)')
        elif event.button() == Qt.MiddleButton:
            self.etiqueta.setText('Mucho entusiasmo (Click Middle)')
        elif event.button() == Qt.RightButton:
            self.etiqueta.setText('Mucho entusiasmo (Click Right)')
        

if __name__ == '__main__':
    app = QApplication([])
    ventana = VentanaPrincipal()
    ventana.show()
    app.exec()