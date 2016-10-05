class Solution(object):
  def toHex(self, num):
    def toChar(c):
      if c < 10:
        return chr(c+ord('0'))
      else:
        return chr(c-10+ord('a'))
    if num < 0:
      num = (1<<32) + num
    l = []
    while num > 0:
      l.append(toChar(num%16))
      num /= 16
    if len(l) == 0:
      return "0"
    l.reverse()
    return "".join(l)
print Solution().toHex(0)
print Solution().toHex(26)
print Solution().toHex(-1)
