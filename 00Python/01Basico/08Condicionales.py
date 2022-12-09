#Condicionales

a = 6
b = 10
c = 6

if a > b:
    print(f" {a} es mayor que {b} ")
else:
    print(f" {b} es mayor que {a}")

if a > b and c > b:
    print(f"{a} y {c} es mayor que {b}")
elif a == c and a < b:
    print(f"{a} y {b} son menores que {c}")
else:
    print("No se cumple ninguna condicion")

#Negamos
if not a > b:
    print(f"{a} es menor que {b}")