#Diccionarios
mi_dict = dict()
otro_dict = {}

print(type(otro_dict))

mi_dict = {
    "Nombre":"Alejandro",
    "Apellido":"Alonso", 
    "Edad":24,
    "Lenguajes":["html", "css", "python"]
    }

print(mi_dict)
#Buscar por clave
print(mi_dict["Nombre"])

#Modificar por clave
mi_dict["Nombre"] = "Paco"
print(mi_dict["Nombre"])

#Añadir registros
mi_dict["Calle"] = "Santander"
print(mi_dict["Calle"])

#Eliminar un elemento
del mi_dict["Calle"]
print(mi_dict)

#Comprobar si existe una clave
print("Apellido" in mi_dict)

#Retorna todas las claves
print(mi_dict.keys())
#Retorna todos los valores
print(mi_dict.values())
#Crea una lista con todos los items
print(mi_dict.items())
#Crea un diccionario vacio con las claves que le indicamos
print(mi_dict.fromkeys(("Nombre",1)))