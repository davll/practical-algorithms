# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def build_tree(inorder, postorder):
    def _construct(il, ir, pl, pr):
        if il >= ir or pl >= pr:
            return None
        rootval = postorder[pr-1]
        im = -1
        for i in range(il, ir):
            if inorder[i] == rootval:
                im = i
                break
        assert im != -1
        pm = pl + (im - il)
        root = TreeNode(rootval)
        root.left = _construct(il, im, pl, pm)
        root.right = _construct(im+1, ir, pm, pr-1)
        return root
    return _construct(0, len(inorder), 0, len(postorder))

class Solution:
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        return build_tree(inorder, postorder)
