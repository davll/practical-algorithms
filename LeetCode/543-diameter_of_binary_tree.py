# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# returns (max depth, max path)
def longest_path(root):
    if not root:
        return (0, 0)
    ld, lp = longest_path(root.left)
    rd, rp = longest_path(root.right)
    return (max(ld, rd)+1, max(lp, rp, ld+rd))

class Solution:
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        _, p = longest_path(root)
        return p
