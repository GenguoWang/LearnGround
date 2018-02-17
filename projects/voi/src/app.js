import Shape from './shape'
import Game from './game'
import {createFromJson} from './level'

class App {
  constructor() {
    this.currentLevel = 0
    this.addBtn = document.getElementById("add")
    this.addBtn.addEventListener("click", e=>{
      this.levels.push({
        initShapes:[],
        targetShapes:[]
      })
      this.currentLevel = this.levels.length - 1
      this.game.loadLevel(this.levels[this.currentLevel])
      this.game.edit()
    })

    const bgCanvas = document.getElementById("bg")
    const canvas = document.getElementById("voi")
    const targetBgCanvas = document.getElementById("bgTarget")
    const targetCanvas = document.getElementById("voiTarget")
    const editCanvas = document.getElementById("editor")
    fetch("levels.json").then(response => response.json()).then(levelString=>{
      this.levels = createFromJson(levelString)
      this.game = new Game(canvas, bgCanvas, targetCanvas, targetBgCanvas, editCanvas)
      this.game.delegate = this
      this.game.loadLevel(this.levels[this.currentLevel])
    })
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
    if (this.currentLevel < this.levels.length - 1) {
      this.currentLevel += 1
      this.game.loadLevel(this.levels[this.currentLevel])
    }
  }
}

export default App
