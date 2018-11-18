# https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/

from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def bfs_zigzag(root):
    if not root:
        return []
    result = []
    queue1 = deque([(root, 0)])
    queue2 = deque()
    while queue1:
        node, lv = queue1.popleft()
        if lv == len(result):
            result.append([])
        result[lv].append(node.val)
        if node.left:
            queue2.append((node.left, lv+1))
        if node.right:
            queue2.append((node.right, lv+1))
        if not queue1:
            queue1, queue2 = queue2, queue1
    for i, r in enumerate(result):
        if i % 2 == 1:
            r.reverse()
    return result

class Solution:
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        return bfs_zigzag(root)
