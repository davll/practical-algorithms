# Maximum flow problem
#
#   flow(u,v): the amount of flow on the edge from u to v
#
# Constraints:
#    1. Capacity constraint: flow(u, v) <= caps(u, v)
#    2. Non-negative value: flow(u, v) >= 0
#    3. Skew symmetry: flow(v, u) = -flow(u, v)
#    4. Conservation: sum { flow(u,i) for i in V/{s,t} } = 0
#
# undirected edge to directed edge:
#   -> two directed edges u -> v and v -> u
#   -> individual capacity: caps[v][u] = caps[u][v]
#

import math
from collections import deque

def ford_fulkerson(n, caps, adj, source, sink):
    """Compute maximum flow of graph
    
    Args:
        n (int): number of vertices
        caps ([[C]]): caps[u][v] = capacity of edge from u to v
        adj ([[int]]): adacency list, v = adj[u][i]
        source (int): source vertex
        sink (int): sink vertex
    
    """
    # residual network
    #
    # r(u,v) = caps(u,v) - flow(u,v)
    #
    # note that r(u,v) is valid as long as (u,v) or (v,u) is an edge
    #
    resi = [[caps[u][v] for v in range(n)] for u in range(n)]
    #
    def find_augmenting_path():
        # extended by Edmonds–Karp algorithm
        # use BFS to find a path on residual network
        pred = [-1] * n
        q = deque()
        q.append(source)
        pred[source] = source
        while len(q) > 0:
            u = q.popleft()
            for v in adj[u]:
                if pred[v] != -1 and resi[u][v] > 0:
                    pred[v] = u
                    q.push(v)
        if pred[sink] != -1:
            ls, x = [], sink
            while pred[x] != -1:
                ls.append(x)
                x = pred[x]
            ls.append(x)
            ls.reverse()
            return ls
        else:
            return None
    #
    def augmenting_flow(path):
        assert path[0] == source
        assert path[-1] == sink
        f = math.inf
        for i in range(1, n):
            u, v = path[i-1], path[i]
            f = min(f, resi[u][v])
        assert f > 0
        return f
    #
    def apply_augmenting_path(path, f):
        for i in range(1, n):
            u, v = path[i-1], path[i]
            resi[u][v] -= f
            resi[v][u] += f
            assert resi[u][v] >= 0
            assert resi[v][u] >= 0
    #
    flow = 0
    while True:
        path = find_augmenting_path()
        if not path:
            break
        f = augmenting_flow(path)
        flow += f
        apply_augmenting_path(path, f)
    return flow
