# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# returns (p, d)
# p = maximum path inside subtree
# d = maximum path from root to any node
def dfs(root):
    mp = root.val
    md = root.val
    if root.left:
        lp, ld = dfs(root.left)
        md = max(md, ld + root.val)
        mp = max(mp, md, lp)
    if root.right:
        rp, rd = dfs(root.right)
        md = max(md, rd + root.val)
        mp = max(mp, md, rp)
    if root.left and root.right:
        mp = max(mp, root.val + ld + rd)
    return (mp, md)

class Solution:
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        p, _ = dfs(root)
        return p
