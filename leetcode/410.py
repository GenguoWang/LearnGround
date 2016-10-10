class Solution(object):
    def search(self,nums,m,x,minV,maxV):
      if minV >= self.v:
        return
      s = self.s
      n = self.n
      if ( (s[n]-s[x]) / m >= self.v):
        return
      minV = max(minV,
      if m == 1:
        remain = sum(nums[x:])
        print self.v," ",minV," ",remain
        self.v = min(max(minV,remain),self.v)
        return 
      s = nums[x]
      p = x+1
      f = True
      while p <= self.n - m:
          if s >= maxV:
            f = False
            break
          if s+nums[p] > minV:
            self.search(nums,m-1,p,max(s,minV),min(maxV,s+nums[p]))
          s += nums[p]
          p += 1
      if f:
            self.search(nums,m-1,p,max(s,minV),maxV)
          
    def splitArray(self, nums, m):
      n = len(nums)
      s = [0]
      for i in range(0,n):
        s.append(s[i]+nums[i])
      self.s = s
      avg = (s[n]+m-1) / m
      maxNum = max(nums)
      self.v = s[n]
      self.n = n
      self.search(nums,m,0,max(avg,maxNum),s[n]+1)
      return self.v

print Solution().splitArray([10,5,13,4,8,4,5,11,14,9,16,10,20,8],8) 
