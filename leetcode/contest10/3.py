class Solution(object):
    def arrangeCoins(self, n):
      if n<=0:
        return 0
      i = 0
      j = n
      m = 0
      n = n*2
      while i <=j:
        m = (i+j)/2
        r = m*(1+m)
        if r > n:
          j = m-1
        elif r < n:
          i = m+1
        else:
          return m
      r = m*(1+m)
      if r > n:
        return m-1
      else:
        return m
for i in range(0,11):
  print i,Solution().arrangeCoins(i)
