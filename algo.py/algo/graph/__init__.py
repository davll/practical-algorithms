# Adjacency List

from collections import namedtuple

Edge = namedtuple('Edge', ['u', 'v', 'w'])
OutEdge = namedtuple('OutEdge', ['v', 'w'])

class Graph:
    def __init__(self, n):
        self._num_vertices = n
        self._edges = [[] for _ in range(n)]
    #
    def __len__(self):
        return self._num_vertices
    #
    def edges_from(self, u):
        return (OutEdge(v,w) for (v,w) in self._edges[u])
    #
    def outdegree(self, u):
        return len(self._edges[u])
    #
    def add_edge(self, u, v, w = None):
        self._edges[u].append(OutEdge(v, w))
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

# Undirected Graph
class UGraph:
    def __init__(self, n):
        self._num_vertices = n
        self._edges = []
        self._adj = [[] for _ in range(n)]
    #
    def __len__(self):
        return self._num_vertices
    #
    def edges_from(self, x):
        for (u,v,w) in map(lambda i: self._edges[i], self._adj[x]):
            if u == x:
                yield (v, w)
            else:
                yield (u, w)
    #
    def degree(self, u):
        return len(self._adj[u])
    #
    def add_edge(self, u, v, w = None):
        i = len(self._edges)
        self._edges.append(Edge(u, v, w))
        self._adj[u].append(i)
        self._adj[v].append(i)
    #
    def edges(self):
        return (e for e in self._edges)
