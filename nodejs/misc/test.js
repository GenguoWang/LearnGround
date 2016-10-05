var p = new global.Promise(function(resolve, reject){
  setTimeout(function(){
    resolve("wgg");
  }, 1000);
});
p.then(function(res){
  console.log(res+"wgg"+wgg);
  var p = new global.Promise(function(resolve, reject){
    setTimeout(function(){
      resolve("sec wgg");
    }, 1000);
  });
  return p;
}, function(err){
  console.log("ano "+err);
  return "wgg ano";
}).then(function(res){
  console.log("2 "+res);
}).catch(function(err){
  console.log("cat:"+err);
});
