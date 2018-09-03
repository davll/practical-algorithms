# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def is_mirror(tree1, tree2):
            if tree1 == None and tree2 == None:
                return True
            elif tree1 != None and tree2 != None:
                if tree1.val == tree2.val:
                    return is_mirror(tree1.left, tree2.right) and is_mirror(tree1.right, tree2.left)
                else:
                    return False
            else:
                return False
        if root == None:
            return True
        else:
            return is_mirror(root.left, root.right)
