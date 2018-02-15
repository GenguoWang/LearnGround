import Point from './point'
import Shape from './shape'
import {render} from './render'

class Board {
  constructor(canvas, bgCanvas, width, height, ratio, invalid) {
    this.width = width || 40
    this.height = height || 40
    this.ratio = ratio || 10
    this.canvas = canvas
    this.bgCanvas = bgCanvas
    this.drawBackground()
    this.ctx = canvas.getContext("2d")
    this.ctx.globalCompositeOperation = "xor"

    // Init states
    this.shapes = []
    this.isMouseDown = false
    this.startPoint = null
    this.currentShape = null
    this.render()

    canvas.addEventListener("mousedown",this.mousedown.bind(this))
    canvas.addEventListener("touchstart",this.mousedown.bind(this))
    canvas.addEventListener("mouseup",this.mouseup.bind(this))
    canvas.addEventListener("touchend",this.mouseup.bind(this))
    canvas.addEventListener("mousemove",this.mousemove.bind(this))
    canvas.addEventListener("touchmove",this.mousemove.bind(this))
    this.invalid = invalid
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
    const ctx = this.ctx
    ctx.clearRect(0, 0, this.canvas.width, this.canvas.height)
    ctx.fillStyle = "#000000"
    ctx.save()
    ctx.scale(this.ratio, this.ratio)
    if(this.isMouseDown) {
      this.shapes.forEach(function (shape) {
        if (shape === this.currentShape) {
          ctx.save()
          ctx.translate(this.currentOffset.x, this.currentOffset.y)
          shape.draw(ctx)
          ctx.restore()
        } else {
          shape.draw(ctx)
        }
      }, this)
    } else {
      render(this.shapes, this.ctx)
    }
    ctx.restore()
  }

  mousedown(e) {
    e.preventDefault()
    if (this.invalid) {
      return
    }
    this.startPoint = this.getPointFromMouseEvent(e)
    this.currentShape = null
    for (let i = 0; i < this.shapes.length; ++i) {
      if (this.shapes[i].containsPoint(this.startPoint)) {
        // Move the target shape to the top.
        const tmp = this.shapes[0]
        this.shapes[0] = this.shapes[i]
        this.shapes[i] = tmp
        this.currentShape = this.shapes[0]
        break
      }
    }
    this.isMouseDown = true
  }

  mouseup(e) {
    e.preventDefault()
    if (this.invalid) {
      return
    }
    if (this.isMouseDown && this.currentShape) {
      this.isMouseDown = false
      this.currentShape.origin = this.currentShape.origin.add(this.currentOffset)
      this.currentShape.origin =
        new Point(Math.round(this.currentShape.origin.x), Math.round(this.currentShape.origin.y))
      this.currentOffset = Point.ZERO
      this.render()
      this.isMatching && this.isMatching()
    }
    this.isMouseDown = false
    this.currentShape = null
  }

  mousemove(e) {
    e.preventDefault()
    if (this.invalid) {
      return
    }
    if (this.isMouseDown && this.currentShape) {
      const nowPoint = this.getPointFromMouseEvent(e)
      this.currentOffset = nowPoint.minus(this.startPoint)
      this.render()
    }
  }

  getPointFromMouseEvent(e) {
    if (e.touches) {
      return new Point((e.touches[0].clientX - this.canvas.offsetLeft) / this.ratio
      ,(e.touches[0].clientY - this.canvas.offsetTop) / this.ratio)
    }
    return new Point(e.offsetX / this.ratio, e.offsetY / this.ratio)
  }
  drawBackground() {
    const bgCtx = this.bgCanvas.getContext("2d")
    bgCtx.fillStyle = "#ff0000"
    for (let i = 0; i <= this.width; i++) {
      for (let j = 0; j <= this.height; j++) {
        bgCtx.fillRect(i * this.ratio,j * this.ratio,1,1)
      }
    }
  }
}

export default Board