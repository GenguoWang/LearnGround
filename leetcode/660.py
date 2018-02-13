g = [0,1]
c = 10
p = 1
for i in range(10):
    p = p*9+c
    c *= 10
    g.append(p)
def f(n):
    if n < 10:
        return 1 if n==9 else 0
    d = [i for i in str(n)]
    k = len(d)-1
    v = int(d[0])
    e = int(''.join(d[1:]))
    if v == 9:
        return v*g[k]+e+1
    else:
        return v*g[k]+f(e)
class Solution(object):
    def newInteger(self, n):
        """
        :type n: int
        :rtype: int
        """
        l = n
        r = 10*n
        while l<r:
            m = (l+r)/2
            c = m-f(m)
            if c < n:
                l = m+1
            else:
                r = m
        return l

print f(8)
print Solution().newInteger(1)
