class Solution(object):
    def validWordSquare(self, words):
        """
        :type words: List[str]
        :rtype: bool
        """
        n = len(words)
        if n == 0:
            return True
        m = len(words[0])
        if n != m:
            return False
        for i in range(0,n):
            if len(words[i]) > n:
              return False
            for j in range(i+1,n):
                if len(words[i]) < j and len(words[j]) < i:
                  pass
                elif len(words[i]) < j or len(words[j]) < i:
                  return False
                elif words[i][j] != words[j][i]:
                    return False
        return True
