a = int(input("Ingrese el primer valor: "))
b = int(input("Ingrese el segundo valor: "))

primerVal = a > b
segVal = a < b

if primerVal:
    print(f"{a} es mayor que {b}")
elif segVal:
    print(f"{b} es mayor que {a}")
else:
    print("Es posible que los valores sean iguales")