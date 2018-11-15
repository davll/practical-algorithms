# https://leetcode.com/problems/shortest-path-visiting-all-nodes/

from collections import deque, defaultdict

# Idea: BFS
#
# Define state:
#   state = (cover, head)
#   cover = the set of nodes that is covered by a path sor far
#   head = the current node
#
def bfs_v1(graph):
    N = len(graph)
    GOAL = 2**N - 1
    #
    distance = defaultdict(lambda: N * N)
    for x in range(N):
        distance[(1 << x), x] = 0
    #
    queue = deque(((1 << x), x) for x in range(N))
    while queue:
        cover, head = queue.popleft()
        dist = distance[cover, head]
        if cover == GOAL:
            return dist
        for child in graph[head]:
            cover2 = cover | (1 << child)
            if dist + 1 < distance[cover2, child]:
                distance[cover2, child] = dist + 1
                queue.append((cover2, child))

# Idea: Dynamic Programming
#
#
def dp_v1(graph):
    N = len(graph)
    distance = [[float('inf')] * N for _ in range(1 << N)]
    for x in range(N):
        distance[1 << x][x] = 0
    for cover in range(1 << N):
        repeat = True
        while repeat:
            repeat = False
            for head, d in enumerate(distance[cover]):
                for neighbour in graph[head]:
                    cover2 = cover | (1 << neighbour)
                    if d + 1 < distance[cover2][neighbour]:
                        distance[cover2][neighbour] = d + 1
                        if cover == cover2:
                            repeat = True
    return min(distance[2**N-1])

class Solution:
    def shortestPathLength(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: int
        """
        return bfs_v1(graph)
