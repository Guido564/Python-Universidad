diccionario = {
    "HTML":"HyperText Markup Language",
    "CSS":"cascade style sheet",
    "JavaScript":"Lenguaje Orientado a Objetos"
}

for termino, valor in diccionario.items():
    print(termino, valor)

for termino in diccionario.keys():
    print(termino)

for termino in diccionario.values():
    print(termino)

print("HTML" in diccionario)

diccionario["Bootstrap"] = " Library that focuses on simplifying the development of informative web pages"
print(diccionario)

diccionario.pop("Bootstrap")
print(diccionario)

diccionario.clear()
print(diccionario)

del diccionario
print(diccionario)