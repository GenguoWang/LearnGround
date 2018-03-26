function onSocket(socket) {
  const token = socket.handshake.query.token
  console.log("connect user");
  console.log(socket.handshake.query.token)
  socket.join(token, function(err){
    if(err) {
      console.log("err",err);
    }
  })
  socket.on('disconnect', function(){
    console.log("connect user disconnected");
  });
  socket.on('join',function(to) {
    console.log(to,'join');
    socket.to(to).emit('join',token);
  });
  socket.on('begin',function(to) {
    console.log(to,'begin');
    socket.to(to).emit('begin',token);
  });
  socket.on('solve',function(to) {
    console.log(to,'solve');
    socket.to(to).emit('solve',token);
  });
}
module.exports = onSocket;