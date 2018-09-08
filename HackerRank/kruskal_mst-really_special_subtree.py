#!/bin/python3
# https://www.hackerrank.com/challenges/kruskalmstrsub/problem

class UnionFind:
    """
    """
    def __init__(self, n):
        self._id = list(range(n))
        self._sz = [1] * n
        self._count = n
    #
    def find(self, p):
        while p != self._id[p]:
            p = self._id[p]
        return p
    #
    def depth(self, p):
        k = 0
        while p != self._id[p]:
            p = self._id[p]
            k += 1
        return k
    #
    def connected(self, p, q):
        return self.find(p) == self.find(q)
    # 
    def count(self):
        return self._count
    #
    def union(self, p, q):
        i, j = self.find(p), self.find(q)
        if i == j:
            return
        # make smaller root point to larger one
        if self._sz[i] < self._sz[j]:
            self._id[i] = j
            self._sz[j] += self._sz[i]
        else:
            self._id[j] = i
            self._sz[i] += self._sz[j]
        # decrease the counter
        self._count -= 1

def mst_kruskal(n, edges):
    mst, cost = [], 0
    edges.sort(key = lambda x: x[2])
    group = UnionFind(n)
    for (u, v, w) in edges:
        if group.find(u) != group.find(v):
            #mst.append((u, v, w))
            cost += w
            group.union(u, v)
    return cost

if __name__ == '__main__':
    g_nodes, g_edges = map(int, input().split())

    edges = [tuple(map(int, input().split())) for _ in range(g_edges)]
    for i in range(len(edges)):
        (u, v, w) = edges[i]
        edges[i] = (u-1, v-1, w)
    cost = mst_kruskal(g_nodes, edges)
    print(str(cost))
