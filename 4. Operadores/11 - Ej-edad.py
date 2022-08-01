edad = int(input("Ingrese su edad: "))

veintes = edad >= 20 and edad < 30
print(veintes)
treintas = edad >= 30 and edad < 40
print(treintas)

if veintes or treintas:
    print("Dentro del rango")
    if veintes:
        print("Dentro de los 20")
    elif treintas:
        print("Dentro de los 30")
else:
    print("Fuera del rango")