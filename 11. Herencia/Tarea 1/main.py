from sre_constants import BIGCHARSET


class Vehiculo:
    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas
    
    def __str__(self):
        return f'Las caracteristicas principales a destacar son un aromatico color {self.color} y la hermosa movilidad de {self.ruedas} ruedas'

class Coche(Vehiculo):
    def __init__(self, color, ruedas, velocidad):
        super().__init__(color, ruedas)
        self.velocidad = velocidad
    
    def __str__(self):
        return f'{super().__str__()} ademas de una velocidad de {self.velocidad} kms/h que permite recorrer convenientes distancia sin un alto consumo de combustible'

class Bicicleta(Vehiculo):
    def __init__(self, color, ruedas, tipo):
        super().__init__(color, ruedas)
        self.tipo = tipo
    
    def __str__(self):
        return f'{super().__str__()} aparte de su unica exclusividad de modelo tipo {self.tipo}'

vehiculoAnonimo = Vehiculo("negro", 8)
print(vehiculoAnonimo)
print("Divisor".center(120, "-"))
autoFiat = Coche("blanco", 4, 180)
print(autoFiat)
bici = Bicicleta("rojo", 2, "montania")
print("Divisor".center(120, "-"))
print(bici)
