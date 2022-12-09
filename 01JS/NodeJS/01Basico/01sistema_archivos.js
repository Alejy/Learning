var http = require('http')
//Importamos el modulo de sistemas de archivos
var fs = require('fs');

http.createServer(function (req, res) {
    fs.readFile('files/01file.html', function(err, data) { //Leemos el archivo html y recuperamos la data para reportarlo en el puerto 8080
      res.writeHead(200, {'Content-Type': 'text/html'});
      res.write(data);
      return res.end();
    });
  }).listen(8080);

//Ahora vamos a crear un archivo txt y controlamos los errores
fs.appendFile('files/01file.txt', 'Learning NodeJS', function (err) {
    if (err) throw err;
    console.log('01file.txt Created');
});


//Creamos un archivo con el metodo open y lo abre
/*
fs.open('files/01file.txt', 'w', function (err, file) {
    if (err) throw err;
    console.log('Saved!');
});
*/

//Escribimos una linea en el archivo
fs.writeFile('files/01file.txt', 'Una linea nueva', function (err) {
    if (err) throw err;
    console.log('Saved!');
  });

//Añadimos una linea al final del archivo
fs.appendFile('files/01file.txt', 'appendFile', function (err) {
    if (err) throw err;
    console.log('Updated!');
});

//Reemplaza el contenido del archivo
/*
fs.writeFile('files/01file.txt', 'Contenido reemplazado', function (err) {
  if (err) throw err;
  console.log('Replaced!');
});
*/


//Reportamos la data del archivo txt a traves del puerto 8081
http.createServer(function (req, res) {
    fs.readFile('files/01file.txt', function(err, data) { //Leemos el archivo html y recuperamos la data para reportarlo en el puerto 8080
        res.writeHead(200, {'Content-Type': 'text/html'});
        res.write(data);
        return res.end();
    });
}).listen(8081);



//Borrar archivo
/*
fs.unlink('files/01file.txt', function (err) {
    if (err) throw err;
    console.log('Deleted');
  });
*/

//Renombrar archivos
/*
fs.rename('mynewfile1.txt', 'myrenamedfile.txt', function (err) {
    if (err) throw err;
    console.log('File Renamed!');
  });
*/
