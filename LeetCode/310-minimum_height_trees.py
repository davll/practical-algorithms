# https://leetcode.com/problems/minimum-height-trees/
# https://www.geeksforgeeks.org/roots-tree-gives-minimum-height/

from collections import deque

def find_mht_v1(n, edges):
    graph = make_graph(n, edges)
    result = []
    mindepth = n * 2
    for i in range(n):
        depth = [-1] * n
        depth[i] = 0
        queue = deque([i])
        while queue:
            u = queue.popleft()
            for v in graph[u]:
                if depth[v] == -1:
                    depth[v] = depth[u] + 1
                    queue.append(v)
        d = max(depth)
        if mindepth > d:
            mindepth = d
            result = [i]
        elif mindepth == d:
            result.append(i)
    return result

# Idea: Trim Leaves
def find_mht_v2(n, edges):
    if n == 1:
        return [0]
    graph = make_graph(n, edges)
    degree = [len(graph[i]) for i in range(n)]
    queue = deque(i for i in range(n) if degree[i] == 1)
    while n > 2:
        num_leaves = len(queue)
        n -= num_leaves
        for _ in range(num_leaves):
            u = queue.popleft()
            for v in graph[u]:
                degree[v] -= 1
                if degree[v] == 1:
                    queue.append(v)
    return list(queue)

def make_graph(n, edges):
    graph = [[] for _ in range(n)]
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    return graph

class Solution:
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        return find_mht_v2(n, edges)
