def less(m,n,v):
    if m > n:
        a = m
        m = n
        n = a
    res = 0
    for i in range(m):
        res += min(n,v/(i+1))
    return res
class Solution(object):
    def findKthNumber(self, m, n, k):
        """
        :type m: int
        :type n: int
        :type k: int
        :rtype: int
        """
        l = 0
        r = m*n+1
        while l < r:
            a = (l+r)/2
            v = less(m,n,a)
            if v < k:
                l = a+1
            else:
                r = a
        return r
print less(5,5,10)
print Solution().findKthNumber(2,3,3)

