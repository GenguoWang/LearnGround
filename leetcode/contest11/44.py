class Solution(object):
  def numberOfArithmeticSlices(self, A):
    """
    :type A: List[int]
    :rtype: int
    """
    ans=0
    dp = []
    for i in range(len(A)):
      a=A[i]
      dp.append({})
      for j in range(i):
        b=A[j]
        d=a-b
        if d in dp[j]:
          v=1+dp[j][d]
        else:
          v=1
        if d in dp[i]:
          dp[i][d]=dp[i][d]+v
        else:
          dp[i][d]=v
      ans += sum([dp[i][x] for x in dp[i]]) - i
    return ans

a = [0, 2, 2, 3, 4, 7, 9, 9, 13]
a = [79,20,64,28,67,81,60,58,97,85,92,96,82,89,46,50,15,2,36,44,54,2,90,37,7,79,26,40,34,67,64,28,60,89,46,31,9,95,43,19,47,64,48,95,80,31,47,19,72,99,28,46,13,9,64,4,68,74,50,28,69,94,93,3,80,78,23,80,43,49,77,18,68,28,13,61,34,44,80,70,55,85,0,37,93,40,47,47,45,23,26,74,45,67,34,20,33,71,48,96]
print Solution().numberOfArithmeticSlices(a)
