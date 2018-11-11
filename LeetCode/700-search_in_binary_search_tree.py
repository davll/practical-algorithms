# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def dfs(root, val):
    if not root:
        return None
    if root.val == val:
        return root
    elif root.val > val:
        return dfs(root.left, val)
    else:
        return dfs(root.right, val)

class Solution:
    def searchBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        return dfs(root, val)
