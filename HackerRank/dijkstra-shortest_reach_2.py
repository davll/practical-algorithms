#!/bin/python3

import math
import os
import random
import re
import sys
import heapq

def dijkstra(n, edges, s):
    pendings = set(range(n))
    costs = [-1 for _ in range(n)]
    costs[s] = 0
    def candidates():
        for i in pendings:
            if costs[i] != -1:
                yield (i, costs[i])
    def extract():
        while len(pendings) > 0:
            result = min(candidates(), default = None, key = lambda x: x[1])
            if result:
                (i, _) = result
                pendings.remove(i)
                yield i
            else:
                break
    def relax(v):
        for (t, w) in edges[v]:
            if t in pendings:
                if costs[t] == -1 or costs[t] > costs[v] + w:
                    costs[t] = costs[v] + w
    for i in extract():
        relax(i)
    return costs

class _PQEdge:
    def __init__(self, u, v, w):
        self.u = u
        self.v = v
        self.w = w
    def __eq__(self, other):
        return self.w == other.w
    def __lt__(self, other):
        return self.w < other.w
    def __gt__(self, other):
        return self.w > other.w
    def __le__(self, other):
        return self.w <= other.w
    def __ge__(self, other):
        return self.w >= other.w

def dijkstra2(n, edges, s):
    visited = [False] * n
    costs = [-1] * n
    costs[s] = 0
    visited[s] = True
    queue, u = [], s
    for _ in range(n):
        for (v, w) in edges[u]:
            if not visited[v]:
                heapq.heappush(queue, _PQEdge(u, v, costs[u] + w))
        def smallest_edge():
            while len(queue) > 0:
                x = heapq.heappop(queue)
                if not visited[x.v]:
                    return x
            return None
        e = smallest_edge()
        if not e:
            break
        u = e.v
        costs[u] = e.w
        visited[u] = True
    return costs

def shortestReach(n, edges, s):
    adj = [[] * n for _ in range(n)]
    for e in edges:
        u, v, w = e[0]-1, e[1]-1, e[2]
        adj[u].append((v, w))
        adj[v].append((u, w))
    costs = dijkstra2(n, adj, s-1)
    return list(map(lambda x: x[1], filter(lambda x: x[0] != s-1, enumerate(costs))))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        nm = input().split()

        n = int(nm[0])

        m = int(nm[1])

        edges = []

        for _ in range(m):
            edges.append(list(map(int, input().rstrip().split())))

        s = int(input())

        result = shortestReach(n, edges, s)

        #print(' '.join(map(str, result)))
        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
