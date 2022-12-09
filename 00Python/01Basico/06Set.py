#SETS Primero se declara como un diccionario pero al añadirle datos en forma de set se convierte en un set.
#Set no es una estructura ordenada, no admite datos repetidos

mi_set = set()
otro_set = {}

print(type(otro_set))

otro_set = {1, 2, "3"}
print(type(otro_set))

print(len(otro_set))

#print(otro_set[1]) no se puede acceder a un set de esta forma

#Añador datos no permite datos duplicados
otro_set.add("Alejandro")
print(otro_set)
otro_set.add("Alejandro")
print(otro_set)

otro_set.remove("Alejandro")
print(otro_set)

#Elimina los items dentro del set
otro_set.clear()
print(otro_set)
#Elimina la variable set
del otro_set
#print(otro_set) Error Variable no definidad

#Convertir set a lista
otro_set = {"Hola", "Adios", 43, 22}
otro_list = list(otro_set)
print(type(otro_list))

#Unir sets
otro_set_mas = {"Paco", "Masa", 32}
union_set = otro_set.union(otro_set_mas).union({"java"})
print(union_set)

#Diferencia entre dos set
print(union_set.difference(otro_set_mas))