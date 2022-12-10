'''
 * Escribe un programa que imprima los 50 primeros números de la sucesión
 * de Fibonacci empezando en 0.
 * - La serie Fibonacci se compone por una sucesión de números en
 *   la que el siguiente siempre es la suma de los dos anteriores.
 *   0, 1, 1, 2, 3, 5, 8, 13...
'''

def fibonacci():
    first_num = 0
    second_num = 1
    for i in range(1,51):
        print(first_num)
        fib_num = first_num + second_num
        first_num = second_num
        second_num = fib_num
        

if __name__=="__main__":
    fibonacci()