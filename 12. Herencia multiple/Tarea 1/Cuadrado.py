from FiguraGeometrica import FiguraGeometrica
from Color import Color

class Cuadrado(FiguraGeometrica, Color):
    def __init__(self, ancho, color):
        FiguraGeometrica.__init__(self, ancho, ancho)
        Color.__init__(self, color)
        
    def __str__(self):
        return f'{FiguraGeometrica.__str__(self)}, ademas con {Color.__str__(self)}'
    
    def calcularArea(self):
        return f'El area del cuadrado es de {self.ancho * self.ancho}'

if __name__ == "__main__":
    cuadrado1 = Cuadrado(5, "rojo")
    print(cuadrado1.calcularArea())
    print(cuadrado1)

    cuadrado2 = Cuadrado(7, "marron")
    print(cuadrado2.calcularArea())
    print(cuadrado2)