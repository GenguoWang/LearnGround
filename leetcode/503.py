class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        if n == 0:
            return []
        mValue = max(nums)
        res = [-1 for i in range(n)]
        flag = [False if nums[i]!=mValue else True for i in range(n)]
        q = range(n)
        while len(q) > 0:
            cur = q[-1]
            if flag[cur]:
                q.pop()
                continue
            nex = (cur+1) % n
            if cur == nex:
                flag[cur] = True
                res[cur] = -1
                q.pop()
                continue
            while nex != -1 and flag[nex] and nums[nex] <= nums[cur]:
                nex = res[nex]
            if nex == -1 or nex == cur:
                flag[cur] = True
                res[cur] = -1
                q.pop()
            elif nums[nex] > nums[cur]:
                res[cur] = nex
                flag[cur] = True
                q.pop()
                if not flag[nex]:
                    q.append(nex)
            else:
                q.append(nex)
        print res
        return [nums[i] if i != -1 else -1 for i in res]
a = range(30000,-1,-1)
print Solution().nextGreaterElements(a)
