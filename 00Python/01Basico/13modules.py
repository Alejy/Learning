#Modulos -Añadir modulos permite añadir funcionalidades sin tenerlas que programar desde 0.
#import funciones - Hemos creado un archivo modulo que contitne funciones. Es como una libreria privada.

import modulo
modulo.sum(2,4)
print("------------------------------")

#Permite cambiar el nombre para acceder a las funciones del modulo.
import modulo as md
md.sum(2,4)
print("------------------------------")

#Se puede importar solo algunas funciones del modulo, las que vayamos a necesitar.
from modulo import sum as s
s(2,4)
print("------------------------------")

#Tambien se pueden importar varias funciones
from modulo import sum, hola
hola()
sum(2,4)
print("------------------------------")
import math
print(math.pi)