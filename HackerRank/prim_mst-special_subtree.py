#!/bin/python3

import math
import os
#import random
#import re
import sys

# Complete the prims function below.
def prims(n, edges, s):
    pendings = set()
    visited = [False] * n
    costs = [float('inf')] * n
    weight = 0
    # the starting point is in MST
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
                if costs[t] > w:
                    costs[t] = w
                    pendings.add(t)
    for i in candidates():
        weight += costs[i]
        relax(i)
    return weight

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n, m = map(int, input().split())

    edges = [[] for _ in range(n)]
    for _ in range(m):
        u, v, w = map(int, input().rstrip().split())
        u, v = u-1, v-1
        edges[u].append((v, w))
        edges[v].append((u, w))

    start = int(input())

    result = prims(n, edges, start-1)

    fptr.write(str(result) + '\n')
    fptr.close()
