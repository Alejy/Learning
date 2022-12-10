//Los modulos incluyen funcionalidades a js y se incluyen con requiered y el nombre del modulo
var http = require('http');

//El modulo http permite transferir datos utilizar el protocolo http 
//Creamos un objeto servidor que se encontrara en el puerto 8080, la funcion recibe como parametros req y res
http.createServer(function(req, res){
    res.writeHead(200, {'Content-Type': 'text/html'});  //Indica que el tipo de contenido sera html
    res.write('Hello World!');  //Indicamos el contenido que se va a devolver
    res.end();  //Terminamos el response
}).listen(8080);


//Ahora vamos a recuperar datos de la URL
http.createServer(function (req, res) {
    res.writeHead(200, {'Content-Type': 'text/html'});
    res.write(req.url); //Indicamos que el el texto incluido en la url lo reporte en HTML Por ejemplo (localhost:8081/Prueba)
    res.end();
}).listen(8081);    //Ahora utilizaremos el puerto 8081


//Importamos el modulo url que permite dividir la url en partes legibles
var url = require('url');
//Creamos un objeto servidor en el puerto 8082
//URL = http://localhost:8082/?year=2017&month=julio
http.createServer(function (req, res) {
  res.writeHead(200, {'Content-Type': 'text/html'});
  var q = url.parse(req.url, true).query;   //url.parse divide la url
  var txt = q.year + " " + q.month; //Recuperamos los parametros year y month
  res.end(txt);
}).listen(8082);

