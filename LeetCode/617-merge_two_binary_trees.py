# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def merge(t1, t2):
    if t1 and t2:
        t = TreeNode(t1.val + t2.val)
        t.left = merge(t1.left, t2.left)
        t.right = merge(t1.right, t2.right)
        return t
    else:
        return (t1 if t1 else t2)

class Solution:
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        return merge(t1, t2)
