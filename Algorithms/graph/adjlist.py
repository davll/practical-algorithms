# Adjacency List

class Graph:
    def __init__(self, n):
        self._num_vertices = n
        self._edges = [[] for _ in range(n)]
    #
    def __len__(self):
        return self._num_vertices
    #
    def edges_from(self, u):
        return ((v,w) for (v,w) in self._edges[u])
    #
    def outdegree(self, u):
        return len(self._edges[u])
    #
    def add_edge(self, u, v, w = None):
        self._edges[u].append((v, w))
    #
    def indegrees(self):
        indegree = [0] * len(self)
        for v in (v for vs in self._edges for (v,_) in vs):
            indegree[v] += 1
        return indegree
    #
    def transposed(self):
        n = len(self)
        g = Graph(n)
        for u in range(0, n):
            for (v, w) in self.edges_from(u):
                g.add_edge(v, u, w)
        return g
