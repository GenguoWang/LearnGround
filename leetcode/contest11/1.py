class Solution(object):
    def minMoves(self, nums):
      n = len(nums)
      if n == 0:
        return 0
      a = min(nums)
      return sum(nums)-a*n
