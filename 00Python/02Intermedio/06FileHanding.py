#FIle Handing
import os
#.txt file
# r - read si no existe Error, w - Crea un archivo si no existe y escribe en el.
txt_file = open("my_file.txt", "w+", encoding="UTF-8", )
txt_file.write("Mi nombre es ALejandro\nMi apellido es Alonso\n32 Años\nMi lenguaje preferido es Python")
txt_file.write("\nAhora manejo git tambien")
txt_file.close()
txt_read = open("my_file.txt", "r+", encoding="UTF-8", )
#print(txt_file.read()) #Lee todo el documento
print(txt_read.readline())  #Lee linea por linea
print(txt_read.readline())
#print(txt_file.readline())
#print(txt_file.readline())

for line in txt_read:
    print(line)
txt_read.close()

#os.remove("my_file.txt")

#Tambien se puede declarar de la siguiente forma evitando tener que abrir y cerrar los archivos:

with open("my_file.txt", "a") as f:
    f.write("\nMe gusta el Pan")

#Lee la ultima linea del archivo
with open("my_file.txt", "r") as f:
    print(f.readlines()[-1])



#------------------------------------------------------------------------------------------------
#Trabajar con archivos JSON
import json
json_file = open("my_file.json", "w+")

json_text = {
    "Name":"Alejandro",
    "Surname":"Alonso",
    "Age":18,
    "web":"Alejandro.com" 
    }

#Dump escribe el dicionario en el archiuvo json 
#json.dump(json_text, json_file)
json.dump(json_text, json_file, indent=4)
json_file.close()

with open("my_file.json") as j:
    for line in j.readlines():
        print(line)

json_dict = json.load(open("my_file.json"))
print(json_dict)



#------------------------------------------------------------------------------------------------
#Trabajar con archivos CSV
import csv

csv_file = open("csv_file.csv", "w+", newline="")
csv_writer = csv.writer(csv_file)
#Add Data
data = ["name", "surname"]
csv_writer.writerow(data)
csv_writer.writerow(["Paco","Alonso"])
csv_writer.writerow(["Sergio","Masa"])

csv_file.close()

with open("csv_file.csv") as csv_file:
    for line in csv_file:
        print(line)



#------------------------------------------------------------------------------------------------
#Trabajar con archivos XML
import xml