# https://leetcode.com/problems/binary-tree-upside-down/
# https://www.geeksforgeeks.org/flip-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def flip_bst(root):
    if not root:
        return None
    elif not root.left and not root.right:
        return root
    #
    flipped_root = flip_bst(root.left)
    # rotate
    root.left.left = root.right
    root.left.right = root
    root.left = root.right = None
    #
    return flipped_root

class Solution:
    def upsideDownBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        return flip_bst(root)
