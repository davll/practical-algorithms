# [WIP]

def edges_to_adjacencies(n, edges):
    adj = [[] for _ in range(n)]
    for pair in edges:
        adj[pair[0]].append(pair[1])
    return adj

def detect_cycle(n, adj):
    

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
