# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def max_depth(root):
    def _traverse(node, h):
        if not node:
            return h
        return max(_traverse(node.left, h+1), _traverse(node.right, h+1))
    return _traverse(root, 0)

class Solution:
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return max_depth(root)
