# Kosaraju's Algorithm for finding strongly connected components

from algo.data.graph import Graph
from sys import stderr

def kosaraju(graph):
    from algo.graph.dfs import dfs, dfs_visit_preorder
    n = len(graph)
    # perform DFS
    order = list(dfs(graph, postorder=True))
    # perform DFS on transposed graph
    scc = []
    visited = [False] * n
    trg = graph.transposed()
    for start in reversed(order):
        if visited[start]:
            continue
        scc.append(list(dfs_visit_preorder(start, trg, visited)))
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
