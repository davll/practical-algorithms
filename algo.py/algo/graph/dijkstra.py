import math
import heapq
import unittest

class SPT:
    """Shortest Path Tree of the single source vertex

    Attributes:
        n (int): number of vertices
        s (int): index of source vertex
        costs ([W]): costs[v] = distance from the source to v
        parents ([int]): parents[v] = the previous vertex followed by v in the shortest path from s to v

    """
    def __init__(self, n, s, costs, parents):
        self.n = n
        self.s = s
        self.costs = costs
        self.parents = parents
    #
    def distance(self, v):
        """Distance from source to v

        Args:
            v (int): index of vertex
        
        Returns:
            W: the total weight of the shortest path from s to v

        """
        return self.costs[v]
    #
    def path(self, v):
        """Generate the shortest path from source to v

        Args:
            v (int): index of vertex

        Returns:
            [int]: list of vertices of the shortest path from s to v

        """
        path = [v]
        i = v
        while self.parents[i] != -1:
            p = self.parents[i]
            path.append(p)
            i = p
        path.reverse()
        return path

def dijkstra(n, edges, s):
    """Compute a shortest path tree of the single source vertex

    Args:
        n (int): number of vertices
        edges ([[(int, W)]]): adjacency list, (v, w) = edges[u][i] denotes an edge (u->v) with weight w
        s (int): index of source vertex

    Returns:
        SPT: shortest path tree

    """
    # pending: the set of unvisited vertices with finitie costs[v] (not infinite)
    pendings = set()
    # visited[v] = True if visited
    visited = [False] * n
    # costs[v] = distance from s to v
    # parents[v] = the previous vertex followed by v in the shortest path from s to v
    costs, parents = [math.inf] * n, [-1] * n
    # process source vertex in the beginning
    costs[s] = 0
    pendings.add(s)
    # extract candidates for relaxation
    def candidates():
        for _ in range(n):
            # find the shortest path from s to v with visited[v] == False
            v = -1
            for i in pendings:
                assert i in range(0, n)
                assert not visited[i]
                if v == -1 or costs[v] > costs[i]:
                    v = i
            if v != -1:
                # mark v visited
                pendings.remove(v)
                visited[v] = True
                yield v
            else:
                # halt the computation
                break
    # relax all unvisited neighbouring vertices around the vertex u
    def relax(u):
        # for each edge u -> v
        for (v, w) in edges[u]:
            if not visited[v]:
                # update v if there is a shorter path
                if costs[v] > costs[u] + w:
                    costs[v] = costs[u] + w
                    parents[v] = u
                    # mark v pending
                    pendings.add(v)
    # execution
    for i in candidates():
        relax(i)
    return SPT(n, s, costs, parents)

def dijkstra2(n, edges, s):
    costs, parents = [math.inf] * n, [-1] * n
    visited = [False] * n
    # initialise
    costs[s] = 0
    queue = [(0, -1, s)]
    #
    while len(queue) > 0:
        # extract the nearest vertex u which is not visited
        (c, p, u) = heapq.heappop(queue)
        if visited[u]:
            continue
        # update values
        visited[u] = True
        costs[u] = c
        parents[u] = p
        # push neighbouring vertices
        for (v, w) in edges[u]:
            if not visited[v]:
                heapq.heappush(queue, (costs[u] + w, u, v))
    # finish when the queue is empty
    return SPT(n, s, costs, parents)

class TestDijkstra(unittest.TestCase):
    def test_case1(self):
        n = 1
        edges = [[(0, 1.0)]]
        result = dijkstra(n, edges, 0)
        self.assertEqual(result.distance(0), 0.0)
        self.assertEqual(result.path(0), [0])
    #
    def test_case2(self):
        n = 2
        edges = [[(0, 1.0), (1, 5.0)], [(0, 2.0)]]
        result = dijkstra(n, edges, 1)
        self.assertEqual(result.distance(0), 2.0)
        self.assertEqual(result.distance(1), 0.0)
        self.assertEqual(result.path(0), [1, 0])
        self.assertEqual(result.path(1), [1])
    #
    def test_case3(self):
        n = 5
        edges = [
            [(1,4), (2,2)],
            [(3,2), (2,3), (4,3)],
            [(1,1), (3,4), (4,5)],
            [],
            [(3,1)]
        ]
        result = dijkstra(n, edges, 0)
        #print(str(costs))
        #print(str(parents))
    #
    def test_case4(self):
        n = 6
        edges = [
            [(1,4), (2,2)],
            [(3,2), (2,3), (4,3)],
            [(1,1), (3,4), (4,5)],
            [(5,10)],
            [(3,1)],
            [(3,10)]
        ]
        result = dijkstra(n, edges, 0)
        #print(str(costs))
        #print(str(parents))
    #
    def test_case5(self):
        n = 2
        edges = [
            [(1,12)],
            [(0,12)]
        ]
        result = dijkstra(n, edges, 0)
        #print(str(costs))
        #print(str(parents))
    #
    def test_case6(self):
        n = 3
        edges = [
            [(1,2)],
            [(2,5)],
            [(0,1), (1,1)]
        ]
        result = dijkstra(n, edges, 0)
        #print(str(costs))
        #print(str(parents))
    #
    def test_case7(self):
        n = 5
        edges = [
            [(1,2)],
            [(2,3)],
            [(3,4)],
            [(2,5)],
            []
        ]
        result = dijkstra(n, edges, 0)
        #print(str(costs))
        #print(str(parents))
    #
    def test_case8(self):
        n = 5
        edges = [
            [(2,1), (3,1), (1,10)],
            [(3,10), (2,1), (3,1)],
            [(4,10)],
            [(2,10), (4,1)],
            []
        ]
        result = dijkstra(n, edges, 0)
        #print(str(costs))
        #print(str(parents))

if __name__ == "__main__":
    unittest.main()
