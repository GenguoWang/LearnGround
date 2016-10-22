class Solution(object):
    def wordSquares(self, words):
      d = ([],{})
      N = len(words)
      if N == 0:
        return []
      M = len(words[0])
      for i in range(N):
        cur = d
        cur[0].append(i)
        for j in range(M):
          c = words[i][j]
          if c not in cur[1]:
            cur[1][c] = ([],{})
          cur = cur[1][c]
          cur[0].append(i)
      res = []
      def search(cur):
        n = len(cur)
        if n == M:
          res.append([words[i] for i in cur])
          return
        w = d
        for i in range(n):
          c = words[cur[i]][n]
          if c not in w[1]:
            return
          w = w[1][c]
        for i in w[0]:
          cur.append(i)
          search(cur)
          cur.pop()
      search([])
      return res
print Solution().wordSquares(["area","lead","wall","lady","ball"])
print Solution().wordSquares(["abat","baba","atan","atal"])
        
