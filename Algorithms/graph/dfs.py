# Depth-First Search

def dfs(n, edges, start):
    visited = [False] * n
    stack = []
    # Initialise
    stack.push((start))
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

if __name__ == "__main__":
    pass
