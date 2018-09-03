# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def check(node, lower, upper):
            if node == None:
                return True
            elif (lower == None or node.val > lower) and (upper == None or node.val < upper):
                cond1 = check(node.left, lower, node.val)
                cond2 = check(node.right, node.val, upper)
                return cond1 and cond2
            else:
                return False
        if root == None:
            return True
        cond1 = check(root.left, None, root.val)
        cond2 = check(root.right, root.val, None)
        return cond1 and cond2
