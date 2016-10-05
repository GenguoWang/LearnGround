class Solution(object):
    def largestDivisibleSubset(self, nums):
      nums = sorted(nums)
      nums.reverse()
      n = len(nums)
      r = [1 for i in range(0,n)]
      p = [-1 for i in range(0,n)]
      for i in range(0,n):
        for j in range(0,i):
          if nums[j] != nums[i] and nums[j] % nums[i] == 0 and r[i]<r[j]+1:
            r[i] = r[j]+1
            p[i] = j
      ind = 0
      maxV = 0
      for i in range(0,n):
        if r[i] > maxV:
          maxV = r[i]
          ind = i
      l = []
      while ind >=0:
        l.append(nums[ind])
        ind = p[ind]
      return l

print Solution().largestDivisibleSubset([1,2,3])
