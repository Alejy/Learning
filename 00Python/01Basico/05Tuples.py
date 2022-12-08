#Tuplas es inmutable no se pueden modificar los elementos.

mi_tupla = tuple()
otra_tupla = ()

mi_tupla = (35, 1.70, "Alejandro", "Alonso")

print(mi_tupla)
print(type(mi_tupla))

print(mi_tupla[0])

print(mi_tupla.count("Alejandro"))
print(mi_tupla.index("Alejandro"))

#Ahora si podemos modificarla al convertirla en una lista
mi_tupla = list(mi_tupla)
print(type(mi_tupla))
print(mi_tupla)
mi_tupla.append(34)
mi_tupla = tuple(mi_tupla)
print(mi_tupla)
print(type(mi_tupla))