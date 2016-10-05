import heapq
class Solution(object):
  def flodd(self,now,x,y):
    a = [x-1,x+1,x,x]
    b = [y,y,y-1,y+1]
    for i in range(0,4):
        xx = a[i]
        yy = b[i]
        if xx < 0 or xx>=self.n:
          continue
        if yy < 0 or yy >= self.m or self.v[xx][yy]:
          continue
        if self.h[xx][yy] < now:
          self.s += now - self.h[xx][yy]
          self.h[xx][yy] = now
        self.add(xx,yy)
  def add(self, x,y):
    heapq.heappush(self.l, (self.h[x][y],(x,y)))
    self.v[x][y] = True
  
  def trapRainWater(self, heightMap):
    n = len(heightMap)
    if n <= 2:
      return 0
    m = len(heightMap[0])
    if m <=2:
      return 0
    self.h = heightMap
    self.n = n
    self.m = m
    self.s = 0
    h = heightMap
    self.v = [[False for i in range(0,m)] for j in range(0,n)]
    self.l = []
    for i in range(0,n):
      self.add(i,0)
      self.add(i,m-1)
    for i in range(0,m):
      self.add(0,i)
      self.add(n-1,i)
    while(len(self.l) > 0):
      now = heapq.heappop(self.l)
      self.flodd(now[0],now[1][0],now[1][1])
    return self.s

  

a= [ [1,4,3,1,3,2], [3,2,1,3,2,4], [2,3,3,2,3,1] ]
print Solution().trapRainWater(a)
