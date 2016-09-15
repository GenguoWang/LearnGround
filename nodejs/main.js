var argv = require('yargs')
  .usage("Usage --l=[num] --b=[num]")
  .demand(['l', 'b'])
  .argv;

var rect = require('./rectangle');
console.log(rect().perimeter(argv.l,argv.b));
console.log("end");
