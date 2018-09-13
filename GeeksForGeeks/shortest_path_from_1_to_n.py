# https://practice.geeksforgeeks.org/problems/shortest-path-from-1-to-n/0

import math
import heapq

def next_vert(n,u):
    v1 = u + 1
    v2 = 3 * (u+1) - 1
    if v1 < n:
        yield v1
    if v2 < n:
        yield v2

def shortest_path(n):
    dist = [0] * n
    visited = [False] * n
    q = [(0,0)]
    while len(q) > 0:
        (d,u) = heapq.heappop(q)
        if visited[u]:
            continue
        dist[u] = d
        visited[u] = True
        for v in next_vert(n,u):
            if not visited[v]:
                heapq.heappush(q, (dist[u]+1, v))
    return dist[n-1]

if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n = int(input().strip())
        result = shortest_path(n)
        print(str(result))
