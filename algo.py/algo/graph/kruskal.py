from union_find import UnionFind
from adjlist import UGraph

class MST:
    """Minimum Spanning Tree

    Attributes:
        size (int): number of vertices
        weight (T): weight of the MST
        edges [Edge(int, int, T)]: edges of the MST

    """
    #
    def __init__(self, n, w, edges):
        self.size = n
        self.weight = w
        self.edges = edges

def mst_kruskal(graph):
    """Find a minimum spanning tree from a graph

    Args:
        graph (UGraph): undirected graph
    
    Returns:
        MST: a minimum spanning tree

    """
    # prepare data
    n, edges = len(graph), list(graph.edges)
    edges.sort(key=lambda x: x.w)
    #
    mst, cost = [], 0
    group = UnionFind(n)
    for (u, v, w) in edges:
        if group.find(u) != group.find(v):
            mst.append((u, v, w))
            cost += w
            group.union(u, v)
    return MST(n, cost, mst)

if __name__ == "__main__":
    pass
