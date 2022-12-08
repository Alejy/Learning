#Variables

primera_variable = "Variable1"
print(primera_variable)

int_variable = 2
print(int_variable)

bool_variable = True
print(bool_variable)

#Concatenar variables y texto
print(primera_variable, int_variable, bool_variable)
print("Mi primera variable: ", primera_variable)

#Funciones de python

#str() convierte una variable a tipo string
print(primera_variable + str(int_variable) + str(bool_variable))

#len() indica la longitud del string
print(len(primera_variable))

#Variables en una linea: No es una buena practica!
nombre, apellido, edad = "Paco", "Alonso", 32
print("Yo soy:", nombre, apellido, edad)

#Inputs
first_name = input("Cual es tu nombre: ")
edad = input("Cual es tu edad: ")

print(first_name)
print(edad)

#Las variables son mutables y pueden cambiar tanto su contenido como su tipo de dato.
first_name = 2
print(type(first_name))