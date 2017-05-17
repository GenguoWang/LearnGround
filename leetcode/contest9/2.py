class Solution(object):
    def findAnagrams(self, s, p):
      def idx(c):
        return ord(c)-ord('a')
      def ok(l):
        cnt = 0
        for i in l:
          if i > 0:
            cnt += i
          else:
            cnt -= i
        return cnt
      r = [0 for i in range(26)]
      for i in p:
        r[idx(i)] += 1
      NS = len(s)
      NP = len(p)
      if NS < NP:
        return []
      for i in range(NP):
        r[idx(s[i])] -= 1
      res = []
      cnt = ok(r)
      if cnt == 0:
        res.append(0)
      for i in range(NS-NP):
        r[idx(s[i])] += 1
        r[idx(s[i+NP])] -= 1
        cnt -= 2
        if cnt <= 0:
          cnt = ok(r)
        if cnt==0:
          res.append(i+1)
      return res
print Solution().findAnagrams("cbaebabacd", "abc")
print Solution().findAnagrams("abab", "ab")
