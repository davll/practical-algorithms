# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        def swap_sides(subtree):
            if subtree != None:
                tmp = subtree.left
                subtree.left = subtree.right
                subtree.right = tmp
                swap_sides(subtree.left)
                swap_sides(subtree.right)
        swap_sides(root)
        return root
