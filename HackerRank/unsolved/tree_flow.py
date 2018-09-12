#!/bin/python3
# https://www.hackerrank.com/challenges/tree-flow/problem

import math
#import numpy
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

def fast_tree_flow(n, adj):
    source, sink = 0, n-1
    # Build tree
    root = source
    dist, parent, depth = [0] * n, [-1] * n, [0] * n
    branch = [-1] * n
    visited = [False] * n
    parent[root] = root
    branch[root] = root
    # BFS
    q = deque()
    q.append(root)
    while len(q) > 0:
        u = q.popleft()
        visited[u] = True
        if sum(map(lambda _: 1, filter(lambda e: not visited[e[0]], adj[u]))) > 1:
            branch[u] = u
        for (v, w) in adj[u]:
            if not visited[v]:
                dist[v] = dist[u] + w
                depth[v] = depth[u] + 1
                parent[v] = u
                branch[v] = branch[u]
                q.append(v)
    # lowest common ancestor
    def lca_slow(a, b):
        d = min(depth[a], depth[b])
        while depth[a] > d:
            a = parent[a]
        while depth[b] > d:
            b = parent[b]
        while a != b:
            a, b = parent[a], parent[b]
        return a
    def lca(a, b):
        while a != b:
            if depth[a] > depth[b]:
                if branch[a] == a:
                    a = parent[a]
                else:
                    a = branch[a]
            else:
                if branch[b] == b:
                    b = parent[b]
                else:
                    b = branch[b]
        return a
    #
    def caps(a, b):
        return dist[a] + dist[b] - 2 * dist[lca(a, b)]
    flow = caps(source, sink)
    for i in range(1, n-1):
        # flow += min(caps(source, i), caps(i, sink))
        flow += dist[i] + min(0, dist[sink] - 2 * dist[lca(i, sink)])
    return flow

#
# Complete the treeFlow function below.
#
def treeFlow(n, adj):
    return fast_tree_flow(n, adj)

if __name__ == '__main__':
    n = int(input())
    adj = [[] for _ in range(n)]
    for _ in range(n-1):
        u, v, w = map(int, input().rstrip().split())
        u, v = u-1, v-1
        adj[u].append((v, w))
        adj[v].append((u, w))
    result = treeFlow(n, adj)
    print(str(result))
