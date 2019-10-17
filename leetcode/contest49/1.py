class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 0:
            return 0
        res = [1 for i in range(n)]
        for i in range(1,n):
            if nums[i] > nums[i-1]:
                res[i] = res[i-1]+1
            else:
                res[i] = 1
        return max(res)

print Solution().findLengthOfLCIS([1,3,5,4,7])

