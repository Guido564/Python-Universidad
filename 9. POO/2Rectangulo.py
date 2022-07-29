class Rectangulo:
    def __init__(self, altura, base):
        self.altura = altura
        self.base = base
        
    def calcularArea(self):
        area = self.base * self.altura
        return area
    
ejercicio1 = Rectangulo(int(input("Ingrese altura: ")), int(input("Ingrese base: ")))
print(f'El area del rectangulo es igual a: {ejercicio1.calcularArea()}')