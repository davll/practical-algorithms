# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def dfs(root):
    if not root:
        return (0, True)
    lh, lb = dfs(root.left)
    rh, rb = dfs(root.right)
    h = max(lh, rh) + 1
    b = lb and rb and abs(lh-rh) <= 1
    return(h, b)

class Solution:
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        _, b = dfs(root)
        return b
