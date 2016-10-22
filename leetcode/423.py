class Solution(object):
    def originalDigits(self, s):
      def ind(c):
        return ord(c)-ord('a')
      d = [0 for i in range(26)]
      cnt = [0 for i in range(10)]
      for c in s:
        d[ind(c)] += 1
      b = [[0,'zero','z'],
          [2,'two','w'],
          [8,'eight','g'],
          [4,'four','u'],
          [6,'six','x'],
          [5,'five','f'],
          [1,'one','o'],
          [3,'three','r'],
          [7,'seven','s'],
          [9,'nine','i']]
      s = dict()
      for p in b:
        n = d[ind(p[2])]
        cnt[p[0]] += n
        for c in p[1]:
          if c in s:
            s[c] += 1
          else:
            s[c] = 1
          d[ind(c)] -= n
      print s
      s = ""
      for i in range(10):
        s += chr(i+ord('0'))*cnt[i]
      return s
print Solution().originalDigits("esnve")
