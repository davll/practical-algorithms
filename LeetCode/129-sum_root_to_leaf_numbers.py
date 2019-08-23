# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        self.total = 0
        self.current = 0
        self.dfs(root)
        return self.total

    def dfs(self, node):
        if not node:
            return
        old_current = self.current
        self.current = self.current * 10 + node.val
        if not node.left and not node.right:
            self.total += self.current
        else:
            self.dfs(node.left)
            self.dfs(node.right)
        self.current = old_current
