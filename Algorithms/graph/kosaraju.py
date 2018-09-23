# Kosaraju's Algorithm for finding strongly connected components

def transpose_edges(n, edges):
    tr = [[] for _ in range(n)]
    for u in range(n):
        for v in edges[u]:
            tr[v].append(u)
    return tr

def kosaraju(n, edges):
    # perform DFS
    def dfs1(u, order, visited, edges):
        assert not visited[u]
        visited[u] = True
        for v in edges[u]:
            if not visited[v]:
                dfs1(v, order, visited, edges)
        order.append(u)
    order = []
    visited = [False] * n
    for start in range(n):
        if visited[start]:
            continue
        dfs1(start, order, visited, edges)
    del visited
    # perform DFS on transposed graph
    def dfs2(u, comp, visited, edges):
        assert not visited[u]
        comp.append(u)
        visited[u] = True
        for v in edges[u]:
            if not visited[v]:
                dfs2(v, comp, visited, edges)
    scc = []
    visited = [False] * n
    tredges = transpose_edges(n, edges)
    for start in reversed(order):
        if visited[start]:
            continue
        comp = []
        dfs2(start, comp, visited, tredges)
        scc.append(comp)
    return scc

if __name__ == "__main__":
    n = 5
    edges = [
        [2, 3],
        [0],
        [1],
        [4],
        []
    ]
    scc = kosaraju(n, edges)
    print(str(scc))
