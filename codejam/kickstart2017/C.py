import sys
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
def inSp(a,s):
    for i in range(3):
        if a[0][i] < s[0][i]:
            return False
        if a[0][i] + a[1] > s[0][i]+s[1]:
            return False
    return True
def cover(a1,a2,sp):
    for s in sp:
        if (not inSp(s, a1)) and (not inSp(s, a2)):
            return False
    return True
def work(case,sp):
    global minValue
    minValue = 1000000000
    num = len(sp)
    m = [min([sp[k][0][i] for k in range(num)]) for i in range(3)]
    M = [max([sp[k][0][i]+sp[k][1] for k in range(num)]) for i in range(3)]
    left = 0
    right = 1000000000
    while left < right:
        mid = (left+right)/2
        p = [m, [k-mid for k in M]]
        covered = False
        for i in range(4):
            x = i/2
            y = i%2
            if cover([[p[0][0],p[x][1],p[y][2]],mid],[[p[1][0],p[1-x][1],p[1-y][2]],mid],sp):
                covered = True
                break
        if covered:
            right = mid
        else:
            left = mid+1
    minValue = right
    print "Case #%d: %d"%(case,minValue)
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
        work(case+1,sp)

main()
