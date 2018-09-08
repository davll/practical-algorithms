#!/bin/python3
# https://www.hackerrank.com/challenges/dijkstrashortreach/problem

import math
import heapq

def dijkstra(n, edges, s):
    pendings = set()
    visited = [False] * n
    costs = [math.inf] * n
    costs[s] = 0
    pendings.add(s)
    def candidates():
        for _ in range(n):
            v = -1
            for i in pendings:
                assert i in range(0, n)
                assert not visited[i]
                if v == -1 or costs[v] > costs[i]:
                    v = i
            if v != -1:
                pendings.remove(v)
                visited[v] = True
                yield v
            else:
                break
    def relax(v):
        for (t, w) in edges[v]:
            if not visited[t]:
                if costs[t] > costs[v] + w:
                    costs[t] = costs[v] + w
                    pendings.add(t)
    for i in candidates():
        relax(i)
    for i in range(n):
        if math.isinf(costs[i]):
            costs[i] = -1
    return costs

def shortestReach(n, edges, s):
    costs = dijkstra(n, edges, s)
    return list(map(lambda x: x[1], filter(lambda x: x[0] != s, enumerate(costs))))

if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        n, m = map(int, input().split())
        edges = [[] for _ in range(n)]
        for _ in range(m):
            u, v, w = map(int, input().rstrip().split())
            u, v = u-1, v-1
            edges[u].append((v, w))
            edges[v].append((u, w))
        s = int(input())
        result = shortestReach(n, edges, s-1)
        print(' '.join(map(str, result)))
