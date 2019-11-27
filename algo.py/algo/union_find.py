# Union-Find (Disjointed Set)
#
# https://en.wikipedia.org/wiki/Disjoint-set_data_structure#Time_complexity
# https://en.wikipedia.org/wiki/Proof_of_O(log*n)_time_complexity_of_union%E2%80%93find
# https://cs.stackexchange.com/questions/96401/why-time-complexity-of-union-find-is-olgn-with-only-union-by-rank
# https://stackoverflow.com/questions/34460492/time-complexity-of-array-based-disjoint-set-data-structure

class UnionFind:
    """
    Disjointed Set (Union Find)
    
    Space Complexity: O(n)
    Time Complexity: O(a(n)) where a(n) < 5
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
    def size(self, p):
        return self._sz[self.find(p)]
    #
    def connected(self, p, q):
        return self.find(p) == self.find(q)
    # 
    @property
    def count(self):
        """
        Number of sets
        """
        return self._count
    #
    def union(self, p, q):
        """
        Merge two sets
        """
        i, j = self.find(p), self.find(q)
        if i == j:
            return
        # make smaller tree point to larger one
        if self._sz[i] < self._sz[j]:
            self._id[i] = j
            self._sz[j] += self._sz[i]
        else:
            self._id[j] = i
            self._sz[i] += self._sz[j]
        # decrease the counter because two sets are merged into one
        self._count -= 1
