'''
 * Escribe una función que reciba dos palabras (String) y retorne
 * verdadero o falso (Bool) según sean o no anagramas.
 * - Un Anagrama consiste en formar una palabra reordenando TODAS
 *   las letras de otra palabra inicial.
 * - NO hace falta comprobar que ambas palabras existan.
 * - Dos palabras exactamente iguales no son anagrama.
'''
def anagrama(str_one, str_two):
    if str_one == str_two:
        return False
    elif sorted(str_one) == sorted(str_two):
        return True
    else:
        return False

if __name__ == "__main__":
    print(anagrama("amor","roma"))
    print(anagrama("amor","amor"))
    print(anagrama("amor","salsa"))