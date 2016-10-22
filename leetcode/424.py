class Solution(object):
    def characterReplacement(self, s, k):
      N = len(s)
      K = k
      d = [[0 for i in range(26)] for j in range(N+1)]
      for i in range(N):
        for j in range(26):
          d[i+1][j] = d[i][j]
        d[i+1][ord(s[i])-ord('A')] += 1
      l = min(N, max(d[N])+k)
      while l>0:
        gap = l
        for i in range(0,N-l+1):
          cur = [d[i+l][k]-d[i][k] for k in range(26)]
          maxNow = max(cur)
          if maxNow+K>=l:
            return l
          else:
            gap = min(gap, l-maxNow-K)
        l -= gap
      return 0
print Solution().characterReplacement("AABABBA", 1)
