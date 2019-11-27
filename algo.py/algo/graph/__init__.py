# Adjacency List

from collections import namedtuple

Edge = namedtuple('Edge', ['u', 'v', 'w'])

class Graph:
    def __init__(self, n):
        self._num_vertices = n
        self._edges = [[] for _ in range(n)]
        self._outdegrees = [0] * n
        self._indegrees = [0] * n
    #
    def __len__(self):
        return self._num_vertices
    #
    def edges_from(self, u):
        return [Edge(u,v,w) for (u,v,w) in self._edges[u]]
    #
    def outdegree(self, u):
        return self._outdegrees[u]
    #
    def add_edge(self, u, v, w = None):
        self._edges[u].append(Edge(u, v, w))
        self._outdegrees[u] += 1
        self._indegrees[v] += 1
    #
    def indegree(self, u):
        return self._indegrees[u]
    #
    def transposed(self):
        n = len(self)
        g = Graph(n)
        for u in range(0, n):
            for (_u, v, w) in self.edges_from(u):
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
                yield Edge(u, v, w)
            else:
                yield Edge(v, u, w)
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
