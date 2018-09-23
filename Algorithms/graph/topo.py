# Topological Sort

# Lemma: After DFS, if it exists a path from vertex A to vertex B,
#        then finish[A] > finish[B]

# Legacy DFS algorithm
def topo_dfs(n, edges):
    from dfs import dfs_postorder
    visited = [False] * n
    stack = []
    def _dfs(u):
        assert not visited[u]
        visited[u] = True
        for v in edges[u]:
            if not visited[v]:
                _dfs(v)
        # finish time
        stack.append(u)
    for s in range(n):
        if visited[s]:
            continue
        stack.extend(dfs_postorder(n, edges, s, visited))
        #_dfs(s)
    # order by finish time (from bigger to smaller)
    stack.reverse()
    return stack

# Kahn's algorithm
def topo_kahn(n, edges):
    """
    n: int => number of vertices
    edges: [[v]] => adjacency list
    return: []
    """
    from collections import deque
    indegree = [0] * n
    for v in (v for vs in edges for v in vs):
        indegree[v] += 1
    used = [[False] * len(edges[i]) for i in range(0,n)]
    result = []
    pendings = deque([i for i in range(0,n) if indegree[i] == 0])
    while len(pendings) > 0:
        u = pendings.popleft()
        result.append(u)
        # for each edge (u -> v)
        for (i,v) in enumerate(edges[u]):
            if used[u][i]:
                continue
            assert indegree[v] > 0
            # remove the edge (u -> v) from the graph
            used[u][i] = True
            indegree[v] -= 1
            # enqueue the vertex if its in-degree is zero
            if indegree[v] == 0:
                pendings.append(v)
    if any([not f for us in used for f in us]):
        # the graph has at least a cycle
        return None
    else:
        # a topologically sorted vertices
        return result

if __name__ == "__main__":
    n = 15
    edges = [
        [2],
        [2],
        [6,7],
        [4],
        [5],
        [6,14],
        [8,9,11,12],
        [8],
        [],
        [10],
        [],
        [],
        [13],
        [],
        [],
    ]
    result1 = topo_dfs(n, edges)
    result2 = topo_kahn(n, edges)
    print(str(result1))
    print(str(result2))
