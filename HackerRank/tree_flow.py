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

def fast_tree_flow(n, caps, source, sink):
    pass

def fill_caps(n, adj, caps):
    # do bfs to fill caps
    for i in range(n):
        visited = [False] * n
        q = deque()
        q.append(i)
        while len(q) > 0:
            u = q.popleft()
            visited[u] = True
            for v in adj[u]:
                if not visited[v]:
                    caps[i][v] = caps[i][u] + caps[u][v]
                    q.append(v)

#
# Complete the treeFlow function below.
#
def treeFlow(n, caps):
    return ford_fulkerson(n, caps, 0, n-1)

if __name__ == '__main__':
    n = int(input())
    adj = [[] for _ in range(n)]
    #caps = [[0] * n for _ in range(n)]
    for _ in range(n-1):
        u, v, w = map(int, input().rstrip().split())
        u, v = u-1, v-1
        adj[u].append((v, w))
        adj[v].append((u, w))
        #caps[u][v] += w
        #caps[v][u] += w
    print("input complete", file = stderr)
    #fill_caps(n, adj, caps)
    #print(str(caps), file = stderr)
    #result = treeFlow(n, caps)
    #print(str(result))
