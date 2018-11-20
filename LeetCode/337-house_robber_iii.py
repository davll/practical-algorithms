# https://leetcode.com/problems/house-robber-iii/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# return (x, y)
# x = root is robbed
# y = root is not robbed
def rob_bt_v1(root):
    if not root:
        return (0, 0)
    lx, ly = rob_bt_v1(root.left)
    rx, ry = rob_bt_v1(root.right)
    # rob the root
    x = root.val + ly + ry
    # not rob the root
    y = max(lx, ly) + max(rx, ry)
    #
    return (x, y)

class Solution:
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return max(rob_bt_v1(root))
