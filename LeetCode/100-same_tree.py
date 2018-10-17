# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        def is_same(tree1, tree2):
            if tree1 == None and tree2 == None:
                return True
            elif tree1 != None and tree2 != None:
                if tree1.val == tree2.val:
                    cond1 = is_same(tree1.left, tree2.left)
                    cond2 = is_same(tree1.right, tree2.right)
                    return cond1 and cond2
                else:
                    return False
            else:
                return False
        return is_same(p, q)
