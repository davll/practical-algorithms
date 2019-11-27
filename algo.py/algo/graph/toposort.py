# Topological Sort

# Lemma: After DFS, if it exists a path from vertex A to vertex B,
#        then finish[A] > finish[B]

from .dfs import dfs

# Legacy DFS algorithm
def toposort_dfs(graph):
    from algo.graph.dfs import dfs
    stack = list(dfs(graph, mode='postorder'))
    # order by finish time (from new to old)
    stack.reverse()
    return stack

# Kahn's algorithm
def toposort_kahn(graph):
    from collections import deque
    n = len(graph)
    indegree = graph.indegrees()
    used = [[False] * graph.outdegree(i) for i in range(0,n)]
    result = []
    q = deque([i for i in range(0,n) if indegree[i] == 0])
    while len(q) > 0:
        u = q.popleft()
        result.append(u)
        # for each edge (u -> v)
        for (i,(v,_)) in enumerate(graph.edges_from(u)):
            if used[u][i]:
                continue
            assert indegree[v] > 0
            # remove the edge (u -> v) from the graph
            used[u][i] = True
            indegree[v] -= 1
            # enqueue the vertex if its in-degree is zero
            if indegree[v] == 0:
                q.append(v)
    if any([not f for us in used for f in us]):
        # the graph has at least a cycle
        return None
    else:
        # a topologically sorted vertices
        return result
