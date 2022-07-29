class Persona:
    contador_persona = 0
    
    @classmethod
    def generarSiguienteValor(cls):
        cls.contador_persona += 1
        return cls.contador_persona
    
    def __init__(self, nombre, edad):
        self.idPersona = Persona.generarSiguienteValor()
        self.nombre = nombre
        self.edad = edad
        
    def __str__(self):
        return f'Persona [{self.idPersona} {self.nombre} {self.edad}]'
    
persona1 = Persona("Guido", 25)
print(persona1)
persona2 = Persona("Michelle", 21)
print(persona2)
persona3 = Persona("Julia", 10)
print(persona3)