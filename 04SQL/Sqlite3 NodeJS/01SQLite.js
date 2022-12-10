//Instalamos los paquetes para sqlite3 (npm install sqlite3)


//Importamos el modulo de sqlite    El metodo verbose reporta los errores ocurridos
const sqlite3 = require('sqlite3').verbose();

//Creamos el directorio Databases si no existe
var fs = require('fs');
if (!fs.existsSync('./Databases')){
    fs.mkdirSync('./Databases');
}

//Creamos la base de datos si no existe, nos conectamos a ella y controlamos si hay algun error que lo reporte por consola
const db = new sqlite3.Database('./Databases/01Database.db', err =>{
    if(err){
        return console.error(err.message);
    }else{
        console.log('Se ha realizado la conexion')
    }
})


//Creamos la tabla de la base de datos y controlamos los errores
//Tenemos que indicar que lo ejecute de forma asincrona ya que sino al ejecutar un insert todabia no existe la tabla
async function createDB(){
    var sql_sentence = "CREATE TABLE IF NOT EXISTS people(name text, surname text, age TINYINT, nick VARCHAR)"
    db.run(sql_sentence, err =>{
        if(err){
            return console.error(err.message);
        }else{
            console.log('Tabla creada')
        }
    })
}

//Insertamos una fila en la base de datos 
var sql_sentence = 'INSERT INTO people(name, surname, age, nick) values(?, ?, ?, ?)'
var person = ["Paco", "Martin", 18, "Paquito"]
db.run(sql_sentence, person, err =>{
    if(err){
        return console.error(err.message);
    }else{
        console.log('Se ha insertado los datos')
    }
})


