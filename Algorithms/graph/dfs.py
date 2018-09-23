# Depth-First Search

def dfs_preorder(n, edges, u, visited):
    assert not visited[u]
    yield u
    visited[u] = True
    for v in edges[u]:
        if not visited[v]:
            yield from dfs_preorder(n, edges, v, visited)

def dfs_postorder(n, edges, u, visited):
    assert not visited[u]
    visited[u] = True
    for v in edges[u]:
        if not visited[v]:
            yield from dfs_postorder(n, edges, v, visited)
    yield u

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

if __name__ == "__main__":
    pass
