import math

def floyd_warshall(n, edges):
    """
    n: int
    edges: [(u, v, w)]
    return: [[w]]
    """
    dist = [[math.inf] * n for _ in range(n)]
    for (u,v,w) in edges:
        dist[u][v] = w
    for v in range(n):
        dist[v][v] = 0
    for k in range(0, n):
        for i in range(0, n):
            for j in range(0, n):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    return dist
