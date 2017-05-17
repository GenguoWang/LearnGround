import sys
sys.setrecursionlimit(3000)
r = [57846736,
27,
307731966,
200000000,
3,
16,
295,
260,
324,
262,
3,
286,
327952909,
30,
20,
27,
28,
29,
304719599,
22,
293,
291082944,
265,
330,
262940960,
152114544,
27,
61486792,
4,
33,
293532179,
49583234,
325022847,
49519433,
296,
33,
254,
305284494,
27,
21,
319916126,
325,
280,
26,
280104891,
297,
265859180,
21,
287,
285541029,
23,
29,
288,
278573327,
326,
292265855,
245470838,
73366173,
245705645,
24,
319,
98989727,
90668487,
350600410,
246,
32,
327,
5,
28331360,
236988798,
29,
273210896,
31,
35,
28,
92903111,
28,
269,
310,
302,
304,
265,
305897079,
327,
30,
29,
25,
27,
319,
315,
32879707,
322,
292,
2,
327486330,
26,
341811318,
112236070,
303,
31]
minValue = 1000000000
def addSp(a1,a2):
    if a1 == None:
        return [a2[0],[i+a2[1] for i in a2[0]]]
    return [[min(a1[0][i],a2[0][i]) for i in range(3)],
            [max(a1[1][i],a2[0][i]+a2[1]) for i in range(3)]]
def inSp(a1,a2):
    if a1 == None:
        return False
    p = a2[0]
    l = a2[1]
    for i in range(3):
        if p[i] < a1[0][i]:
            return False
        if p[i]+l > a1[1][i]:
            return False
    return True
def dfs(s1,s2,i,num,sp,t1=[],t2=[]):
    global minValue
    now = 0
    if s1 != None:
        now = max([s1[1][k]-s1[0][k] for k in range(3)])
    if s2 != None:
        n1 = max([s2[1][k]-s2[0][k] for k in range(3)])
        now = max(now,n1)
    if now >= minValue:
        return
    if i==num:
        minValue = min(now,minValue)
        return
    if inSp(s1, sp[i]):
        ns = addSp(s1,sp[i])
        dfs(ns,s2,i+1,num,sp,t1+[i],t2)
    elif inSp(s2, sp[i]):
        ns = addSp(s2,sp[i])
        dfs(s1,ns,i+1,num,sp,t1,t2+[i])
    else:
        ns = addSp(s1,sp[i])
        dfs(ns,s2,i+1,num,sp,t1+[i],t2)
        ns = addSp(s2,sp[i])
        dfs(s1,ns,i+1,num,sp,t1,t2+[i])
def dist(a, a1, a2):
    d1 = max([max(a[0][i]+a[1]-a1[0][i], a1[0][i]+a1[1]-a[0][i]) for i in range(3)])
    d2 = max([max(a[0][i]+a[1]-a2[0][i], a2[0][i]+a2[1]-a[0][i]) for i in range(3)])
    return min(d1,d2)
def work(case,sp):
    i1,i2 = preWork(sp)
    s1 = addSp(None, sp[i1])
    s2 = addSp(None, sp[i2])
    sp = sorted(sp, key=lambda ii:-dist(ii,sp[i1],sp[i2]))
    global minValue
    minValue = 1000000000
    num = len(sp)
    dfs(s1,s2,0,num,sp)
    print "Case #%d: %d"%(case,minValue)
def preWork(sp):
    n = len(sp)
    m = [min(xrange(n),key=lambda i:sp[i][0][k]) for k in range(3)]
    M = [max(xrange(n),key=lambda i:sp[i][0][k]+sp[i][1]) for k in range(3)]
    k = max(range(3), key=lambda i:sp[M[i]][0][i]+sp[M[i]][1]-sp[m[i]][0][i])
    return [m[k], M[k]]
def main():
    inF = sys.stdin
    N = int(inF.readline())
    for case in range(N):
        n = int(inF.readline())
        sp = []
        for j in range(n):
            x = inF.readline().split()
            x = [int(i) for i in x]
            p = x[0:3]
            l = x[3]
            p = [i-l for i in p]
            sp.append([p,2*l])
        print n
        work(case+1,sp)
#        if minValue != r[case]:
#            print case+1
#            raise Error()

main()
