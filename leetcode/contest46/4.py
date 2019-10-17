class Solution(object):
    def index(self, pre,nex, l):
        r = []
        for i in l:
            if i>= pre and i<nex:
                r.append(i)
        return r
    def work(self, s, pre, f, pos, maxV,n,step,cnt):
        print pre,step,f
        if step >= maxV[0]:
            return
        if maxV[0] == cnt:
            return
        while pre < n and f[pre]:
            pre += 1
        if pre >= n:
            if step < maxV[0]:
                maxV[0] = step
                print step
            return
        nex = pre
        while nex < n and not f[nex]:
            nex += 1
        c = s[pre]
        aval = self.index(pre,nex,pos[c])
        na = len(aval)
        for k in range(na-1,-1,-1):
            for i in range(k+1):
                f[aval[i]] = True
            self.work(s,pre+1,f,pos,maxV,n,step+1,cnt)
            for i in range(k+1):
                f[aval[i]] = False

    def strangePrinter(self, s):
        """
        :type s: str
        :rtype: int
        """
        pos = {}
        n = len(s)
        cnt = 0
        for i in range(n):
            c = s[i]
            if c not in pos:
                cnt += 1
                pos[c] = []
            # pos[c].append(i)
            pos[c].append(i)
        f = [False for i in range(n)]
        maxV = [200]
        self.work(s, 0,f,pos,maxV,n,0,cnt)
        #print pos
        return maxV[0]

a = "aabbccaabbccddee" * 6
print len(a)
print Solution().strangePrinter(a)
