import math

#
# d[i,j,k] = distance of shortest path from i to j through 0~k
#
# d[i,j,k] = min { d[i,k,k-1]+d[k,j,k-1], d[i,j,k-1] }
#

class SPM:
    """Shortest Path Matrix
    """
    def __init__(self, n, dist, next):
        self.n = n
        self.dist = dist
        self.next = next
    #
    def path(self, s, t):
        ls = []
        i = s
        while i != t:
            ls.append(i)
            i = self.next[i][t]
        ls.append(t)
        return ls

def floyd_warshall(n, edges):
    """
    n: int
    edges: [(u, v, w)]
    return: [[w]]
    """
    # dist[i][j] = distance from i to j
    dist = [[math.inf] * n for _ in range(n)]
    # next[i][j] = the 2nd vertex after i in the path from i to j
    next = [[j for j in range(n)] for _ in range(n)]
    # initialize dist[i][j]
    for (u,v,w) in edges:
        dist[u][v] = min(dist[u,v], w)
    for v in range(n):
        dist[v][v] = 0
    # perform DP
    for k in range(0, n):
        for i in range(0, n):
            for j in range(0, n):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    next[i][j] = next[i][k]
    # detect negative cycle
    for i in range(0, n):
        if dist[i][i] < 0:
            return None
    # return matrix of distances
    return SPM(n, dist, next)
