var http = require('http');
var fs = require('fs');
var path = require('path');

var hostname = 'localhost';
var port = 3000;

var server = http.createServer(function(req, res){
  console.log(req.headers);
  console.log('Request for ' + req.url + ' by method ' + req.method);
  if (req.method == 'GET') {
    var fileUrl;
    if (req.url == '/') fileUrl = '/index.html';
    else fileUrl = req.url;
    
    var filePath = path.resolve('./public' + fileUrl);
    var fileExt = path.extname(filePath);
    if (fileExt == '.html') {
      fs.exists(filePath, function(exists) {
        if(!exists) {
          res.writeHead(404, { 'Content-Type': 'text/html' });
          res.end("no file");
          return;
        } else {
          res.writeHead(200, { 'Content-Type': 'text/html' });
          fs.createReadStream(filePath).pipe(res);
          return;
        }
      });
    } else {
      res.writeHead(404, { 'Content-Type': 'text/html' });
      res.end("no html");
      return;
    }
  } else {
    res.writeHead(404, { 'Content-Type': 'text/html' });
    res.end("no method");
    return;
  }

});

server.listen(port, hostname, function (){
  console.log(`Server running at http://${hostname}:${port}/`);
});
