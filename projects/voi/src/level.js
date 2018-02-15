import Shape, {makeSquare} from './shape'
import Point from './point'

const L1 = {
  initShapes:[
    makeSquare(4,new Point(6,6)),
    makeSquare(2,new Point(8,12),1),
  ],
  targetShapes:[
    makeSquare(4,new Point(5,5)),
    makeSquare(2,new Point(7,5),1),
  ]
}

const L2 = {
  initShapes:[
    makeSquare(4,new Point(1,4)),
    makeSquare(4,new Point(15,4)),
    makeSquare(4,new Point(8,10)),
  ],
  targetShapes:[
    makeSquare(4,new Point(5,5)),
    makeSquare(4,new Point(6,6)),
    makeSquare(4,new Point(4,4)),
  ]
}

export function createFromJson(data) {
  return data.map(item=>{
    return {
      initShapes:item.initShapes.map(s=>new Shape(
        s.points.map(p=>new Point(p.x,p.y)),
        new Point(s.origin.x, s.origin.y))),
      targetShapes:item.targetShapes.map(s=>new Shape(
        s.points.map(p=>new Point(p.x,p.y)),
        new Point(s.origin.x, s.origin.y))),
    }
  })
}
export const LEVELS = [L2, L1]