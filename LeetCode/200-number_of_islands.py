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

class Solution:
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0
        elif not grid[0]:
            return 0
        m, n = len(grid), len(grid[0])
        def make_key(i,j):
            return i * n + j
        sets = UnionFind(m * n + 1)
        # combine water
        for i in range(0, m):
            for j in range(0, n):
                if grid[i][j] == '0':
                    sets.union(make_key(i,j), m*n)
        # combine lands horizontally
        for i in range(0, m):
            for j in range(1, n):
                if grid[i][j] == '1' and grid[i][j-1] == '1':
                    sets.union(make_key(i,j), make_key(i,j-1))
        # combine lands vertically
        for i in range(1, m):
            for j in range(0, n):
                if grid[i][j] == '1' and grid[i-1][j] == '1':
                    sets.union(make_key(i,j), make_key(i-1,j))
        # return results
        return sets.count()-1
