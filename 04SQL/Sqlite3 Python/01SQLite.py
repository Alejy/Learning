#Importamos la librteria de sqlite para trabajar con este tipo de BBDD
import sqlite3
import os


#Comprobamos si existe el directorio databases y sino lo creamos:
if not os.path.exists('Databases'):
    os.mkdir('Databases')


#Creamos la conexion con la base de datos si no existe la crea:
conn = sqlite3.connect("Databases/01Database.db")


#Creamos una tabla en la bbdd se puede realizar de dos formas para realizar el control de errores:
#En la primera controlamos la existencia de una tabla persona con codigo python.
try:
    sql_sentence = '''create table people (
        name text,
        surname text,
        age TINYINT,
        nick VARCHAR
    )'''
    conn.execute(sql_sentence)
    print("La tabla personas ha sido creada")
except sqlite3.OperationalError:
    print("La tabla personas ya existe")
#La segunda forma controlamos la existencia de una tabla personas con la sentencia SQL.
'''sql_sentence = """create table if not exists people(
    name text,
    surname text,
    age integer,
    nick text
    )"""
conn.execute(sql_sentence)'''


#Insertar filas en una tabla:
'''sql_sentence = 'insert into people(name, surname, age, nick) values(?, ?, ?, ?)'
person = ["Paco", "Martin", 18, "Paquito"]
conn.execute(sql_sentence, person)
conn.commit()'''


#Insertar varias columnas
'''sql_sentence = 'insert into people(name, surname, age, nick) values(?, ?, ?, ?)'
people = [["Rafa", "Lugan", 23, "Rafita"], ["Alejandro", "Salvador", 54, "Alex23"],["Lucia", "Salmo", 67, "Luci"],["Sergio", "Losa", 14, "SLosa52"]]
for person in people:
    conn.execute(sql_sentence, person)
    conn.commit()'''


#Buscar en la base de datos:
#Recuperar toda la base de datos:
sql_sentence = "select * from people"
cursor = conn.execute(sql_sentence)
for fila in cursor:
    print(fila)
#Recuperar algunas filas de la base de datos:
sql_sentence = "select name, age from people"
cursor = conn.execute(sql_sentence)
for fila in cursor:
    print(fila)
#Recuperar fila por nombre
sql_sentence = "select * from people where name=?"
name = "Alejandro"
cursor = conn.execute(sql_sentence, (name,))
for fila in cursor:
    print(fila)


#Actualizar datos de una tabla:
#Modificamos la edad de Alejandro de 54 a 24
sql_sentence = "update people set age=? where name=?"
name = "Alejandro"
age = 24
conn.execute(sql_sentence, (age, name))
conn.commit()


#Comprobamos el Update.
sql_sentence = "select * from people where name=?"
name = "Alejandro"
cursor = conn.execute(sql_sentence, (name,))
for fila in cursor:
    print(fila)


#Cerramos la conexion con la bbdd
conn.close()