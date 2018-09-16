# https://www.hackerrank.com/challenges/bfsshortreach/problem

from collections import deque
import math

def bfs(n, edges, s, units):
    d = [-1] * n
    d[s] = 0
    q = deque([s])
    while len(q) > 0:
        u = q.popleft()
        for v in edges[u]:
            if d[v] == -1 or d[v] > d[u] + units:
                d[v] = d[u] + units
                q.append(v)
    return d

if __name__ == "__main__":
    Q = int(input())
    for _ in range(Q):
        n, m = map(int, input().split())
        edges = [[] for _ in range(n)]
        for _ in range(m):
            u, v = map(int, input().split())
            u, v = u-1, v-1
            edges[u].append(v)
            edges[v].append(u)
        s = int(input())
        result = bfs(n, edges, s-1, 6)
        result = list(filter(lambda x: x != 0, result))
        print(' '.join(map(str, result)))
