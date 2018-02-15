import Point from './point'
import Shape from './shape'

class Editor {
  constructor(canvas, ratio) {
    this.canvas = canvas
    this.ctx = canvas.getContext("2d")
    this.ratio = ratio || 20
    canvas.addEventListener("mouseup",this.mouseup.bind(this))
    canvas.addEventListener("mousemove",this.mousemove.bind(this))
    this.points = []
    this.currentPoint = null
  }

  getPointFromMouseEvent(e) {
    return new Point(e.offsetX / this.ratio, e.offsetY / this.ratio)
  }

  mouseup(e) {
    const tmpP = this.getPointFromMouseEvent(e)
    const p = new Point(Math.round(tmpP.x),Math.round(tmpP.y))
    if (this.points.length > 0 && this.points[0].equals(p)) {
      this.addShape && this.addShape(new Shape(this.points))
      this.points = []
    } else {
      this.points.push(p)
    }
    this.render()
  }

  mousemove(e) {
    this.currentPoint = this.getPointFromMouseEvent(e)
    this.render()
  }

  render() {
    const ctx = this.ctx
    ctx.clearRect(0, 0, this.canvas.width, this.canvas.height)
    ctx.fillStyle = "#000000"
    ctx.save()
    ctx.lineWidth = 2
    if (this.points.length > 0) {
      ctx.beginPath()
      ctx.moveTo(this.points[0].x * this.ratio,this.points[0].y * this.ratio)
      for (let i = 1; i < this.points.length;++i) {
        ctx.lineTo(this.points[i].x * this.ratio,this.points[i].y * this.ratio)
      }
      if (this.currentPoint) {
        ctx.lineTo(this.currentPoint.x * this.ratio,this.currentPoint.y * this.ratio)
      }
      ctx.stroke()
    }
    ctx.restore()
  }

  hide() {
    this.canvas.style.display = "none"
    this.points = []
  }
  show() {
    this.canvas.style.display = "block"
  }
}

export default Editor