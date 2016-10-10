def isNum(c):
  return c >= '0' and c <= '9'
class F:
  def isI(self):
    return False
  def isF(self):
    return True
class I(F):
  def isI(self):
    return True
class U:
  def isF(self):
    return False
  def isI(self):
    return False
# start state
class SS(U):
  def __init__(self):
    self.m = True
  def work(self, c):
    if isNum(c):
      if c=='0':
        return ZS()
      else:
        return BS()
    elif c == '.':
      return SSS()
    elif (c == '-' or c=='+') and self.m:
      self.m = False
      return self
    else:
      return None
# start zero
class ZS(I): 
  def work(self, c):
    if isNum(c):
      return BS()
    elif c == '.':
      return PS()
    else:
      return None
# start point
class SSS(U):
  def work(self,c):
    if isNum(c):
        return PS()
    else:
      return None
# point
class PS(F):
  def work(self,c):
    if isNum(c):
      return self
    else:
      return None
# big number
class BS(I): 
  def work(self, c):
    if isNum(c):
      return self
    elif c == '.':
      return PS()
    else:
      return None
  
class Solution(object):
    def isNumber(self, s):
      s = s.strip()
      state = SS()
      print state.__class__.__name__
      f = True
      for i in s:
        if i == 'e':
          if f and state.isF():
            f = False
            state = SS()
          else:
            return False
        else:
          state = state.work(i)
          if state == None:
            return False
          print state.__class__.__name__
      if f:
        return state.isF()
      else:
        return state.isI()

trueList = ["+.8","-1.","-1e-1",".20","00", "0.","3.","0"," 0.1 ","2e10",".1",".0"]
falseList = ["6e6.5","--","abc","1 a","."]
for s in trueList:
  print Solution().isNumber(s)," ",s
  print float(s)
  assert(Solution().isNumber(s))
for s in falseList:
  print Solution().isNumber(s)," ",s
  try:
    print float(s)
    assert(False)
  except Exception,e:
    pass
  assert(not Solution().isNumber(s))
