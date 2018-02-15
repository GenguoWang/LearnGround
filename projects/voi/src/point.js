function Point(x,y) {
  this.x = x
  this.y = y
}
Point.prototype.add = function (p) {
  return new Point(this.x + p.x, this.y + p.y)
}
Point.prototype.minus = function (p) {
  return new Point(this.x - p.x, this.y - p.y)
}
Point.prototype.min = function (p) {
  return new Point(Math.min(this.x, p.x), Math.min(this.y, p.y))
}
Point.prototype.max = function (p) {
  return new Point(Math.max(this.x, p.x), Math.max(this.y, p.y))
}
Point.prototype.equals = function (p) {
  return this.x === p.x && this.y === p.y
}
Point.crossProduct = function (p1,p2,p3) {
  return (p2.x - p1.x) * (p3.y - p1.y) - (p2.y - p1.y) * (p3.x - p1.x)
}
Point.ZERO = new Point(0,0)

export default Point