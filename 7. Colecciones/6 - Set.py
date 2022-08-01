planetas = {"jupiter", "venus", "uranos"}
print(planetas)

print(len(planetas))
print("venus" in planetas)

planetas.add("tierra")
print(planetas)

planetas.add("tierra")
print(planetas)

planetas.remove("venus")
print(planetas)

planetas.discard("tierra")
print(planetas)

planetas.clear()
print(planetas)

del planetas
print(planetas)