'''
 * Crea un programa que invierta el orden de una cadena de texto
 * sin usar funciones propias del lenguaje que lo hagan de forma automática.
 * - Si le pasamos "Hola mundo" nos retornaría "odnum aloH"
'''
def invertir_str(text):
    return text[::-1]

if __name__=="__main__":
    print(invertir_str("Hola"))