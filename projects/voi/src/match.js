import io from 'socket.io-client'

class Match {
  constructor(me, opponent) {
    this.opponent = opponent
    this.socket = io('http://10.0.0.123:3000?token=' + me)
    this.isHost = opponent == null
    if (!this.isHost) {
      this.socket.emit("join", opponent)
    }
    this.socket.on("join", this.opponentJoined.bind(this))
    this.socket.on("begin", this.hostBegin.bind(this))
    this.socket.on("solve", this.opponentSolved.bind(this))
  }
  opponentJoined(opponent) {
    console.log("match joined:", opponent)
    this.opponent = opponent
    this.socket.emit("begin", opponent)
    this.delegate && this.delegate.matchStart()
  }
  hostBegin() {
    console.log("match host begin")
    this.delegate && this.delegate.matchStart()
  }
  meSolved() {
    this.meFinished = true
    this.socket.emit("solve", this.opponent)
    this.mayNextStage()
  }
  opponentSolved() {
    this.opponentFinished = true
    this.mayNextStage()
  }
  mayNextStage() {
    if (this.meFinished && this.opponentFinished) {
      this.meFinished = false
      this.opponentFinished = false
      this.delegate && this.delegate.matchNextStage()
    }
  }
  timeout() {

  }
}

export default Match