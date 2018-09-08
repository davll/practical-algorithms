#!/bin/python3
# https://www.hackerrank.com/challenges/journey-to-the-moon/problem

import math

class UnionFind:
    """Disjointed Set (Union Find)
    """
    def __init__(self, n):
        self._id = list(range(n))
        self._sz = [1] * n
        self._count = n
    #
    def find(self, p):
        t = p
        while p != self._id[p]:
            p = self._id[p]
        self._id[t] = p
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

def method1(n, edges):
    nationality = UnionFind(n)
    for (i,j) in edges:
        nationality.union(i, j)
    nations = [0] * n
    for i in range(n):
        p = nationality.find(i)
        nations[p] += 1
    values = [x for x in nations if x > 1]
    m = len(values)
    ans = 0
    for x in nations:
        if x == 1:
            ans += 1
    result = ans * (ans - 1) // 2
    for i in range(m):
        for j in range(i+1, m):
            result += values[i] * values[j]
    for i in range(m):
        result += values[i] * ans
    return result

# Complete the journeyToMoon function below.
def journeyToMoon(n, edges):
    return method1(n, edges)

if __name__ == '__main__':
    n, p = map(int, input().split())
    edges = []
    for _ in range(p):
        edges.append(tuple(map(int, input().rstrip().split())))

    result = journeyToMoon(n, edges)
    print(str(result))
