# https://leetcode.com/problems/clone-graph/description/

# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

from collections import deque

def clone_v1(root):
    table = {}
    queue = deque([root])
    # copy nodes
    while queue:
        old = queue.popleft()
        if not old or old.label in table:
            continue
        new = UndirectedGraphNode(old.label)
        table[old.label] = new
        for neighbour in old.neighbors:
            new.neighbors.append(neighbour.label)
            if neighbour.label not in table:
                queue.append(neighbour)
    # redirect neighbours
    for node in table.values():
        node.neighbors = list(map(lambda k: table[k], node.neighbors))
    #
    return table[root.label]

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        if not node:
            return None
        return clone_v1(node)
