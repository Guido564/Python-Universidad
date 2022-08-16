class Aritmetica:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def sumar(self):
        return self.a + self.b
    
    def restar(self):
        return self.a - self.b
    
    def multiplicar(self):
        return self.a * self.b
    
    def dividir(self):
        return self.a / self.b
    
aritmetica1 = Aritmetica(10, 5)

print(aritmetica1.sumar())
print(aritmetica1.restar())
print(aritmetica1.multiplicar())
print(aritmetica1.dividir())
print('Ejemplo')