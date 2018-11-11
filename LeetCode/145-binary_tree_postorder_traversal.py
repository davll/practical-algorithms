# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def dfs_v1(root):
    if not root:
        return
    yield from dfs_v1(root.left)
    yield from dfs_v1(root.right)
    yield root.val

def dfs_v2(root):
    stack = [(root, 0)]
    while stack:
        node, state = stack.pop()
        if not node:
            continue
        if state == 0:
            stack.append((node, 1))
            stack.append((node.left, 0))
        elif state == 1:
            stack.append((node, 2))
            stack.append((node.right, 0))
        else:
            yield node.val

class Solution:
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        return list(dfs_v2(root))
