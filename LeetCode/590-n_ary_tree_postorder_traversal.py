"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""

def traverse_v1(root):
    def dfs(tree):
        if not tree:
            return
        for node in tree.children:
            yield from dfs(node)
        yield tree.val
    return list(dfs(root))

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        return traverse_v1(root)
