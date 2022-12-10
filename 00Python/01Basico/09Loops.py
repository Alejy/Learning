#Loops o Bucles

#WHILE
#while true mientras algo no sea true sigue el bucle.

mi_condition = 0
while mi_condition < 10:
    print(mi_condition)
    mi_condition += 1
else:
    print("Se a completado la condicion")

otra_condition = 0
while otra_condition < 10:
    print(otra_condition)
    otra_condition += 1
    if otra_condition == 5:
        print("Es igual a 5")
        break                   #Tambien se puede utilizar continue para segir el bucle pero sin ejecutar el resto del codigo
else:
    print("Se ha salido del bucle")


#FOR exite break y continue para parar o continuar el bucle pero reiniciandole de nuevo

list_uno = [1, 2, 3, 4, 5, 6, 7]
for i in list_uno:
    print(i)
    if i == 3:
        print("i igual a 3")
        continue
        print("No se ejecuta con el continue")
else:
    print("hemos salido del for")