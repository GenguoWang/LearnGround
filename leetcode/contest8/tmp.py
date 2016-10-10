class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        s = sum(nums)
        if s%2 == 1:
            return False
        s //= 2
        print s
        c = [0]
        def f(nums, ss):
            c[0] += 1
            #print c[0]
            if ss==s:
                return True
            if ss>s:
                return False
            if not nums:
                return False
            nums2 = nums[1:]
            return f(nums2, ss+nums[0]) or f(nums2, ss)
        res = f(nums, 0)
        print c[0]
        return res
nums = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,100]
print 1<<len(nums)
print Solution().canPartition(nums)
