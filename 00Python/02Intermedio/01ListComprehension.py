#Listas Comprimidas

original_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
mi_lista = [i for i in original_list]
print(mi_lista)

rango = range(8)
print(rango)

#Crear lista con range
mi_lista = [ i for i in range(8)]
print(mi_lista)

#Crear lista empezando por 1
mi_lista = [ i +1 for i in range(8)]
print(mi_lista)

#Crear lista de 10 en 10
mi_lista = [ i * 10 for i in range(8)]
print(mi_lista)

#Utilizar funciones para modificar la lista
def sum_five(number):
    return number +5
mi_lista = [ sum_five(i) for i in range(8)]
print(mi_lista)