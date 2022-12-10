#Listas

mi_lista = [32, 24, 45, 76, 88, 45]

print(len(mi_lista))
print(mi_lista)
print(len(mi_lista))

otra_lista = [32, "paco", 65, "hola"]

print(type(otra_lista))

print(otra_lista)
print(otra_lista[0])#Empieza en 0
print(otra_lista[1:3])#Selecionar varios

print(otra_lista.count("paco"))

edad, nombre, dientes, palabra = otra_lista
print(edad)
print(nombre)

print(mi_lista, otra_lista)

#Concatena listas y las dos formas de declarar una lista
list_uno = [1,2,3]
list_dos = list([1,2,3])
print(list_uno+list_dos)

#Modificar datos
list_uno.append("hola")
print(list_uno)

list_uno.insert(0,"azul")
print(list_uno)

list_uno.remove(1)
print(list_uno)

list_tres = [30, 30, 30]
list_tres.remove(30)
print(list_tres)

#Elimina el ultimo elemento retornando el elemento
list_cuatro = [30, 40, 23]
print(list_cuatro)
print(list_cuatro.pop())#Tambien puedes indicarle el indice
print(list_cuatro)

#Eliminar por posicion
del list_cuatro[0]
print(list_cuatro)

list_cinco = list_cuatro.copy()
print(list_cinco)
list_cinco.clear()
print(list_cinco)

list_seis = [1, 2, 3, 4, 5, 6, 7, 8]
print(list_seis)
list_seis.reverse()
print(list_seis)
list_seis.sort()
print(list_seis)


print(list_seis.index(2))