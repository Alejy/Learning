#FECHAS

from datetime import datetime

now = datetime.now()

#Es un estandar para indicar el momento actual es el tiempo pasado desde 1970 y es mas facil para propagar que otras formas defechas.
timestamp = now.timestamp()
print(timestamp)

def print_date(date):
    print(date.year)
    print(date.month)
    print(date.day)
    print(date.hour)
    print(date.minute)
    print(date.second)
    print(date.timestamp())

print_date(now)
print("------------------------------")

year_2023 = datetime(2023, 1, 1)
print_date(year_2023)
print("------------------------------")

#Time no tiene informacion le tienes que indicar la informacion
from datetime import time
current_time = time(13,7,30)
print(current_time)
print(current_time.hour)
print(current_time.minute)
print(current_time.second)
print("------------------------------")

#Fecha actual
from datetime import date
current_date = date.today()
print(current_time)
print(current_date.year)
print(current_date.month)
print(current_date.day)
print("------------------------------")

#Modificar datos
current_date = date(current_date.year + 5,12,2)
print(current_date)
print(current_date.year)
print(current_date.month)
print(current_date.day)
print("------------------------------")

#Crear fechas
current_date = date(2023,12,2)
print(current_date)
print(current_date.year)
print(current_date.month)
print(current_date.day)
print("------------------------------")

#Operar con tiempos
year_one = datetime(2027,5,30)
year_two = datetime.now()

print(year_one - year_two)

time_one = datetime.now()
time_two = time(13,21,35)

# print(time_one.time - time_two) Error no permite operarlo entre si
print("------------------------------")

from datetime import timedelta
init_timedelta = timedelta(200, 100 ,100, weeks=10)
end_timedelta = timedelta(300,100,100,weeks=13)

print(init_timedelta + end_timedelta)

#54:46