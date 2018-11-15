# https://leetcode.com/problems/cheapest-flights-within-k-stops/description/

from math import inf, isinf
from collections import defaultdict
from heapq import heappush, heappop

# Idea: Dijkstra
#
# cost[k, u] = minimum cost from source to u with exactly k steps
#
def dijkstra_v1(graph, source, destination, nstops):
    costs = defaultdict(lambda: inf)
    maxsteps = nstops + 1
    # entry = (cost, steps, vertex)
    queue = [(0, 0, source)]
    while queue:
        cu, k, u = heappop(queue)
        if k > maxsteps or cu > costs[k, u]:
            continue
        costs[k, u] = cu
        if u == destination:
            return cu
        for v, w in graph[u]:
            heappush(queue, (cu + w, k+1, v))
    return -1

# Idea: Dynamic Programming
#
# cost[k; v] = minimum cost from source to v within k steps
#
# cost[k; v] = min {
#                 cost[k-1; v]
#                 cost[k-1; u] + edge[u,v] for all edges (u,v)
#              }
#
# cost[0; source] = 0
#
def dp_v1(n, edges, source, destination, nstops):
    dp0, dp1 = [[inf] * n for _ in range(2)]
    dp0[source] = 0
    for _ in range(nstops+1):
        dp1[:] = dp0[:]
        for u, v, w in edges:
            dp1[v] = min(dp1[v], dp0[u] + w)
        dp0, dp1 = dp1, dp0
    #
    if isinf(dp0[destination]):
        return -1
    else:
        return dp0[destination]

class Solution:
    def findCheapestPrice(self, n, flights, src, dst, K):
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type K: int
        :rtype: int
        """
        #graph = edges2adj(n, flights)
        #return dijkstra_v1(graph, src, dst, K)
        return dp_v1(n, flights, src, dst, K)

def edges2adj(N, edges):
    graph = [[] for _ in range(N)]
    for u, v, w in edges:
        graph[u].append((v, w))
    return graph
