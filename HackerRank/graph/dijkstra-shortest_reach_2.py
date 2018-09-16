#!/bin/python3
# https://www.hackerrank.com/challenges/dijkstrashortreach/problem

import math
import heapq
from sys import stdin, stdout, stderr

def dijkstra2(n, edges, s):
    costs = [-1] * n
    visited = [False] * n
    # initialise
    costs[s] = 0
    queue = [(0, s)]
    #
    while len(queue) > 0:
        (c, u) = heapq.heappop(queue)
        if visited[u]:
            continue
        visited[u] = True
        costs[u] = c
        for (v, w) in edges(u):
            if not visited[v] and (costs[v] == -1 or costs[v] > costs[u] + w):
                costs[v] = costs[u] + w
                heapq.heappush(queue, (costs[u] + w, v))
    return costs

def shortestReach(n, edges, s):
    costs = dijkstra2(n, edges, s)
    return list(map(lambda x: x[1], filter(lambda x: x[0] != s, enumerate(costs))))

if __name__ == '__main__':
    for _ in range(int(stdin.readline().strip())):
        # Allocate memory
        n, m = map(int, stdin.readline().strip().split())
        adjl = [set() for _ in range(n)]
        adjm = [[math.inf] * n for _ in range(n)]
        # Read edges
        for _ in range(m):
            u, v, w = map(int, stdin.readline().strip().split())
            u, v = u-1, v-1
            if u == v:
                continue
            adjm[u][v] = min(adjm[u][v], w)
            adjm[v][u] = min(adjm[v][u], w)
            adjl[u].add(v)
            adjl[v].add(u)
        s = int(stdin.readline().strip())
        # Compute
        def edges(u):
            for v in adjl[u]:
                yield (v, adjm[u][v])
        result = shortestReach(n, edges, s-1)
        stdout.write(' '.join(map(str, result)) + '\n')
