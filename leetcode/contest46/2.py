class Solution(object):
    def work(self, M,i,j,x,y):
        s = 0
        c = 0
        for di in [-1,0,1]:
            for dj in [-1,0,1]:
                if di+i >=0 and di+i < x and dj+j>=0 and dj+j < y:
                    s += M[di+i][dj+j]
                    c += 1
        return s/c
        
    def imageSmoother(self, M):
        """
        :type M: List[List[int]]
        :rtype: List[List[int]]
        """
        x = len(M)
        if x == 0:
            return M
        y = len(M[0])
        if y == 0:
            return M
        r = [[0 for j in range(y)] for i in range(x)]
        for i in range(x):
            for j in range(y):
                r[i][j] = self.work(M,i,j,x,y)
        return r

a = [
    [1,1,1],
    [1,1,1],
    [1,1,1],
]

print Solution().imageSmoother(a)
