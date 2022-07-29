class Cubo:
    def __init__(self, ancho, alto, profundo):
        self.ancho = ancho
        self.alto = alto
        self.profundo = profundo
        
    def calcularVolumen(self):
        volumen = self.ancho * self.alto * self.profundo
        return volumen
   
ancho1 = int(input("Ingrese el ancho: "))
alto1 = int(input("Ingrese el alto: "))
profundo1 = int(input("Ingrese el profundo: "))
    
ejercicio1 = Cubo(ancho1, alto1, profundo1)
print(f'El volumen del cubo es igual a: {ejercicio1.calcularVolumen()} metros cubicos')