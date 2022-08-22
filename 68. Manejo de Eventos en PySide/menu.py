from PySide6.QtWidgets import QApplication, QMainWindow, QLabel

class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Eventos')
        self.etiqueta = QLabel('Si es tan amable salude a esta ventana con un pituco click')
        self.setCentralWidget(self.etiqueta)
        
    def mouseMoveEvent(self, event):
        self.etiqueta.setText('Te vas a marear, tio')
        
    def mousePressEvent(self, event):
        self.etiqueta.setText('Click!')
        
    def mouseReleaseEvent(self, event):
        self.etiqueta.setText('Haga click click!')
        
    def mouseDoubleClickEvent(self, event):
        self.etiqueta.setText('Mucho entusiasmo')

if __name__ == '__main__':
    app = QApplication([])
    ventana = VentanaPrincipal()
    ventana.show()
    app.exec()