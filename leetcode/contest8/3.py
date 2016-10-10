class Solution(object):
    def search(self,q,p,vp):
      d1 = [1,-1,0,0]
      d2 = [0,0,1,-1]
      matrix = self.matrix
      while len(q) > 0:
        t = q.pop()
        x = t[0]
        y = t[1]
        for i in range(0,4):
          xx = x+d1[i]
          yy = y+d2[i]
          if xx >=0 and yy >=0 and xx<self.m and yy<self.n:
            if (not vp[xx][yy]) and matrix[xx][yy]>=matrix[x][y]:
              p[xx][yy] = True
              vp[xx][yy] = True
              q.append((xx,yy))

    def pacificAtlantic(self, matrix):
      m = len(matrix)
      if m == 0:
        return []
      n = len(matrix[0])
      if n == 0:
        return []
      p = [[False for i in range(0,n)] for j in range(0,m)]
      a = [[False for i in range(0,n)] for j in range(0,m)]
      vp = [[False for i in range(0,n)] for j in range(0,m)]
      va = [[False for i in range(0,n)] for j in range(0,m)]
      self.matrix = matrix
      self.m = m
      self.n = n 
      q =[]
      qa = []
      for i in range(0,m):
        q.append((i,0))
        p[i][0] = True
        vp[i][0] = True
        qa.append((i,n-1))
        a[i][n-1] = True
        va[i][n-1] = True
      for j in range(0,n):
        q.append((0,j))
        p[0][j] = True
        vp[0][j] = True
        qa.append((m-1,j))
        a[m-1][j] = True
        va[m-1][j] = True
      self.search(q,p,vp)
      self.search(qa,a,va)
      res = []
      for i in range(0,m):
        for j in range(0,n):
          if a[i][j] and p[i][j]:
            res.append([i,j])
      print p
      print a
      return res
a = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
a = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1]]
a = [[1]]
print Solution().pacificAtlantic(a)
