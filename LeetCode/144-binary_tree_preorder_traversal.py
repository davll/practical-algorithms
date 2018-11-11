# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def dfs_v1(root):
    if not root:
        return
    yield root.val
    yield from dfs_v1(root.left)
    yield from dfs_v1(root.right)

def dfs_v2(root):
    stack = [root]
    while stack:
        node = stack.pop()
        if not node:
            continue
        yield node.val
        stack.append(node.right)
        stack.append(node.left)

class Solution:
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        return list(dfs_v2(root))
