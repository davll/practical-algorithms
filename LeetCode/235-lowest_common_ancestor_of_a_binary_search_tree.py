# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def bst_lca(root, p, q):
    if p.val < root.val and q.val < root.val:
        return bst_lca(root.left, p, q)
    elif root.val < p.val and root.val < q.val:
        return bst_lca(root.right, p, q)
    else:
        return root

class Solution:
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        return bst_lca(root, p, q)
