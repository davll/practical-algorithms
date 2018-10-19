# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import math

def validate_bst(root):
    def _check(node, lower, upper):
        if not node:
            return True
        elif node.val > lower and node.val < upper:
            cond1 = _check(node.left, lower, node.val)
            cond2 = _check(node.right, node.val, upper)
            return cond1 and cond2
        else:
            return False
    if not root:
        return True
    cond1 = _check(root.left, -math.inf, root.val)
    cond2 = _check(root.right, root.val, math.inf)
    return cond1 and cond2

class Solution:
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return validate_bst(root)
