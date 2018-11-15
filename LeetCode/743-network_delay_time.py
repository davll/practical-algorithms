# https://leetcode.com/problems/network-delay-time/

from heapq import heappush, heappop

def dijkstra_v1(graph, source):
    n = len(graph)
    costs = [-1] * n
    queue = [(0, source)]
    while queue:
        d, u = heappop(queue)
        if costs[u] != -1:
            continue
        costs[u] = d
        for v, w in graph[u]:
            heappush(queue, (d + w, v))
    if any(map(lambda x: x == -1, costs)):
        return -1
    return max(costs)

class Solution:
    def networkDelayTime(self, times, N, K):
        """
        :type times: List[List[int]]
        :type N: int
        :type K: int
        :rtype: int
        """
        graph = edges2adj(N, times)
        src = K - 1
        return dijkstra_v1(graph, src)


def edges2adj(N, edges):
    graph = [[] for _ in range(N)]
    for u, v, w in edges:
        graph[u-1].append((v-1, w))
    return graph
