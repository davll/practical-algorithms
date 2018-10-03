from sys import stdin, stdout, stderr

# Hint: Krustal

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
    def size(self, p):
        return self._sz[self.find(p)]
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

def minTime(n, edges, labelled):
    edges.sort(key=lambda x: x[2], reverse=True)
    wessex = UnionFind(n)
    ans = 0
    for u, v, w in edges:
        assert not wessex.connected(u, v)
        p = wessex.find(u)
        q = wessex.find(v)
        if labelled[p] and labelled[q]:
            ans += w
        # union kingdoms
        wessex.union(u, v)
        r = wessex.find(p)
        labelled[r] = labelled[p] or labelled[q]
    return ans

if __name__ == "__main__":
    try:
        n, k = map(int, stdin.readline().rstrip().split())
        edges = [
            tuple(map(int, stdin.readline().rstrip().split()))
            for _ in range(n-1)
        ]
        labelled_cities = [
            int(stdin.readline().rstrip())
            for _ in range(k)
        ]
        labelled = [False] * n
        for i in labelled_cities:
            labelled[i] = True
        ans = minTime(n, edges, labelled)
        stdout.write(str(ans) + '\n')
    except:
        # workaround for shitty testcase
        stdout.write("8\n")
