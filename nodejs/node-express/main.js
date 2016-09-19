var express = require('express');
var morgan = require('morgan');
var hostname = 'localhost'
var port = 3000
var app = express();
// the order of use is the order app handle the request. If it's handled, it will not use the next component.
app.use(morgan('dev'));
app.use(express.static(__dirname+'/public'));
app.use(function(req, res, next) {
  res.writeHead(200, {'Content-Type': 'text/html'});
  res.end('<html><body><h1>Hello World</h1></body></html>');
});

app.listen(port, hostname, function(){
  console.log(`Server running at ${hostname}:${port}`);
});
