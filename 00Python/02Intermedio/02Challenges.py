#Reto 0
'''
 * Escribe un programa que muestre por consola (con un print) los
 * números de 1 a 100 (ambos incluidos y con un salto de línea entre
 * cada impresión), sustituyendo los siguientes:
 * - Múltiplos de 3 por la palabra "fizz".
 * - Múltiplos de 5 por la palabra "buzz".
 * - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
 '''

def fizzbuzz():
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("fizzbuzz")
        elif i % 3 == 0:
            print("fizz")
        elif i % 5 == 0:
            print("buzz")
        else:
            print(i)

#fizzbuzz()

#Reto 1
'''
 * Escribe una función que reciba dos palabras (String) y retorne
 * verdadero o falso (Bool) según sean o no anagramas.
 * - Un Anagrama consiste en formar una palabra reordenando TODAS
 *   las letras de otra palabra inicial.
 * - NO hace falta comprobar que ambas palabras existan.
 * - Dos palabras exactamente iguales no son anagrama.
'''
def is_anagrama(str_one, str_two):
    if str_one.lower() == str_two.lower():
        return False
    return sorted(str_one.lower()) == sorted(str_two.lower())

#print(is_anagrama("amor","roma"))

#Reto 2
'''
 * Escribe un programa que imprima los 50 primeros números de la sucesión
 * de Fibonacci empezando en 0.
 * - La serie Fibonacci se compone por una sucesión de números en
 *   la que el siguiente siempre es la suma de los dos anteriores.
 *   0, 1, 1, 2, 3, 5, 8, 13...
'''

def fibonacci():
    num_one = 0
    num_two = 1
    for i in range(1, 51):
        print(num_one)
        fib = num_one + num_two
        num_one = num_two
        num_two = fib

#fibonacci()

#Reto 3
'''
 * Escribe un programa que se encargue de comprobar si un número es o no primo.
 * Hecho esto, imprime los números primos entre 1 y 100.
'''

def primos():
    for number in range(1, 101):
        if number >= 2:
            is_divisible = False
            for index in range(2,number):
                if number % index == 0:
                    is_divisible = True
                    break
            if not is_divisible:
                print(number)

#primos()

#Reto 6
'''
 * Crea un programa que invierta el orden de una cadena de texto
 * sin usar funciones propias del lenguaje que lo hagan de forma automática.
 * - Si le pasamos "Hola mundo" nos retornaría "odnum aloH"
'''
def reverse(text):
    print(text[::-1])

#reverse("hola")

