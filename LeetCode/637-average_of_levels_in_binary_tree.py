# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque

def avglevel(root):
    values = []
    counts = []
    queue = deque()
    queue.append((root, 0))
    while queue:
        node, level = queue.popleft()
        if not node:
            continue
        if level >= len(values):
            d = level + 1 - len(values)
            values += [0] * d
            counts += [0] * d
        values[level] += node.val
        counts[level] += 1
        if node.left:
            queue.append((node.left, level+1))
        if node.right:
            queue.append((node.right, level+1))
    #
    return list(map(lambda t: t[0] / t[1], zip(values, counts)))

class Solution:
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        return avglevel(root)
