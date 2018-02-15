import Board from './board'
import Shape from './shape'
import Point from './point'
import Editor from './editor'
import {calculate, match} from './render'

function getCorners(shapes) {
  let leftTopX = 1000, leftTopY = 1000, rightBottomX = 0, rightBottomY = 0
  shapes.forEach(shape => {
    shape.points.forEach(op => {
      const p = op.add(shape.origin)
      leftTopX = Math.min(p.x, leftTopX)
      leftTopY = Math.min(p.y, leftTopY)
      rightBottomX = Math.max(p.x, rightBottomX)
      rightBottomY = Math.max(p.y, rightBottomY)
    })
  })
  return [new Point(leftTopX, leftTopY), new Point(rightBottomX, rightBottomY)]
}

function getMatric(shapes) {
  const corners = getCorners(shapes)
  let i = 0,j = 0
  let matric = []
  let blackCnt = 0
  let leftTopX = 1000, leftTopY = 1000, rightBottomX = 0, rightBottomY = 0
  for (let fj = corners[0].y; fj <= corners[1].y; fj += 0.1) {
    matric[i] = []
    j = 0
    for (let fi = corners[0].x; fi <= corners[1].x;fi += 0.1) {
      let c = 0
      shapes.forEach(shape=>{
        if (shape.containsPoint(new Point(fi,fj))) {
          c += 1
        }
      })
      const isBlack = c % 2
      matric[i][j] = isBlack
      blackCnt += isBlack
      if (isBlack) {
        leftTopX = Math.min(j, leftTopX)
        leftTopY = Math.min(i, leftTopY)
        rightBottomX = Math.max(j, rightBottomX)
        rightBottomY = Math.max(i, rightBottomY)
      }
      j++
    }
    i++
  }
  return {
    data:matric,
    blackCnt:blackCnt,
    corners:[new Point(leftTopX, leftTopY), new Point(rightBottomX, rightBottomY)]
  }
}

class Game {
  constructor(canvas, bgCanvas, targetCanvas, targetBgCanvas,levels,editCanvas) {
    const size = 15
    canvas.width = canvas.clientWidth
    canvas.height = canvas.clientHeight
    bgCanvas.width = bgCanvas.clientWidth
    bgCanvas.height = bgCanvas.clientHeight
    targetCanvas.width = targetCanvas.clientWidth
    targetCanvas.height = targetCanvas.clientHeight
    targetBgCanvas.width = targetBgCanvas.clientWidth
    targetBgCanvas.height = targetBgCanvas.clientHeight
    editCanvas.width = editCanvas.clientWidth
    editCanvas.height = editCanvas.clientHeight
    console.log(canvas.clientWidth)
    console.log(targetCanvas.clientWidth)
    this.workBoard = new Board(canvas, bgCanvas,size,size,(canvas.clientWidth - 1) / size)
    this.workBoard.isMatching = this.isMatching.bind(this)
    this.editor = new Editor(editCanvas, editCanvas.clientWidth / size)
    this.editor.addShape = this.addShape.bind(this)
    this.editor.hide()
    this.isEditing = false
    const targetSize = 12
    this.targetBoard = new Board(targetCanvas, targetBgCanvas,targetSize,targetSize,(targetCanvas.clientWidth - 1) / targetSize, true)
    this.levels = levels
    this.currentLevel = 0
    this.loadLevel()

    this.editBtn = document.getElementById("edit")
    this.editBtn.addEventListener("click",e=>{
      console.log("eeee")
      if (this.isEditing) {
        this.stopEdit()
      } else {
        this.edit()
      }
    })
    this.clearBtn = document.getElementById("clear")
    this.clearBtn.style.display = "none"
    this.clearBtn.addEventListener("click",e=>{
      this.targetBoard.loadShapes([])
      this.workBoard.loadShapes([])
    })
    this.addBtn = document.getElementById("add")
    this.addBtn.addEventListener("click", e=>{
      this.levels.push({
        initShapes:[],
        targetShapes:[]
      })
      this.currentLevel = this.levels.length - 1
      this.loadLevel()
      this.edit()
    })
  }
  stopEdit() {
    this.isEditing = false
    this.editor.hide()
    this.editBtn.textContent = "Edit"
    this.clearBtn.style.display = "none"
    this.targetBoard.invalid = true
    this.targetMatric = getMatric(this.targetBoard.shapes)
    this.levels[this.currentLevel] = {
      initShapes:this.workBoard.shapes.map(s=>new Shape(s.points, s.origin)),
      targetShapes:this.targetBoard.shapes.map(s=>new Shape(s.points, s.origin))
    }
    localStorage.setItem("LEVELS", JSON.stringify(this.levels))
  }
  edit() {
    this.isEditing = true
    this.editor.show()
    this.editBtn.textContent = "Done"
    this.clearBtn.style.display = "inline"
    this.targetBoard.invalid = false
  }
  loadLevel() {
    const level = this.levels[this.currentLevel]
    this.workBoard.loadShapes(level.initShapes)
    this.targetBoard.loadShapes(level.targetShapes)
    this.targetMatric = getMatric(level.targetShapes)
    console.log(this.targetMatric)
  }
  addShape(shape) {
    this.workBoard.addShape(new Shape(shape.points,shape.origin))
    this.targetBoard.addShape(new Shape(shape.points, shape.origin))
  }
  isMatching() {
    const f1 = calculate(this.targetBoard.shapes)
    const f2 = calculate(this.workBoard.shapes)
    if (match(f1,f2)) {
      console.log("Match!")
      if (this.currentLevel < this.levels.length - 1) {
        this.currentLevel += 1
        this.loadLevel()
      }
    }
    /*
    const matric = getMatric(this.workBoard.shapes)
    const targetMatric = this.targetMatric
    const ratio = matric.blackCnt / targetMatric.blackCnt
    console.log(matric)
    if (ratio > 0.9 && ratio < 1.1) {
      const lx = Math.min(matric.corners[1].x - matric.corners[0].x,
        targetMatric.corners[1].x - targetMatric.corners[0].x)
      const ly = Math.min(matric.corners[1].y - matric.corners[0].y,
        targetMatric.corners[1].y - targetMatric.corners[0].y)
      let cnt = 0
      for (let dx = 0; dx < lx;++dx) {
        for (let dy = 0; dy < ly;++dy) {
          if (matric.data[dy + matric.corners[0].y][dx + matric.corners[0].x] !==
            targetMatric.data[dy + targetMatric.corners[0].y][dx + targetMatric.corners[0].x]) {
            cnt++
          }
        }
      }
      if (cnt / targetMatric.blackCnt < 0.1) {
        console.log("Match! "+cnt+"/"+targetMatric.blackCnt)
        if (this.currentLevel < this.levels.length - 1) {
          this.currentLevel += 1
          this.loadLevel()
        }
      } else {
        console.log("unMatch "+cnt+"/"+targetMatric.blackCnt)
      }
    }
    */
  }
}

export default Game