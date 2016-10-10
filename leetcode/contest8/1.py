class Solution:
  def addStrings(self, num1, num2):
    n1 = len(num1)
    n2 = len(num2)
    if n1 < n2:
      n = n1
      n1 = n2
      n2 = n
      n = num1
      num1 = num2
      num2 = n
    res = [ord(i)-ord('0') for i in num1]
    c = 0
    for k in range(0,n1):
      i1 = n1 - 1 -k
      i2 = n2 - 1 -k
      if i2 >=0 :
        res[i1] += ord(num2[i2])-ord('0') + c
      else:
        res[i1] += c
      c = res[i1]/10
      res[i1] %= 10
    if c > 0:
      res.insert(0,c)
    return "".join([str(i) for i in res])

print Solution().addStrings("9999","9999234")

