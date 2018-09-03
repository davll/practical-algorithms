# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        def traverse(node, s):
            if node == None:
                return False
            s -= node.val
            if node.left == None and node.right == None:
                return s == 0
            else:
                return traverse(node.left, s) or traverse(node.right, s)
        return traverse(root, sum)
