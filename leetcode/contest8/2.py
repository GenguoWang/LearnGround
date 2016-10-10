class Solution(object):
    def canPartition(self, nums):
      n = len(nums)
      if n <2:
        return False
      s = sum(nums)
      if s%2 != 0:
        return False
      avg = s/2
      f = [[False for j in range(0,n+1)] for i in range(0,avg+1)]
      for i in range(0,n+1):
        f[0][i] = True
      for i in range(1,n+1):
        for j in range(1,avg+1):
          f[j][i] = f[j][i-1]
          if j-nums[i-1] >=0:
            f[j][i] = f[j][i] or f[j-nums[i-1]][i-1]
      return f[avg][n-1]
a = [53,63,64,51,78,28,26,32,60,20,73,32,21,21,7,45,82,89,44,43,85,93,30,100,91,51,46,95,65,20,78,2,45,34,3,26,25,30,80,15,7,45,82,74,8,59,74,3,38,20,97,47,21,70,84,18,90,68,38,24,53,83,27,57,1,99,2,60,21,4,48,71,5,87,78,72,81,40,65,32,14,30,94,58,14,49,82,4,51,66,5,50,90,22,90,100,50,44,68,100]
print Solution().canPartition(a)
