class TreeNode(object):
    def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.s = 0
        def calc(self, node, isLeft):
          if node == None:
            return
          if isLeft and node.left == None and node.right == None:
            self.s += node.val
          calc(self, node.left, True)
          calc(self, node.right, False)
        calc(self, root, False)
        return self.s

