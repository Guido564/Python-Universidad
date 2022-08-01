frutas = ("naranja", "manzana", "frambuesa")
print(frutas)

for fruta in frutas:
    print(fruta, end=" ")

frutaLista = list(frutas)
frutaLista[0] = "pera"
print(frutaLista)
frutas = tuple(frutaLista)
print(frutas)

del frutas
print(frutas)