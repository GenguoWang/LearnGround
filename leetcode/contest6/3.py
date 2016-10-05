class Solution(object):
  def reconstructQueue(self, people):
    def cmpd(a,b):
      if a[0] > b[0]:
        return -1
      elif a[0] == b[0] and a[1] < b[1]:
        return -1
      elif a[0] == b[0] and a[1] == b[1]:
        return 0
      return 1
    people = sorted(people,cmpd)
    r = []
    print people
    for i in range(0,len(people)):
      p = people[i]
      k = p[1]
      h = p[0]
      c = 0
      index = i
      for j in range(0,i):
        if c == k:
          index = j
          break
        if r[j][0] >= h:
          c += 1
      if index < 0:
        index = 0
      print index
      r.insert(index,p)
    return r
a = [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]
print Solution().reconstructQueue(a)
