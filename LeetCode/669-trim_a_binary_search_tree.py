# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def trim(root, L, R):
    if not root:
        return None
    if root.val < L:
        return trim(root.right, L, R)
    elif root.val > R:
        return trim(root.left, L, R)
    else:
        root.left = trim(root.left, L, R)
        root.right = trim(root.right, L, R)
        return root

class Solution:
    def trimBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: TreeNode
        """
        return trim(root, L, R)
