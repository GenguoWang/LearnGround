/******/ (function(modules) { // webpackBootstrap
/******/ 	// The module cache
/******/ 	var installedModules = {};

/******/ 	// The require function
/******/ 	function __webpack_require__(moduleId) {

/******/ 		// Check if module is in cache
/******/ 		if(installedModules[moduleId])
/******/ 			return installedModules[moduleId].exports;

/******/ 		// Create a new module (and put it into the cache)
/******/ 		var module = installedModules[moduleId] = {
/******/ 			exports: {},
/******/ 			id: moduleId,
/******/ 			loaded: false
/******/ 		};

/******/ 		// Execute the module function
/******/ 		modules[moduleId].call(module.exports, module, module.exports, __webpack_require__);

/******/ 		// Flag the module as loaded
/******/ 		module.loaded = true;

/******/ 		// Return the exports of the module
/******/ 		return module.exports;
/******/ 	}


/******/ 	// expose the modules object (__webpack_modules__)
/******/ 	__webpack_require__.m = modules;

/******/ 	// expose the module cache
/******/ 	__webpack_require__.c = installedModules;

/******/ 	// __webpack_public_path__
/******/ 	__webpack_require__.p = "";

/******/ 	// Load entry module and return exports
/******/ 	return __webpack_require__(0);
/******/ })
/************************************************************************/
/******/ ([
/* 0 */
/***/ function(module, exports, __webpack_require__) {

	'use strict';

	var _cats = __webpack_require__(1);

	var _cats2 = _interopRequireDefault(_cats);

	function _interopRequireDefault(obj) { return obj && obj.__esModule ? obj : { default: obj }; }

	//import $ from 'jquery';
	//$ = require('jquery');

	//$('<h1>Cats</h1>').appendTo('body');
	//const ul = $('<ul></ul>').appendTo('body');
	var _iteratorNormalCompletion = true; //cats = require('./cats.js');
	//console.log(cats);
	//import 'babel-polyfill';

	var _didIteratorError = false;
	var _iteratorError = undefined;

	try {
	   for (var _iterator = _cats2.default[Symbol.iterator](), _step; !(_iteratorNormalCompletion = (_step = _iterator.next()).done); _iteratorNormalCompletion = true) {
	      var cat = _step.value;

	      //$('<li></li>').text(cat).appendTo(ul);
	      console.log(cat);
	   }
	} catch (err) {
	   _didIteratorError = true;
	   _iteratorError = err;
	} finally {
	   try {
	      if (!_iteratorNormalCompletion && _iterator.return) {
	         _iterator.return();
	      }
	   } finally {
	      if (_didIteratorError) {
	         throw _iteratorError;
	      }
	   }
	}

/***/ },
/* 1 */
/***/ function(module, exports) {

	'use strict';

	var cats = ['dave', 'henry', 'martha'];
	module.exports = cats;

/***/ }
/******/ ]);