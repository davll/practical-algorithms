# Breadth-First Search

from collections import deque

def bfs(n, edges, start):
    visited = [False] * n
    q = deque()
    # Initialise
    q.append(start)
    visited[start] = True
    # Iterate
    while len(q) > 0:
        u = q.popleft()
        yield u
        for v in edges[u]:
            if not visited[v]:
                q.append(v)
                visited[v] = True

if __name__ == "__main__":
    pass
