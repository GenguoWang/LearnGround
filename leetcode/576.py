class Solution(object):
    def nearestPalindromic(self, n):
        """
        :type n: str
        :rtype: str
        """
        l = len(n)
        if l == 1:
            return n
        h = l/2
        r = 10**h
        a = (int)("".join(n))
        b = a%r
        a = a/r
        #print a,b
        a1 = a-1
        a1str = str(a1)
        if a1==0:
            a1str = "9"
        if len(a1str) < h:
            a1str = a1str +'9'
        #print a1str
        b1 = int(a1str[0:h][::-1])
        r1 = a1*r+b1
        #print r1
        d1 = r+b-b1
        a2 = a
        b2 = int(str(a2)[0:h][::-1])
        r2 = a2*r+b2
        #print r2
        d2 = abs(b2-b)
        a3 = a+1
        b3 = int(str(a3)[0:h][::-1])
        d3 = r+b3-b
        r3 = a3*r+b3
        #print r3
        dm = d1
        res = r1
        if d2 < dm:
            dm = d2
            res =r2
        if d3 < dm:
            res = r3
        return list(str(res))

print Solution().nearestPalindromic(["9","9"])
print Solution().nearestPalindromic(["1","2","3"])
print Solution().nearestPalindromic(["1","0"])
print Solution().nearestPalindromic(["9","9","0"])
print Solution().nearestPalindromic(["1","0","0"])
print Solution().nearestPalindromic(["2"])
