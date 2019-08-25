# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def cvtbst_v1(root):
    def dfs(tree, bonus):
        if not tree:
            return (None, bonus)
        right2, br = dfs(tree.right, bonus)
        left2, bl = dfs(tree.left, br + tree.val)
        tree2 = TreeNode(tree.val + br)
        tree2.right = right2
        tree2.left = left2
        return (tree2, bl)
    root2, _ = dfs(root, 0)
    return root2

class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        return cvtbst_v1(root)
