/*Para instalar paquetes en node podemos utilizar npm
Para instalar un modulo ejecutamos el siguiente comando en la terminal
-npm install upper-case
*/

var http = require('http')
//Este paquete convierte los textos en mayuscula
var uc = require('upper-case')

http.createServer(function (req, res) {
    res.writeHead(200, {'Content-Type': 'text/html'});
    res.write(uc.upperCase('Este texto se vera reflejado en mayusculas'));
    res.end();
  }).listen(8080);
