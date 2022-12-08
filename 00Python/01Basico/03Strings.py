#String
primer_string = "Esto es una prueba"
segundo_string = "Esto es otra prueba"

print(len(primer_string))
print(primer_string + " " + segundo_string)

salto_linea = "Esto\n es un salto de linea"
print(salto_linea)

tabulador_string = "\t Esto es \n un tabulado"
print(tabulador_string)

escapar_caracteres = "\"Hola\""
print(escapar_caracteres)

name = "Paco"
apellido = "Masa"
edad = 32
print("Mi nombre es {} {} y mi edad es {}".format(name, apellido, edad))
print("Mi nombre es %s %s y mi edad es %d" %(name, apellido, edad))
print(f"Mi nombre es {name} {apellido} y mi edad es {edad}") #Utilizar esta siempre que se pueda
print("Mi nombre es " + name + " " + apellido + " y mi edad es " + str(edad)) #Forma menos eficiente(Evitarlo siempre que podamos)

print(f"Mi edad es {edad-2}")

#Desempaquetado de caracteres

lenguaje = "Python"
a, b,c ,d ,e ,f = lenguaje
print(a)
print(b)
print(f)

#Division

lenguaje_slice = lenguaje[1:3] #Empieza en 0
print(lenguaje_slice)

lenguaje_slice = lenguaje[1:] #Empieza en 0
print(lenguaje_slice)

lenguaje_slice = lenguaje[:3] #Empieza en 0
print(lenguaje_slice)

lenguaje_slice = lenguaje[-3] #Empieza en 0
print(lenguaje_slice)

lenguaje_slice = lenguaje[1:3] #Empieza en 0
print(lenguaje_slice)

#Evitar caracteres con saltos
lenguaje_slice = lenguaje[0:6:2] #Empieza en 0
print(lenguaje_slice)

#Reverse
lenguaje_slice = lenguaje[::-1] #Empieza en 0
print(lenguaje_slice)

#Funciones del sistema
prueba = "hOlA"
print(prueba.capitalize())#Primera letra mayuscula luego minusculas
print(prueba.lower())#Todo en minuscula
print(prueba.upper())#Todo en mayuscula
print(prueba.count("O"))#Cuenta los caracteres
print(prueba.isnumeric())#Comprueba si es un numero
print("1".isnumeric())#Comprueba si es un numero
print(prueba.lower().isupper())#Concatena convierte en minuscula y comprueba si es mayuscula
print(prueba.startswith("hO"))#Comprueba como empieza
