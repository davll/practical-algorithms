from union_find import UnionFind

class MST:
    """Minimum Spanning Tree

    Attributes:
        n (int): number of vertices
        w (T): weight of the MST
        edges [(int, int, T)]: edges of the MST

    """
    #
    def __init__(self, n, w, edges):
        self.n = n
        self.w = w
        self.edges = edges

def mst_kruskal(n, edges):
    """Find a minimum spanning tree from an undirected graph

    Args:
        n (int): number of vertices
        edges ([(int, int, T)]): list of edges, each edge is composed of (u, v, w)
    
    Returns:
        MST: a minimum spanning tree

    """
    mst, cost = [], 0
    edges.sort(key = lambda x: x[2])
    group = UnionFind(n)
    for (u, v, w) in edges:
        if group.find(u) != group.find(v):
            mst.append((u, v, w))
            cost += w
            group.union(u, v)
    return MST(n, cost, mst)

if __name__ == "__main__":
    pass
