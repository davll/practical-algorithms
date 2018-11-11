# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def dfs(root, buffer):
    if not root:
        return
    buffer.append(root.val)
    if not root.left and not root.right:
        yield '->'.join(map(str, buffer))
    else:
        yield from dfs(root.left, buffer)
        yield from dfs(root.right, buffer)
    buffer.pop()

class Solution:
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        return list(dfs(root, []))
