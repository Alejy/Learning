#RegularExpresion
import re

my_string = "Esta es la lección número: 7 Expresiones Regulares Lección"

#Match busca una coincidencia en el inicio del texto
match = re.match("Esta es la lección", my_string)
print(re.match("Esta es la lección", my_string)) #Empieza a buscar desde el principio
print(re.match("es la lección", my_string)) #Como empieza a buscar desde el principio dice que no lo encuentra.

print(match.span()) #Nos indica entre que caracteres ha hecho el match
span = match.span()
print(span)
print(my_string[span[0]: span[1]])

#Search Busca la coincidencia del texto en cualquier lugar del texto
#Como vemos el ultimo parametro indica que convierta todo a minusculas y  busque si hay una coincidencia
search = re.search("Lección", my_string, re.I)
print(search)
print(search.span())

#Findall recupera una lista con las veces que ha encontrado la palabra

findall = re.findall("Lección", my_string, re.I)
print(findall)

#Split Busca un elemento y divide el texto desde ahi.
split = re.split(":", my_string)
print(split)

#Sub sustituye en este caso las dos palabras tanto con mayuscula como con minuscula.
print(re.sub("lección|Lección", "LECCION", my_string))
print(re.sub("[l|L]ección", "LECCION", my_string))


#Patrones REGEX

pattern = r"[lL]ección"
print(re.findall(pattern, my_string))

pattern_two = r"[l|L]ección|Expresiones"
print(re.findall(pattern_two, my_string))

pattern_three = r"[0-9]"
print(re.findall(pattern_three, my_string))

#Todo lo que sean numeros
pattern_four = r"\d"
print(re.findall(pattern_four, my_string))

#Todo lo que no sean numeros
pattern_five = r"\D"
print(re.findall(pattern_five, my_string))

#Expresion regurlar correo electronicp
pattern_six = r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+'
mail = "alejandro12@gmail.com"
print(re.match(pattern_six, mail))