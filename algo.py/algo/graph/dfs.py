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

def dfs(graph, sources = None, mode = 'preorder'):
    n = len(graph)
    visited = [False] * n
    sources = iter(sources) if sources else range(n)
    for s in sources:
        if visited[s]:
            continue
        if mode == 'postorder':
            yield from dfs_visit_postorder(s, graph, visited)
        elif mode == 'preorder':
            yield from dfs_visit_preorder(s, graph, visited)
        else:
            raise ValueError("Invalid mode = {}".format(mode))

def detect_cycle(graph):
    n = len(graph)
    visited = [False] * n
    instack = [False] * n
    def _dfs_visit(u):
        assert not visited[u]
        assert not instack[u]
        visited[u] = True
        instack[u] = True
        for (v,_) in graph.edges_from(u):
            if not visited[v]:
                if _dfs_visit(v):
                    return True
            elif instack[v]:
                return True
        instack[u] = False
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
