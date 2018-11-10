# https://leetcode.com/problems/unique-binary-search-trees-ii/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def copy_tree(tree, delta):
    if not tree:
        return None
    node = TreeNode(tree.val + delta)
    node.left = copy_tree(tree.left, delta)
    node.right = copy_tree(tree.right, delta)
    return node

class Solution:
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if n == 0:
            return []
        dp = [[] for _ in range(n+1)]
        dp[0].append(None)
        for k in range(1, n+1):
            for x in range(1,k+1):
                for left in dp[x-1]:
                    for right in dp[k-x]:
                        root = TreeNode(x)
                        root.left = copy_tree(left, 0)
                        root.right = copy_tree(right, x)
                        dp[k].append(root)
        return dp[n]
