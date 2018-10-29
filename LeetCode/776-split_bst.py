# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def split_bst(node, value):
    if not node:
        return (None, None)
    elif node.val <= value:
        l, r = split_bst(node.right, value)
        node.right = l
        return (node, r)
    else: # node.val > value
        l, r = split_bst(node.left, value)
        node.left = r
        return (l, node)

class Solution:
    def splitBST(self, root, V):
        """
        :type root: TreeNode
        :type V: int
        :rtype: List[TreeNode]
        """
        return list(split_bst(root, V))
