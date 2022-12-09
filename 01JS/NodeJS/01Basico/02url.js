var url = require('url');
var adrress = 'http://localhost:8080/default.htm?name=Alejandro&surname=Alonso'
var p = url.parse(adrress, true);

/*Selecciona cada una de las partes de la peticion
Url {
  protocol: 'http:',
  slashes: true,
  auth: null,
  host: 'localhost:8080',
  port: '8080',
  hostname: 'localhost',
  hash: null,
  search: '?name=Alejandro&surname=Alonso',
  query: [Object: null prototype] { name: 'Alejandro', surname: 'Alonso' },
  pathname: '/default.htm',
  path: '/default.htm?name=Alejandro&surname=Alonso',
  href: 'http://localhost:8080/default.htm?name=Alejandro&surname=Alonso'
}
*/
console.log(adrress);
console.log(p);
console.log(p.host);
console.log(p.pathname);
console.log(p.search);
console.log(p.query);
console.log(p.query.name);