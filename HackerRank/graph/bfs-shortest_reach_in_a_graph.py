from collections import deque

def bfs(n, adj, start, w):
    visited = [False] * n
    distance = [-1] * n
    queue = deque([start])
    visited[start] = True
    distance[start] = 0
    while len(queue) > 0:
        u = queue.popleft()
        assert visited[u]
        for v in adj[u]:
            if not visited[v]:
                visited[v] = True
                distance[v] = distance[u] + w
                queue.append(v)
    return distance

if __name__ == "__main__":
    for _ in range(int(input())):
        n, m = map(int, input().split())
        adj = [[] for _ in range(n)]
        for _ in range(m):
            u, v = map(int, input().split())
            adj[u-1].append(v-1)
            adj[v-1].append(u-1)
        start = int(input()) - 1
        distance = bfs(n, adj, start, 6)
        print(' '.join(map(lambda x: str(x[1]), filter(lambda x: x[0] != start, enumerate(distance)))))
