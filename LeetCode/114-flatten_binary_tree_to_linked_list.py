# https://leetcode.com/problems/flatten-binary-tree-to-linked-list/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def bt_flatten(root):
    if not root:
        return None
    if not root.left and not root.right:
        return root
    left, right = root.left, root.right
    left_tail = bt_flatten(left)
    right_tail = bt_flatten(right)
    if left_tail:
        left_tail.right = right
    root.left = None
    root.right = left or right
    return right_tail or left_tail

class Solution:
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        bt_flatten(root)
