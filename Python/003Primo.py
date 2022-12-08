'''
 * Escribe un programa que se encargue de comprobar si un número es o no primo.
 * Hecho esto, imprime los números primos entre 1 y 100.
 '''

def numeros_primos():
    for num in range(1, 101):
        if num >= 2:
            is_divisible = False
            for i in range(2,num):
                if num % i == 0:
                    is_divisible = True
                    break
            if not is_divisible:
                print(num)

if __name__=="__main__":
    numeros_primos()