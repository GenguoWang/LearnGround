class Solution(object):
    def findNumberOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 0:
            return 0
        res = [1 for i in range(n)]
        cnt = [1 for i in range(n)]
        for i in range(1,n):
            c = nums[i]
            mValue = 1
            cValue = 1
            for j in range(i):
                if nums[j] < c:
                    if res[j] + 1 > mValue:
                        mValue = res[j]+1
                        cValue = cnt[j]
                    elif res[j]+1 == mValue:
                        cValue += cnt[j]
            res[i] = mValue
            cnt[i] = cValue
        mValue = max(res)
        r = 0
        for i in range(n):
            if res[i] == mValue:
                r += cnt[i]
        print res
        return r

a = [1,3,5,4,7]
a = [0,1,1,2,2]
print Solution().findNumberOfLIS(a)
