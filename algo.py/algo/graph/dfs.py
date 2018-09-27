# Depth-First Search

def dfs_visit_preorder(u, graph, visited):
    assert not visited[u]
    # visit and mark vertex u
    yield u
    visited[u] = True
    # visit neighbours
    for (v,_) in graph.edges_from(u):
        if not visited[v]:
            yield from dfs_visit_preorder(v, graph, visited)

def dfs_visit_postorder(u, graph, visited):
    assert not visited[u]
    # mark vertex u
    visited[u] = True
    # visit neighbours
    for (v,_) in graph.edges_from(u):
        if not visited[v]:
            yield from dfs_visit_postorder(v, graph, visited)
    # visit vertex u
    yield u

def dfs(graph, postorder = False, source = None):
    n = len(graph)
    visited = [False] * n
    if source:
        source = iter(source)
    else:
        source = range(0, n)
    for s in source:
        if visited[s]:
            continue
        if postorder:
            yield from dfs_visit_postorder(s, graph, visited)
        else:
            yield from dfs_visit_preorder(s, graph, visited)

def detect_cycle(graph):
    n = len(graph)
    visited = [False] * n
    intree = [False] * n
    def _dfs_visit(u):
        assert not visited[u]
        assert not intree[u]
        visited[u] = True
        intree[u] = True
        for (v,_) in graph.edges_from(u):
            if not visited[v]:
                if _dfs_visit(v):
                    return True
            elif intree[v]:
                return True
        intree[u] = False
        return False
    for s in range(0, n):
        if visited[s]:
            continue
        if _dfs_visit(s):
            return True
    return False

def dfs_i(n, edges, start, visited):
    stack = [start]
    # Iterate
    while len(stack) > 0:
        u = stack.pop()
        if visited[u]:
            continue
        yield u
        visited[u] = True
        for v in reversed(edges[u]):
            if not visited[v]:
                stack.append(v)

# http://alrightchiu.github.io/SecondRound/graph-depth-first-searchdfsshen-du-you-xian-sou-xun.html
# https://www.geeksforgeeks.org/detect-cycle-in-a-graph/
