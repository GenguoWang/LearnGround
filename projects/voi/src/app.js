import Shape from './shape'
import Game from './game'
import uuid from 'uuid'
import {createFromJson} from './level'
import Match from './match'

function getParameterByName(name, url) {
  if (!url) url = window.location.href;
  name = name.replace(/[\[\]]/g, "\\$&");
  var regex = new RegExp("[?&]" + name + "(=([^&#]*)|&|#|$)"),
      results = regex.exec(url);
  if (!results) return null;
  if (!results[2]) return '';
  return decodeURIComponent(results[2].replace(/\+/g, " "));
}

function getMe() {
  const fromLocal = localStorage.getItem("ME")
  if (fromLocal == null) {
    const me = uuid.v4()
    localStorage.setItem("ME", me)
    return me
  }
  return fromLocal
}

function getOpponent() {
  return getParameterByName("op")
}

class App {
  constructor() {
    this.currentLevel = 0
    this.addBtn = document.getElementById("add")
    this.addBtn.addEventListener("click", e=>{
      if (this.levels == null) {
        return
      }
      this.levels.push({
        initShapes:[],
        targetShapes:[]
      })
      this.currentLevel = this.levels.length - 1
      this.game.loadLevel(this.levels[this.currentLevel])
      this.game.edit()
    })

    fetch("levels.json").then(response => response.json()).then(levelString=>{
      this.levelsLoaded(createFromJson(levelString))
    })
  }
  levelsLoaded(levels) {
    this.levels = levels
    const bgCanvas = document.getElementById("bg")
    const canvas = document.getElementById("voi")
    const targetBgCanvas = document.getElementById("bgTarget")
    const targetCanvas = document.getElementById("voiTarget")
    const editCanvas = document.getElementById("editor")
    this.game = new Game(canvas, bgCanvas, targetCanvas, targetBgCanvas, editCanvas)
    this.game.delegate = this

    if (getParameterByName("g") != null) {
      // Match Mode
      this.match = new Match(getMe(), getOpponent())
      this.match.delegate = this
      console.log('match', this.match)
    } else {
      this.game.loadLevel(this.levels[this.currentLevel])
    }
  }

  // Match delegates
  matchStart() {
    console.log("match start")
    this.game.loadLevel(this.levels[this.currentLevel])
  }
  matchNextStage() {
    if (this.currentLevel < this.levels.length - 1) {
      this.currentLevel += 1
      this.game.loadLevel(this.levels[this.currentLevel])
    }
  }

  // Game delegates.
  onLevelEdit(initShapes, targetShapes) {
    this.levels[this.currentLevel] = {
      initShapes:initShapes.map(s=>new Shape(s.points, s.origin)),
      targetShapes:targetShapes.map(s=>new Shape(s.points, s.origin))
    }
    localStorage.setItem("LEVELS", JSON.stringify(this.levels))
  }
  puzzleSolved() {
    if (this.match) {
      this.match.meSolved()
    } else {
      this.matchNextStage()
    }
  }
}

export default App
