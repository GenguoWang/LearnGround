class Solution(object):
  def findKthNumber(self, n, k):
    def calc(n):
      r = []
      while n>0:
        r.append(n%10)
        n /= 10
      r.reverse()
      cnt = 0
      for i in range(1,len(r)+1):
        s = r[0]
        for j in range(1,i):
          s *= r[j]+1
        cnt += s
      print cnt
      print r
    calc(n)
    return []
print Solution().findKthNumber(100,10)

