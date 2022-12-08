#Exceptions Handling

num_one = 5
num_two = "1"
num_three = 8

try:
    print(num_one + num_two)
except:
    print("Se ha producido un Error")

print("------------------------------")

#Excep y else solo se ejecuta si se ha producido un error
try:
    print(num_one + num_three)
except:
    #Se ejecuta si se ha producido un error
    print("Se ha producido un Error")
else:
    #Se ejecuta si no hay un error
    print("La ejecucion continua1")
finally:
    #Se ejecuta siempre al final
    print("La ejecucion continua2")

print("------------------------------")
try:
    print(num_one + num_two)
except:
    print("Se ha producido un Error")
else:
    print("La ejecucion continua1")
finally:
    print("La ejecucion continua2")

print("------------------------------")

try:
    print(num_one + num_two)
except TypeError:
    print("Se ha producido un Error de typo")
except ValueError:
    print("Se ha producido un Error de valor")


print("------------------------------")

#Se puede almacenar el error en una variable para reportarlo en un log o reportarlo al usuario.
#Exception reporta cualquier tipo de error no hace falta repprtar cada tipo de error a una variable. Como ValueError o TypeError.
try:
    print(num_one + num_two)
except ValueError as error:
    print("Se ha producido un Error de valor")
except Exception as random_error:
    print(random_error)
