import math

def bellman_ford(n, edges, s):
    """Compute a shortest path tree with single source vertex

    Args:
        n (int): number of vertices
        edges ([(int, int, W)]): list of edges (u, v, w)
        s (int): index of source vertex

    Returns:
        [W]: dist[v] = distance from source to v

    If the algorithm detects at least one negative cycle, it will return None

    """
    dist = [math.inf] * n
    dist[s] = 0
    # |V|-1 iterations
    for _ in range(n-1):
        # update optimal distances
        for (u, v, w) in edges:
            if dist[v] > dist[u] + w:
                dist[v] = dist[u] + w
    # do one more iteration to detect negative cycle
    for (u, v, w) in edges:
        if dist[v] > dist[u] + w:
            return None
    # return list of distances
    return dist
