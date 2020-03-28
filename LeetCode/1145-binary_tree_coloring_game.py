# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def btreeGameWinningMove(self, root: TreeNode, n: int, x: int) -> bool:
        nodes = [None] * n
        parents = [None] * n
        tsizes = [-1] * n
        def preprocess(tree, parent):
            if not tree:
                return 0
            parents[tree.val-1] = parent
            nodes[tree.val-1] = tree
            siz = 1 + preprocess(tree.left, tree) + preprocess(tree.right, tree)
            tsizes[tree.val-1] = siz
            return siz
        preprocess(root, None)
        #
        tsiz = tsizes[root.val-1]
        xsiz = tsizes[x-1]
        # choose parent of x
        if parents[x-1]:
            if tsiz - xsiz > xsiz:
                return True
        # choose left subtree of x
        l = nodes[x-1].left
        if l:
            lsiz = tsizes[l.val-1]
            if lsiz > tsiz - lsiz:
                return True
        # choose right subtree of x
        r = nodes[x-1].right
        if r:
            rsiz = tsizes[r.val-1]
            if rsiz > tsiz - rsiz:
                return True
        # cannot ensure
        return False
