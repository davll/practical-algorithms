# https://leetcode.com/problems/recover-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def inorder(root):
    if not root:
        return
    yield from inorder(root.left)
    yield root
    yield from inorder(root.right)

def recover_bst_v1(root):
    a = list(inorder(root))
    b = a[:]
    b.sort(key=lambda t: t.val)
    # find mismatch
    for x, y in zip(a, b):
        if x.val != y.val:
            x.val, y.val = y.val, x.val
            break

def recover_bst_v2(root):
    raise NotImplementedError()

class Solution:
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        recover_bst_v1(root)
