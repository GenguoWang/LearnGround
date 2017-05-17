class Solution(object):
    def parseTernary(self, expression):
      def value(e,p):
        if len(e) == p:
          return (None,0)
        c = e[p]
        if c >= '0' and c <='9':
          return (c,1)
        if len(e) == p+1 or e[p+1] !='?':
          return (c,1)
        left,pl = value(e,2+p)
        right,pr = value(e,p+3+pl)
        if c == 'F':
          return (right,3+pl+pr)
        elif c == 'T':
          return (left,3+pl+pr)
        else:
          return (None,3+pl+pr)
      return value(expression,0)[0]
a = "F?1:T?4:5"
#print Solution().parseTernary(a)
a = "T?T?F:5:3"
print Solution().parseTernary(a)
a = "F?T?F:5:F?5:T?4:2"
print Solution().parseTernary(a)
