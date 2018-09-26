class MST:
    """Minimum Spanning Tree

    Attributes:
        n (int): number of vertices
        w (T): weight of the MST
        s (int): index of starting vertex
        parents ([int]): previous vertex of vertex v

    """
    #
    def __init__(self, n, w, s, parents):
        self.n = n
        self.w = w
        self.s = s
        self.parents = parents

def mst_prim(n, edges, s):
    """Find a minimum spanning tree from an undirected graph

    Args:
        n (int): number of vertices
        edges ([[(int, W)]]): adjacency list, (v, w) = edges[u][i] denotes an edge (u->v) with weight w
        s (int): index of starting vertex

    Returns:
        MST: minimum spanning tree

    """
    # pending: the set of unvisited vertices with finitie costs[v] (not infinite)
    pendings = set()
    # visited[v] = True if visited
    visited = [False] * n
    # costs[v] = distance betweem v and mst
    # parents[v] = previous vertex of vertex v
    costs, parents = [math.inf] * n, [-1 for _ in range(n)]
    # process source vertex in the beginning
    costs[s] = 0
    pendings.add(s)
    # extract candidates for relaxation
    def candidates():
        for _ in range(n):
            # find the shortest path from s to v with visited[v] == False
            v = -1
            for i in pendings:
                assert i in range(0, n)
                assert not visited[i]
                if v == -1 or costs[v] > costs[i]:
                    v = i
            if v != -1:
                # mark v visited
                pendings.remove(v)
                visited[v] = True
                yield v
            else:
                # halt the computation
                break
    # relax all unvisited neighbouring vertices around the vertex u
    def relax(u):
        # for each edge u -> v
        for (v, w) in edges[u]:
            if not visited[v]:
                # update v if there is a shorter path
                if costs[v] > w:
                    costs[v] = w
                    parents[v] = u
                    # mark v pending
                    pendings.add(v)
    # execution
    weight = 0
    for i in candidates():
        weight += costs[i]
        relax(i)
    return MST(n, w, s, parents)
