import Game from './game'
import {createFromJson} from './level'
import 'promise-polyfill'
import 'whatwg-fetch'

document.addEventListener("DOMContentLoaded", function () {
  const bgCanvas = document.getElementById("bg")
  const canvas = document.getElementById("voi")
  const targetBgCanvas = document.getElementById("bgTarget")
  const targetCanvas = document.getElementById("voiTarget")
  const editCanvas = document.getElementById("editor")
  fetch("levels.json").then(response => response.json())
  .then(levelString=>{
    const levels = createFromJson(levelString)
    new Game(canvas, bgCanvas, targetCanvas, targetBgCanvas, levels, editCanvas)
  })
})














