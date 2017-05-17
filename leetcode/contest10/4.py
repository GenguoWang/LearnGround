class Solution(object):
    def sequenceReconstruction(self, org, seqs):
      n = len(org)
      r = [0 for i in range(n)]
      for i in range(n):
        r[org[i]-1] = i
      print r
      for i in seqs:
        for j in range(len(i)):
          if i[j] > n or i[j] < 1:
            return False
          i[j] = r[i[j]-1]
      for i in range(n):
        r[i] = 0
      for s in seqs:
        ns = len(s)
        for i in range(ns):
          if i < ns - 1:
            if s[i] >= s[i+1]:
              return False
            if s[i]+1 == s[i+1]:
              r[s[i]] = 2
          if r[s[i]] == 0:
            r[s[i]] = 1
      for i in range(n):
        if i < n-1:
          if r[i] != 2:
            return False
        else:
          if r[i] != 1:
            return False
      return True
a = [4,1,5,2,6,3]
b = [[5,2,6,3],[4,1,5,2]]
print Solution().sequenceReconstruction(a,b)
