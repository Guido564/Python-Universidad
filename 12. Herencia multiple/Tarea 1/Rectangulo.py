from FiguraGeometrica import FiguraGeometrica
from Color import Color

class Rectangulo(FiguraGeometrica, Color):
    def __init__(self, alto, ancho, color):
        FiguraGeometrica.__init__(self, alto, ancho)
        Color.__init__(self, color)
        
    def __str__(self):
        return f'{FiguraGeometrica.__str__(self)}, ademas con {Color.__str__(self)}'
    
    def calcularArea(self):
        return f'El area del rectangulo es de {self.alto * self.ancho}'
    
if __name__ == "__main__":
    rectangulo1 = Rectangulo(10, 5, "violeta")
    print(rectangulo1.calcularArea())
    print(rectangulo1)