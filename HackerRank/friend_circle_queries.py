from sys import stdin, stdout, stderr

class FriendCircle:
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
    #
    def size(self, p):
        return self._sz[self.find(p)]

def max_circle(queries):
    id_map = {}
    for x, y in queries:
        if x not in id_map:
            id_map[x] = len(id_map)
        if y not in id_map:
            id_map[y] = len(id_map)
    n = len(id_map)
    fc = FriendCircle(n)
    max_sz = 1
    for x, y in queries:
        x, y = id_map[x], id_map[y]
        fc.union(x, y)
        max_sz = max(max_sz, fc.size(x))
        yield max_sz

if __name__ == "__main__":
    queries = []
    for _ in range(int(stdin.readline().strip())):
        a, b = map(int, stdin.readline().strip().split())
        queries.append((a, b))
    for x in max_circle(queries):
        stdout.write(str(x) + '\n')
