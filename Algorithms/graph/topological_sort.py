from collections import deque

# Kahn's algorithm
def toposort(n, edges):
    """
    n: int => number of vertices
    edges: [[v]] => adjacency list
    return: []
    """
    indegree = [0] * n
    for vs in edges:
        for v in vs:
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
