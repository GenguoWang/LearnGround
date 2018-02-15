import Game from './game'
import {LEVELS, createFromJson} from './level'

document.addEventListener("DOMContentLoaded", function () {
  const bgCanvas = document.getElementById("bg")
  const canvas = document.getElementById("voi")
  const targetBgCanvas = document.getElementById("bgTarget")
  const targetCanvas = document.getElementById("voiTarget")
  const editCanvas = document.getElementById("editor")
  const levelString = localStorage.getItem("LEVELS")
  fetch("levels.json").then(response => response.json())
  .then(levelString=>{
    const levels = createFromJson(levelString)
    const game = new Game(canvas, bgCanvas, targetCanvas, targetBgCanvas, levels, editCanvas)
  })
})














