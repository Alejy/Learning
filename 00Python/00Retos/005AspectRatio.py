'''
 * Crea un programa que se encargue de calcular el aspect ratio de una
 * imagen a partir de una url.
 * - Url de ejemplo: https://raw.githubusercontent.com/mouredev/
 *   mouredev/master/mouredev_github_profile.png
 * - Por ratio hacemos referencia por ejemplo a los "16:9" de una
 *   imagen de 1920*1080px.
'''
from PIL import Image
import requests

def aspect_ratio(url):
    img = Image.open(requests.get(url, stream=True).raw)
    if round(img.size[0]/img.size[1], 1) == 1.5:
        print("Aspect Ratio 3:2")
    elif round(img.size[0]/img.size[1], 1) == 1.3:
        print("Aspect Ratio 4:3")
    elif round(img.size[0]/img.size[1], 2) == 1.25:
        print("Aspect Ratio 5:4")
    elif round(img.size[0]/img.size[1], 1) == 1.6:
        print("Aspect Ratio 16:10")
    elif round(img.size[0]/img.size[1], 2) == 1.77:
        print("Aspect Ratio 16:9")
    elif round(img.size[0]/img.size[1], 2) == 0.56:
        print("Aspect Ratio 9:16")
    else:
        print(f"No se ha encontrado ningun Aspect ratio adecuado {img.size[0]} x {img.size[1]}")

if __name__=="__main__":
    aspect_ratio("https://img.freepik.com/fotos-premium/mar-cielo-azul-sereno-fondo-vertical-o-fondo-pantalla-dispositivos-moviles-16-9_483040-3252.jpg?w=740")