def edges_to_adjacencies(n, edges):
    adj = [[] for _ in range(n)]
    for pair in edges:
        adj[pair[0]].append(pair[1])
    return adj

def detect_cycle(n, adj):
    pendings = set(range(0, n))
    visited, stacked = [False] * n, [False] * n
    # define Depth-First Search
    def dfs(v):
        if not visited[v]:
            pendings.discard(v)
            visited[v] = True
            stacked[v] = True
            for t in adj[v]:
                if not visited[t] and dfs(t):
                    return True
                elif stacked[t]:
                    return True
        stacked[v] = False
        return False
    # scan the graph
    while len(pendings) > 0:
        v = pendings.pop()
        if dfs(v):
            return True
    return False

class Solution:
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        n = numCourses
        adj = edges_to_adjacencies(n, prerequisites)
        return not detect_cycle(n, adj)
