#Error Types

#SyntaxError
#print "Hola Mundo"
print("Hola Mundo")

#NameError
#print(language) #language no declarado
language = "Spanish"
print(language)

#IndexError
mi_lista = [ 1, 2, 3, 4]
#print(mi_lista[4]) No existe esta posicion
print(mi_lista[3])

#ModuleNotFoundError
#import maths no existe este modulo
import math

#AttributeError
#print(math.PI) no existe el atributo
print(math.pi)

#KeyError
my_dict = {"name":"Paco", "surname":"Alonso"}
#print(my_dict["naame"])    Error de la clave que no existe
print(my_dict["name"])

#TypeError
my_list = [1, 2, 3, 4, 5]
#print(my_list["0"])    Estamos buscando un string cuando queremos una posicion.
print(my_list[2])

#ImportError
#from math import PI    PI en mayuscula no existe
from math import pi

#ValueError
#my_int = int("10years") Error
my_int = 10
print(my_int)

#ZeroDivisionError
#print(4/0)
print(4/2)

#4:20