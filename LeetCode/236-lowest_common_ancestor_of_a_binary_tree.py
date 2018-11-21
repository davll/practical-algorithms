# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# returns (ancestor, status)
#
# status = 0b00 : nothing found
# status = 0b01 : found p
# status = 0b10 : found q
# status = 0b11 : both found
#
def bt_lca(root, p, q):
    if not root:
        return (None, 0b00)
    status = 0
    if root.val == p.val:
        status |= 0b01
    if root.val == q.val:
        status |= 0b10
    left_a, left_st = bt_lca(root.left, p, q)
    right_a, right_st = bt_lca(root.right, p, q)
    status |= left_st | right_st
    if left_st == 0b11:
        return (left_a, 0b11)
    elif right_st == 0b11:
        return (right_a, 0b11)
    elif status == 0b11:
        return (root, 0b11)
    else:
        return (None, status)

class Solution:
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        x, _ = bt_lca(root, p, q)
        return x
