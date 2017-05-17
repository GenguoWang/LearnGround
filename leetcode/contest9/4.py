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
          s = r[0]-1
          for j in range(1,i):
            s = s*10+r[j]
          cnt += s+1
        return cnt
      tmp = n
      cnt = 0
      pre = tmp
      while tmp > 0:
        cnt += 1
        pre = tmp
        tmp /= 10
      res = []
      def search(k,cnt,s):
        if k == 0:
          return
        p = (10**(cnt)-1)/9
        for i in range(s,10):
          if k > p:
            k -= p
          else:
            res.append(i)
            return search(k-1,cnt-1,0)
      off = calc(n)
      if k > off:
        k -= (n-10**(cnt-1)+1)
        search(k, cnt-1,1)
      else:
        search(k,cnt,1)
      f = 0
      for r in res:
        f = f*10+r
      return f

res = []
for i in range(1,224):
  r = Solution().findKthNumber(233,i)
  res.append((r,i))
res = sorted(res)
for r in res:
  print r
