#!/bin/python3
# https://www.hackerrank.com/challenges/tree-flow/problem

import math
from sys import stderr
from collections import deque

def ford_fulkerson(n, caps, source, sink):
    # residual network
    resi = [[caps[u][v] for v in range(n)] for u in range(n)]
    #
    def find_augmenting_path():
        pred = [-1] * n
        q = deque()
        q.append(source)
        while len(q) > 0:
            u = q.popleft()
            for v in range(n):
                if pred[v] == -1 and v != source and resi[u][v] > 0:
                    pred[v] = u
                    q.append(v)
        if pred[sink] != -1:
            ls, x = [], sink
            while pred[x] != -1:
                ls.append(x)
                x = pred[x]
            ls.append(x)
            ls.reverse()
            return ls
        else:
            return None
    #
    def augmenting_flow(path):
        f = math.inf
        for i in range(1, len(path)):
            u, v = path[i-1], path[i]
            f = min(f, resi[u][v])
        return f
    #
    def apply_augmenting_path(path, f):
        for i in range(1, len(path)):
            u, v = path[i-1], path[i]
            resi[u][v] -= f
            resi[v][u] += f
    #
    flow = 0
    while True:
        path = find_augmenting_path()
        if not path:
            break
        f = augmenting_flow(path)
        flow += f
        apply_augmenting_path(path, f)
    return flow

#
# Complete the treeFlow function below.
#
def treeFlow(n, caps):
    return ford_fulkerson(n, caps, 0, n-1)

if __name__ == '__main__':
    n = int(input())
    edges = []
    caps = [[math.inf] * n for _ in range(n)]
    for _ in range(n-1):
        u, v, w = map(int, input().rstrip().split())
        u, v = u-1, v-1
        edges.append((u, v, w))
        if math.isinf(caps[u][v]):
            caps[u][v] = w
        else:
            caps[u][v] += w
        if math.isinf(caps[v][u]):
            caps[v][u] = w
        else:
            caps[v][u] += w
    for i in range(n):
        caps[i][i] = 0
    for k in range(n):
        for i in range(n):
            for j in range(n):
                caps[i][j] = min(caps[i][j], caps[i][k] + caps[k][j])
    for i in range(n):
        for j in range(n):
            if math.isinf(caps[i][j]):
                caps[i][j] = 0
    #print(str(caps), file = stderr)
    result = treeFlow(n, caps)
    print(str(result))
