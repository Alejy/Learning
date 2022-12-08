#Clases - Los nombres de las clases se escriben en mayuscula.
#Cada clase contiene funciones y objetos que son caracteristicas de ella misma.

class MyEmptyPerson:
    pass

#Construimos una clase y creamos una funcion init donde siempre se llama a self y otros parametros. 
class Person:
    def __init__(self, name, apellido, alias = "Sin alias"): #Declaramos variables default
        self.name = name
        self.apellido = apellido
        self.alias = alias
        self.fullname = f"{name} {apellido} {alias}"
        self.__hiddenname = name #Es una variable PRIVADA no se la puede llamar desde fuera pero si utilizar en otras funciones de la clase.
#Si le añadimos self podremos acceder a todas las variables almacenadas en self.
    def walk(self):
        print(f"{self.name} esta Caminando")

#Creamos un objeto y le indicamos las clase y sus parametros.
my_person = Person("Alejandro", "Alonso")
print(type(my_person))
print(my_person.name)
print(my_person.fullname)
my_person.walk()


other_person = Person("Paco", "Masa", "Privilegiado")
print(other_person.fullname)

#Se pueden renombrar las variables de cada objeto
other_person.fullname = 555
print(other_person.fullname)