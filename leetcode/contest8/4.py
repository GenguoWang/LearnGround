class Solution(object):
    def wordsTyping(self, sentence, rows, cols):
      n = len(sentence)
      if n == 0:
        return 0
      f = [0 for i in range(0,n)]
      s = [0 for i in range(0,n)]
      for i in range(0,n):
        s[i] = len(sentence[i]) + 1
      total = sum(s)
      cols += 1
      t = cols/total * n
      cols = cols % total
      for i in range(0,n):
        f[i] = t
        c = 0
        for j in range(0,n):
          if c+s[(i+j)%n] <= cols:
            c += s[(i+j)%n]
            f[i] += 1
          else:
            break
      res = 0
      pos = 0
      for i in range(0,rows):
        res += f[pos]
        pos += f[pos]
        pos = pos % n
      return res / n
rows = 2
cols = 17
sentence = ["hello", "world"]
print Solution().wordsTyping(sentence,rows,cols)
rows = 3
cols = 4
sentence = ["a", "bcd", "e"]
print Solution().wordsTyping(sentence,rows,cols)
rows = 4
cols = 4
sentence = ["I", "had", "apple", "pie"]
print Solution().wordsTyping(sentence,rows,cols)
