# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def work(self, node, level, index, l, r):
        if node == None:
            return
        if level not in l:
            l[level] = index
            r[level] = index
        else:
            if index < l[level]:
                l[level] = index
            if index > r[level]:
                r[level] = index
        self.work(node.left, level+1, index*2,l,r)
        self.work(node.right, level+1, index*2+1,l,r)
    def widthOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        l = {}
        r = {}
        self.work(root, 0, 0, l, r)
        m = -1
        for i in l:
            if r[i]-l[i] > m:
                m = r[i] - l[i]
        return m+1

a = TreeNode(1)
a.left = TreeNode(2)
a.right = TreeNode(3)
a.left.right = TreeNode(4)
a.right.right = TreeNode(5)
print Solution().widthOfBinaryTree(a)
