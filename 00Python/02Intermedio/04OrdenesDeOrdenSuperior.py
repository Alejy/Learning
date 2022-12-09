#FUNCIONES DE ORDEN SUPERIOR
#Funciones que llaman a otras funciones

def sum_one(num):
    return num+1

def sum_five(num):
    return num+5

def sum_two_values_and_add_one(first_value, second_value,f):
    return f(first_value+second_value)

print(sum_two_values_and_add_one(2, 4, sum_one))
print(sum_two_values_and_add_one(2, 4, sum_five))

#Closures retorna funciones
#Podemos 

def sum_ten():
    def add(value):
        return value+10
    return add

add_closure = sum_ten()
print(add_closure(5))
print(sum_ten()(5))

#MAP realiza una operacion o funcion con todos los numeros de un iterable.

numbers = [ 2, 5, 4, 6, 8, 10, 25, 30]

def multiply_two(number):
    return number * 2

print(list(map(multiply_two, numbers)))
print(list(map(lambda number: number * 2, numbers)))

#Filter Filtra un numero por condicion de true o false.

def filter_greater_than_ten(number):
    if number > 10:
        return True
    return False

print(list(filter(filter_greater_than_ten, numbers)))
print(list(filter(lambda number: number > 10, numbers)))

#Reduce en este caso suma todos los valores de la lista entre si
import functools

def sum_two_values(value_one, value_two):
    return value_one + value_two

print(functools.reduce(sum_two_values, numbers))