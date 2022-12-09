#Primero instalamos mongodb community edition en nuestro equipo.
#Instalamos la libreria e importamos pymongo para trabajar con mongodb
import pymongo

#Creamos una conexion con la base de datos
mongo_uri = 'mongodb://localhost:27017'
conn = pymongo.MongoClient(mongo_uri)
'''
Otra forma de hacer la conexion con la base de datos
conn = pymongo.MongoClient('localhost, 27017)
'''

#Creamos la base de datos y las coleccion
db = conn['db-world']
collection = db["collection-people"]
collection_two = db["collection-dogs"]

#Insertamos data en la coleccion people
collection.insert_one({"name": "Alejandro", "age": 24})
collection_two.insert_one({"name": "Thoby", "age": 4})

#insertar data en una coleccion
person_one = {"name": "Paco", "age": 36}
person_two = {"name": "Isidro", "age": 24}
person_three = {"name": "Lucia", "age": 27}
collection.insert_many([person_one, person_two, person_three])


print("------")
#Reportar toda la coleccion
results = collection.find()
for r in results:
    print(r)

#Reportar toda la coleccion pero unicamente el nombre y edad
'''results = collection.find()
for r in results:
    print(f"Nombre: {r['name']} Edad: {r['age']}")'''


print("------")
#Buscar todos los que tengan 24años de edad
results = collection.find({"age":24})
for r in results:
    print(r)


print("------")
#Reportar el nombre de las coleciones:
print(db.list_collection_names())

#Borrar registros que el nombre sea Alejandro
collection.delete_many({"name":"Alejandro"})


print("------")
#Actualizar registros
print(collection.find_one({"name":"Lucia"}))
collection.update_one({"name":"Lucia"}, {"$set":{"age":34}})
print(collection.find_one({"name":"Lucia"}))


#Eliminar coleccion dogs
collection_two.drop()
#Eliminar db
'''conn.drop_database("world")'''
