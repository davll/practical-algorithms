# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def path_sum(root, k, path):
    assert root
    path.append(root.val)
    k -= root.val
    if k == 0:
        if not root.left and not root.right:
            yield path[:]
    if root.left:
        yield from path_sum(root.left, k, path)
    if root.right:
        yield from path_sum(root.right, k, path)
    x = path.pop()
    assert x == root.val

class Solution:
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        if not root:
            if sum == 0:
                return []
            else:
                return []
        return list(path_sum(root, sum, []))
