class Solution(object):
    def numberOfArithmeticSlices(self, A):
      n = len(A)
      if n < 3:
        return 0
      a = sorted(A)
      g = {}
      for i in range(n):
        g[a[i]] = i
      v = [{} for i in range(n)]
      cnt = 0
      for i in range(n):
        for j in range(i+1,n):
          d = a[j] - a[i]
          if (d in v[i]) or (d in v[j]):
            continue
          v[i][d] = 1
          v[j][d] = 1
          q = 2
          if d == 0:
            c = j+1
            while c < n and a[c] == a[i]:
              v[c][d] = 1
              q += 1
              c += 1
            if q > 2:
              cnt += (q-2)*(q-1)*q/6
              print q
          else:
            c = a[j]+d
            while c in g:
              v[g[c]][d] = 1
              q += 1
              c += d
            if q > 2:
              cnt += (q-2)*(q-1)/2
              print q,i,j,d
      return cnt

a = [1,2,3,4,5,10,11,12]
a = [-2147483648,0,-2147483648]
a = [79,20,64,28,67,81,60,58,97,85,92,96,82,89,46,50,15,2,36,44,54,2,90,37,7,79,26,40,34,67,64,28,60,89,46,31,9,95,43,19,47,64,48,95,80,31,47,19,72,99,28,46,13,9,64,4,68,74,50,28,69,94,93,3,80,78,23,80,43,49,77,18,68,28,13,61,34,44,80,70,55,85,0,37,93,40,47,47,45,23,26,74,45,67,34,20,33,71,48,96]
a = [0, 2, 2, 3, 4, 7, 9, 9, 13]
a = [2,2,2,2,2,2,2]
print Solution().numberOfArithmeticSlices(a)
