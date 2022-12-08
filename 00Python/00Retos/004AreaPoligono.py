'''
 * Crea una única función (importante que sólo sea una) que sea capaz
 * de calcular y retornar el área de un polígono.
 * - La función recibirá por parámetro sólo UN polígono a la vez.
 * - Los polígonos soportados serán Triángulo, Cuadrado y Rectángulo.
 * - Imprime el cálculo del área de un polígono de cada tipo.
'''

def area_poligono(poligono, value_one, value_two):
    if poligono == "triangulo":
        print(f"El area del triangulo es {(value_one*value_two)/2}")
    elif poligono =="cuadrado":
        print(f"El area del cuadrado es {value_one*value_two}")
    elif poligono == "rectangulo":
        print(f"El area del rectangulo es {value_one*value_two}")

if __name__ == "__main__":
    area_poligono("cuadrado", 2, 4)
    area_poligono("triangulo", 2, 4)
    area_poligono("rectangulo", 2, 4)