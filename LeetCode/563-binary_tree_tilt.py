# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# returns (all_values, all_tilt)
def tilt(root):
    if not root:
        return (0, 0)
    lv, lt = tilt(root.left)
    rv, rt = tilt(root.right)
    v = root.val + lv + rv
    t = abs(lv - rv) + lt + rt
    return (v, t)

class Solution:
    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        _, t = tilt(root)
        return t
