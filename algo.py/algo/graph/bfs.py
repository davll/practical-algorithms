# Breadth-First Search

from collections import deque

def bfs_visit(s, graph, visited):
    assert not visited[s]
    # Initialise
    q = deque([s])
    visited[s] = True
    # Iterate
    while len(q) > 0:
        u = q.popleft()
        yield u
        for (_,v,_) in graph.edges_from(u):
            if not visited[v]:
                q.append(v)
                visited[v] = True

def bfs(graph, source = None):
    """
    Breadth First Search

    Time Complexity: O(n)
    """
    n = len(graph)
    visited = [False] * n
    source = iter(source) if source else range(n)
    for s in source:
        if visited[s]:
            continue
        yield from bfs_visit(s, graph, visited)
