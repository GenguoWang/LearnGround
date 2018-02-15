import * as turf from '@turf/turf'
console.log("wgg")
console.log(turf)

function toTurfPolygon(shape) {
  const points = shape.points.map(p=>[p.x+shape.origin.x,p.y+shape.origin.y]).concat([[shape.points[0].x+shape.origin.x,shape.points[0].y+shape.origin.y]])
  return turf.polygon([ points ])
}

function drawPoints(points, ctx) {
  ctx.beginPath()
  const startPoint = points[0]
  ctx.moveTo(startPoint[0], startPoint[1])
  for (let i = 1;i < points.length;++i) {
    ctx.lineTo(points[i][0], points[i][1])
  }
  ctx.fill()
}

export function calculate(shapes) {
  if (shapes.length <= 1) {
    return null
  }
  const polygons = shapes.map(s=>toTurfPolygon(s))
  let result = [polygons[0]]
  let tmpResult = []
  for (let i = 1; i < polygons.length; ++i) {
    let leftOver = polygons[i]
    result.forEach(old=>{
      if (leftOver) {
        const d = turf.difference(old, leftOver)
        leftOver = turf.difference(leftOver, old)
        if (d) {
          tmpResult.push(d)
        }
      } else {
        tmpResult.push(old)
      }
    })
    if (leftOver) {
      tmpResult.push(leftOver)
    }
    result = tmpResult
    tmpResult = []
  }
  console.log(polygons)
  console.log("result")
  console.log(result)
  const fc = turf.featureCollection(result)
  const combinedResult = turf.combine(fc)
  console.log(combinedResult)
  if (combinedResult.features.length > 1) {
    alert("combined error")
  }
  if (combinedResult.features.length === 1) {
    return combinedResult.features[0]
  }
  return null
}

export function render(shapes,ctx) {
  const r = calculate(shapes)
  console.log("r",r)
  if (r) {
    if (r.geometry.type === "MultiPolygon") {
      console.log("draw")
      r.geometry.coordinates.forEach(points=>drawPoints(points[0], ctx))
    } else if (r.geometry.type === "Polygon") {
      drawPoints(r.geometry.coordinates[0],ctx)
    }
  }
}

function translate(f,x,y) {
    if (f.geometry.type === "MultiPolygon") {
      f.geometry.coordinates.forEach(points=> {
        points[0].forEach(p=>{
          p[0]+=x
          p[1]+=y
        })
      })
    } else if (f.geometry.type === "Polygon") {
      f.geometry.coordinates[0].forEach(p=>{
          p[0]+=x
          p[1]+=y
      })
    }
}

export function match(f1, f2) {
  const bbox1 = turf.bbox(f1)
  const bbox2 = turf.bbox(f2)
  console.log(f1)
  console.log(f2)
  console.log(bbox1)
  console.log(bbox2)
  if (bbox1[2]-bbox1[0] !== bbox2[2]-bbox2[0]
    || bbox1[3]-bbox1[1] !== bbox2[3]-bbox2[1]) {
    return false
  }
  translate(f1, -bbox1[0], -bbox1[1])
  translate(f2, -bbox2[0], -bbox2[1])
  console.log(f1)
  console.log(f2)
  console.log(turf.area(f2))
  const d1 = turf.difference(f1, f2)
  const d2 = turf.difference(f2, f1)
  console.log(d1)
  console.log(d2)
  return (d1 === null || turf.area(d1) < 100) && (d2 === null || turf.area(d2) < 100)
}