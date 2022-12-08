#Functions

def mi_function():
    print("Esto es una function")

mi_function()

def sum_two_values(a,b):
    print(a+b)

sum_two_values(1,2)

def sum_two_values(a,b):
    print(a+b)

sum_two_values("a","b")

def return_values(a,b):
    return a+b

total = return_values(2, 5)
print(total)


def list_lower(*texts):
    for i in texts:
        print(i.lower())

list_lower("PACO", "JorGE", "MANOLO")