class Solution(object):                                                                                               
    def calcEquation(self, equations, values, queries):
      dics = []
      def findInDics(dics,op):
        for i in range(0,len(dics)):
          if op in dics[i]:
            return i
        return None
      def findInDicsOrAdd(dics,op):
        r = findInDics(dics,op)
        if r == None:
          dics.append({op:1.0})
          r = len(dics) - 1
        return r
      for i in range(0,len(values)):
        op1 = equations[i][0]
        op2 = equations[i][1]
        v = values[i]
        index1 = findInDicsOrAdd(dics,op1)
        index2 = findInDicsOrAdd(dics,op2)
        rate = v * dics[index2][op2] / dics[index1][op1]
        for key in dics[index1]:
          dics[index2][key] = dics[index1][key] * rate
        dics.pop(index1)
      res = []
      for pair in queries:
        op1 = pair[0]
        op2 = pair[1]
        index1 = findInDics(dics, op1)
        index2 = findInDics(dics, op2)
        if index1 == index2 and index1 != None:
          res.append(dics[index1][op1] / dics[index2][op2])
        else:
          res.append(-1.0)
      return res


equations = [ ["a", "b"], ["b", "c"] ]
values = [2.0, 3.0]
queries = [ ["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"] ]
print Solution().calcEquation(equations, values, queries)
