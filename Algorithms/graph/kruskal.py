from union_find import UnionFind

def mst_kruskal(n, edges):
    """
    edges: [(u,v,w)]
    returns: ([(u,v)], w)
    """
    mst, cost = [], 0
    edges.sort(key = lambda x: x[2])
    group = UnionFind(n)
    for (u, v, w) in edges:
        if group.find(u) != group.find(v):
            mst.append((u, v))
            cost += w
            group.union(u, v)
    return (mst, w)
