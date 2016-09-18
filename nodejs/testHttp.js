var http = require('http')
var server = http.createServer(function(res,res){
  res.write("hello world");
  res.end("<html><body>hello world</body></html>");
});
server.listen(8000);

