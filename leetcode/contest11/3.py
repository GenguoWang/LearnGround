class Solution(object):
    def findMinArrowShots(self, points):
      n = len(points)
      if n == 0:
        return 0
      p = sorted(points)
      cnt = 1
      l = p[0][0]
      r = p[0][1]
      for i in range(1,n):
        x = p[i][0]
        y = p[i][1]
        if x > r:
          cnt += 1
          l = x
          r = y
        else:
          l = x
          if y < r:
            r = y
      return cnt
a = [[10,16], [2,8], [1,6], [7,12]]
a = [[1,100],[2,5],[3,4],[7,8],[9,10]]
print Solution().findMinArrowShots(a)
