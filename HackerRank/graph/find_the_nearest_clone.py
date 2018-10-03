from sys import stdin, stdout, stderr
from collections import deque

# BFS
# Lowest Common Ancestor

def _clear_list(ls, v):
    for i in range(len(ls)):
        ls[i] = v

def bfs(n, adj, start):
    distance = [-1] * n
    visited = [False] * n
    #parent = [-1] * n
    queue = deque([start])
    visited[start] = True
    distance[start] = 0
    # do BFS
    while len(queue) > 0:
        u = queue.popleft()
        assert visited[u]
        for v in adj[u]:
            if not visited[v]:
                distance[v] = distance[u] + 1
                #parent[v] = u
                visited[v] = True
                queue.append(v)
    #
    return distance

def findShortest(g_nodes, g_from, g_to, ids, val):
    # prepare adjacency list
    adj = [[] for _ in range(g_nodes)]
    for u, v in zip(g_from, g_to):
        adj[u].append(v)
        adj[v].append(u)
    # select one starting node with color id `val`
    group = [i for i, c in enumerate(ids) if c == val]
    if len(group) < 2:
        return -1
    # do BFS
    ans = -1
    for s in group:
        distance = bfs(g_nodes, adj, s)
        for i in group:
            if ids[i] != val or i == s:
                continue
            if ans == -1:
                ans = distance[i]
            else:
                ans = min(ans, distance[i])
    return ans

if __name__ == "__main__":
    n, m = map(int, stdin.readline().rstrip().split())
    g_from, g_to = [], []
    for _ in range(m):
        u, v = map(int, stdin.readline().rstrip().split())
        g_from.append(u-1)
        g_to.append(v-1)
    ids = list(map(int, stdin.readline().rstrip().split()))
    val = int(stdin.readline().rstrip())
    ans = findShortest(n, g_from, g_to, ids, val)
    stdout.write(str(ans) + '\n')
