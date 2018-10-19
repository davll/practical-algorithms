# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def build_tree(preorder, inorder):
    def _traverse(pl, il, ancestor):
        #print("pl = {pl}, il = {il}, ancestor = {a}".format(pl=pl, il=il, a=ancestor))
        if pl == len(preorder) or il == len(inorder):
            return None, pl, il
        elif inorder[il] == ancestor:
            return None, pl, il
        val = preorder[pl]
        node = TreeNode(val)
        pl += 1
        if inorder[il] != val:
            node.left, pl, il = _traverse(pl, il, val)
        assert inorder[il] == val
        node.right, pl, il = _traverse(pl, il+1, ancestor)
        return node, pl, il
    root, _, _ = _traverse(0, 0, None)
    return root

class Solution:
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        return build_tree(preorder, inorder)
