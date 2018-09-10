# https://www.hackerrank.com/challenges/torque-and-development/problem?h_r=internal-search

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
    @property
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

# Complete the roadsAndLibraries function below.
def roadsAndLibraries(n, c_lib, c_road, edges):
    uf = UnionFind(n)
    for (u,v) in edges:
        uf.union(u, v)
    count = [0] * n
    for i in range(n):
        count[uf.find(i)] += 1
    ans = 0
    for x in filter(lambda x: x > 0, count):
        cand1 = c_lib * x
        cand2 = c_lib + c_road * (x - 1)
        ans += min(cand1, cand2)
    return ans

if __name__ == '__main__':
    for _ in range(int(input())):
        n, m, c_lib, c_road = map(int, input().split())
        cities = []
        for _ in range(m):
            u, v = map(int, input().rstrip().split())
            u, v = u-1, v-1
            cities.append((u, v))
        result = roadsAndLibraries(n, c_lib, c_road, cities)
        print(str(result))
