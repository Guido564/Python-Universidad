nombres = ["guido", "daniel", "domingo"]

print(len(nombres))

nombres.append("matias")
print(nombres)

nombres.insert(1, "sergio")
print(nombres)

nombres.remove("matias")
print(nombres)

nombres.pop()
print(nombres)

del nombres[2]
print(nombres)

nombres.clear()
print(nombres)

del nombres
print(nombres)