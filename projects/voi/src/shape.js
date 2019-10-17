import Point from './point'
function Shape(points, origin) {
  this.points = points
  if (origin) {
    this.origin = origin
  } else {
    this.origin = Point.ZERO
  }
}
Shape.prototype.getDrawPoint = function (index) {
  return this.points[index].add(this.origin)
}
Shape.prototype.draw = function (ctx) {
  ctx.beginPath()
  const startPoint = this.getDrawPoint(0)
  ctx.moveTo(startPoint.x, startPoint.y)
  for (let i = 1;i < this.points.length;++i) {
    const p = this.getDrawPoint(i)
    ctx.lineTo(p.x, p.y)
  }
  ctx.fill()
}
Shape.prototype.containsPoint = function (p) {
  const originPoint = p.minus(this.origin)
  let pFlag = true
  let nFlag = true
  const ps = this.points.concat([this.points[0]])
  for (let i = 0; i < ps.length - 1; ++i) {
    const v = Point.crossProduct(ps[i],ps[i + 1],originPoint)
    if (v > 0) {
      pFlag = false
    } else if (v < 0) {
      nFlag = false
    }
  }
  return pFlag || nFlag
}

export function makeSquare(size, origin, type) {
  const _origin = origin || Point.ZERO
  if (type === 1) {
    return new Shape([
      new Point(0,0),
      new Point(size,size),
      new Point(0,2 * size),
      new Point(-size,size),
    ], _origin)
  }
  return new Shape([
    new Point(0,0),
    new Point(0,size),
    new Point(size,size),
    new Point(size,0),
  ], _origin)
}

export default Shape