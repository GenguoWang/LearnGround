def ind(c):
    return ord(c)-ord('a')+1
class Solution(object):
    def index(self, pre,nex, l):
        r = []
        for i in l:
            if i>= pre and i<nex:
                r.append(i)
        return r
    def work(self,s, pos, pre,nex,d, oldc):
        if d[oldc][pre][nex] >= 0:
            return d[oldc][pre][nex]
        if nex <= pre:
            return 0
        curc = ind(s[pre])
        if nex == pre+1:
            if curc == oldc:
                return 0
            return 1
        if oldc == 0:
            d[oldc][pre][nex] = 1 + self.work(s,pos,pre+1,nex,d,curc)
            return d[oldc][pre][nex]
        aval = self.index(pre,nex,pos[oldc])
        maxV = self.work(s,pos,pre,nex,d,0)
        for k in aval:
            c = self.work(s,pos,pre,k,d,0) + self.work(s,pos,k+1,nex,d,oldc)
            if c < maxV:
                maxV = c
        d[oldc][pre][nex]=maxV
        return maxV

    def strangePrinter(self, s):
        """
        :type s: str
        :rtype: int
        """
        pos = {}
        n = len(s)
        cnt = 0
        d = [[[-1 for i in range(n+1)] for i in range(n+1)] for i in range(27)]
        for i in range(n):
            c = ind(s[i])
            if c not in pos:
                cnt += 1
                pos[c] = []
            # pos[c].append(i)
            pos[c].append(i)
        f = [False for i in range(n)]
        #print pos
        res = self.work(s,pos,0,n,d,0)
        return res

a = "abcdefabcdefffffffffffffedcbafedcba" * 3
print len(a)
print Solution().strangePrinter(a)
