var convert = require('xml-js');
var md5 = require('md5')
var xml =
  '<?xml version="1.0" encoding="utf-8"?>' +
  '<note importance="high" logged="true">' +
  '    <title>Happy</title>' +
  '    <todo>Work</todo>' +
  '    <todo>Play</todo>' +
  '</note>';
var result1 = aaddfawfconvert.xml2json(xml, {compact: true, spaces: 4});
var result2 = convert.xml2json(xml, {compact: false, spaces: 4});
console.log(result1, '\n', result2);

var js = {
  node:{
    ag:'123',aaa
    bd:'test',
    cd:123
  }
}

console.log('wgg')
console.log(convert.js2xml(js, {compact: true}))

let data = {
  a:1,
  b:2
}


console.log(Object.keys(data).sort().map(k=>`${k}=${data[k]}`).join('&'))
console.log(md5('abc'))
