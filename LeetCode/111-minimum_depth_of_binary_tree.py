# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def min_depth(root):
    def _traverse(node, h):
        if node.left:
            if node.right:
                return min(_traverse(node.left, h+1), _traverse(node.right, h+1))
            else:
                return _traverse(node.left, h+1)
        else:
            if node.right:
                return _traverse(node.right, h+1)
            else:
                return h+1
    if not root:
        return 0
    return _traverse(root, 0)

class Solution:
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return min_depth(root)
