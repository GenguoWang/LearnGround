class Solution(object):
    def longestPalindrome(self, s):
      d = {}
      for i in s:
        if i in d:
          d[i] += 1
        else:
          d[i] = 1
      s = 0
      f = False
      for k in d:
        v = d[k]
        if v %2 == 0:
          s += v
        else:
          f = True
          s += v-1
      if f:
        s +=1
      return s

