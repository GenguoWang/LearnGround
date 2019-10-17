import Point from './point'
import Shape from './shape'
//import {render} from './render'

class Board {
  constructor(context, bgCanvas, width, height, ratio, invalid) {
    this.width = width || 40
    this.height = height || 40
    this.ratio = ratio || 10
    this.context = context
    this.drawBackground()
    this.context.globalCompositeOperation = 'xor'
    this.then = 0
    this.interval = 1000 / 10
    this.isDrawing = false
    /*
    this.canvas = canvas
    this.bgCanvas = bgCanvas
    this.ctx = ctx

    // Init states
    this.shapes = []
    this.isMouseDown = false
    this.startPoint = null
    this.currentShape = null
    this.render()

    this.invalid = invalid
    */
  }

  loadShapes(shapes) {
    this.shapes = shapes.map(s=>new Shape(s.points, s.origin))
    this.isMouseDown = false
    this.startPoint = null
    this.currentShape = null
    this.render()
  }

  addShape(shape) {
    this.shapes.push(new Shape(shape.points, shape.origin))
    this.isMouseDown = false
    this.startPoint = null
    this.currentShape = null
    this.render()
  }

  render() {
    if (this.isDrawing) {
      return
    }
    this.isDrawing = true
    const now = Date.now()
    if (now - this.then < this.interval) {
      console.log("ggg")
      //return
    }
    this.then = now
    this.drawBackground()
    const ctx = this.context
    ctx.fillStyle = '#000000'
    ctx.save()
    ctx.scale(this.ratio, this.ratio)
    //if (this.isMouseDown) {
    this.shapes.forEach(function (shape) {
      if (shape === this.currentShape) {
        ctx.save()
        shape.draw(ctx)
        ctx.restore()
      } else {
        shape.draw(ctx)
      }
    }, this)
    //} else {
    //  render(this.shapes, this.ctx)
    //}
    ctx.restore()
    console.log("draw")
    ctx.draw(false, ()=>{console.log('back'); this.isDrawing = false;})
  }

  mousedown(e) {
    e.preventDefault && e.preventDefault()
    if (this.invalid) {
      return
    }
    const touchPoint = this.getPointFromMouseEvent(e)
    this.currentShape = null
    for (let i = 0; i < this.shapes.length; ++i) {
      if (this.shapes[i].containsPoint(touchPoint)) {
        // Move the target shape to the top.
        const tmp = this.shapes[0]
        this.shapes[0] = this.shapes[i]
        this.shapes[i] = tmp
        this.currentShape = this.shapes[0]
        this.startPoint = this.currentShape.origin.minus(touchPoint)
        break
      }
    }
    this.isMouseDown = true
  }

  mouseup(e) {
    e.preventDefault && e.preventDefault()
    if (this.invalid) {
      return
    }
    if (this.isMouseDown && this.currentShape) {
      this.isMouseDown = false
      this.currentShape.origin =
        new Point(Math.round(this.currentShape.origin.x), Math.round(this.currentShape.origin.y))
      this.render()
      this.isMatching && this.isMatching()
    }
    this.isMouseDown = false
    this.currentShape = null
  }

  mousemove(e) {
    e.preventDefault && e.preventDefault()
    if (this.invalid) {
      return
    }
    if (this.isMouseDown && this.currentShape) {
      const nowPoint = this.getPointFromMouseEvent(e)
      this.currentShape.origin = this.startPoint.add(nowPoint)
      this.render()
    }
  }

  getPointFromMouseEvent(e) {
    if (e.changedTouches) {
      // Wechat small program
      return new Point(e.changedTouches[0].x / this.ratio, e.changedTouches[0].y / this.ratio)
    }
    if (e.touches) {
      const rect = this.canvas.getBoundingClientRect()
      return new Point((e.touches[0].clientX - rect.left) / this.ratio
        ,(e.touches[0].clientY - rect.top) / this.ratio)
    }
    return new Point(e.offsetX / this.ratio, e.offsetY / this.ratio)
  }
  drawBackground() {
    const bgCtx = this.context
    bgCtx.fillStyle = '#ff0000'
    for (let i = 0; i <= this.width; i++) {
      for (let j = 0; j <= this.height; j++) {
        bgCtx.fillRect(i * this.ratio,j * this.ratio,1,1)
      }
    }
  }
}

export default Board
