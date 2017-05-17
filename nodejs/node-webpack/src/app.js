//cats = require('./cats.js');
//console.log(cats);
//import 'babel-polyfill';
import cats from './cats';
//import $ from 'jquery';
//$ = require('jquery');

//$('<h1>Cats</h1>').appendTo('body');
//const ul = $('<ul></ul>').appendTo('body');
for (const cat of cats) {
   //$('<li></li>').text(cat).appendTo(ul);
   console.log(cat);
}
