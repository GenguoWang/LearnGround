class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None
class Solution(object):
  def pathSum(self, root, sum):
    cnt = [0]
    def search(node,cur):
      if node == None:
        return
      now = cur[-1] + node.val
      for v in cur:
        if now - v == sum:
          cnt[0] += 1
      cur.append(now)
      search(node.left,cur)
      search(node.right,cur)
      cur.pop()
    search(root, [0])
    return cnt[0]

root = TreeNode(10)
print Solution().pathSum(root,10)
    
