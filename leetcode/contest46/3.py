# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def work(self, root, s):
        if root == None:
            return 0
        l = self.work(root.left,s)
        r = self.work(root.right,s)
        res = l+r+root.val
        s.add(res)
        return res
    def checkEqualTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        s = set()
        if root == None:
            return False
        l = self.work(root.left, s)
        r = self.work(root.right, s)
        total = l+r+root.val
        print total
        if total % 2 != 0:
            return False
        return (total/2) in s

a = TreeNode(5) 
a.left = TreeNode(10)
a.right = TreeNode(10)
a.right.left = TreeNode(2)
a.right.right = TreeNode(3)
print Solution().checkEqualTree(a)

        
