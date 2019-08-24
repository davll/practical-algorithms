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
        yield tree.val
        for node in tree.children:
            yield from dfs(node)
    return list(dfs(root))

def traverse_v2(root):
    if not root:
        return []
    result = []
    stack = [[-1,root]]
    while stack:
        child, node = stack[-1]
        if child == -1:
            result.append(node.val)
            stack[-1][0] = 0
        elif child < len(node.children):
            stack[-1][0] = child + 1
            stack.append([-1, node.children[child]])
        else:
            stack.pop()
    return result

def traverse_v3(root):
    if not root:
        return []
    result = []
    stack = [root]
    while stack:
        node = stack.pop()
        result.append(node.val)
        stack.extend(reversed(node.children))
    return result

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        return traverse_v3(root)
