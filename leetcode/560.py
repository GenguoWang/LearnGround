def work(nums,n,target,a):
    if (n,target) not in a:
        if n > 0:
            a[(n,target)] = work(nums,n-1,target-nums[n],a) + (1 if target == nums[n] else 0)
        else:
            return 1 if target == nums[n] else 0
    return a[(n,target)]
class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        s = 0
        a = {}
        for i in range(len(nums)):
            s += work(nums,i,k,a)
        return s

print Solution().subarraySum([-1,-1,1],0)
