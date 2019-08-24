"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""

from collections import deque

def bfs(root):
    level = -1
    result = []
    q = deque([(0, root)])
    while q:
        lv, node = q.popleft()
        if level < lv:
            result.append([node.val])
            level = lv
        else:
            result[-1].append(node.val)
        q.extend((lv+1, x) for x in node.children)
    return result

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
        return bfs(root)
