# Breadth-First Search

from collections import deque

def bfs_visit(s, graph, visited):
    assert not visited[s]
    q = deque([s])
    visited[s] = True
    # Iterate
    while len(q) > 0:
        u = q.popleft()
        yield u
        for (v,_) in graph.edges_from(u):
            if not visited[v]:
                q.append(v)
                visited[v] = True

def bfs(graph, source = None):
    n = len(graph)
    visited = [False] * n
    if source:
        source = iter(source)
    else:
        source = range(0, n)
    for s in source:
        if visited[s]:
            continue
        yield from bfs_visit(s, graph, visited)
