class Solution(object):
    def findRightInterval(self, intervals):
      def bsearch(d,v):
        i = 0
        j = len(d) - 1
        while i <= j:
          m = (i+j)/2
          if d[m][0][0] > v:
            j = m-1
          elif d[m][0][0] < v:
            i = m+1
          else:
            return d[m][1]
        if i < len(d):
          return d[i][1]
        #if d[m][0][0] > v:
        #  return d[m][1]
        #elif m < len(d)-1:
        #  return d[m+1][1]
        return -1
      #d = [[i.start,i.end] for i in intervals]
      d = intervals
      r = []
      res = []
      for i in range(len(d)):
        r.append([d[i],i])
        res.append(-1)
      r = sorted(r)
      for i in range(len(d)):
        res[i] = bsearch(r,d[i][1])
      return res
a = [ [1,2] ,[3,4]]
print Solution().findRightInterval(a)
