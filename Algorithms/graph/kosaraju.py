# Kosaraju's Algorithm for finding strongly connected components

from adjlist import Graph
from sys import stderr

def kosaraju(graph):
    from dfs import dfs, Order
    n = len(graph)
    # perform DFS
    order = list(dfs(graph, order=Order.POST))
    # perform DFS on transposed graph
    def dfs2(u, visited, g):
        assert not visited[u]
        yield u
        visited[u] = True
        for (v,_) in g.edges_from(u):
            if not visited[v]:
                yield from dfs2(v, visited, g)
    scc = []
    visited = [False] * n
    trg = graph.transposed()
    for start in reversed(order):
        if visited[start]:
            continue
        scc.append(list(dfs2(start, visited, trg)))
    return scc

# http://alrightchiu.github.io/SecondRound/graph-li-yong-dfsxun-zhao-strongly-connected-componentscc.html

if __name__ == "__main__":
    g = Graph(9)
    g.add_edge(0, 1)
    g.add_edge(1, 2)
    g.add_edge(1, 4)
    g.add_edge(2, 0)
    g.add_edge(2, 3)
    g.add_edge(2, 5)
    g.add_edge(3, 2)
    g.add_edge(4, 5)
    g.add_edge(4, 6)
    g.add_edge(5, 4)
    g.add_edge(5, 6)
    g.add_edge(5, 7)
    g.add_edge(6, 7)
    g.add_edge(7, 8)
    g.add_edge(8, 6)
    scc = kosaraju(g)
    print(str(scc))
