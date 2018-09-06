import heapq
import unittest

class DijkstraResult:
    def __init__(self, n, costs, parents):
        self._costs = costs
        self._parents = parents
    #
    def distance(self, v):
        return self._costs[v]
    #
    def path(self, v):
        path = [v]
        i = v
        while self._parents[i] != i:
            p = self._parents[i]
            path.append(p)
            i = p
        path.reverse()
        return path

def dijkstra(n, edges, s):
    """
    n: int => number of vertices
    edges: [[(int, W)]] => adjacency list
    s: int => source vertex
    """
    visited = [False] * n
    costs, parents = [None] * n, [i for i in range(n)]
    costs[s] = 0
    def candidates():
        for i in range(n):
            if not visited[i] and costs[i] != None:
                yield (i, costs[i])
    def extract():
        for _ in range(n):
            result = min(candidates(), default = None, key = lambda x: x[1])
            if result:
                (i, _) = result
                visited[i] = True
                yield i
            else:
                break
    def relax(v):
        for (t, w) in edges[v]:
            if not visited[t]:
                if costs[t] == None or costs[t] > costs[v] + w:
                    costs[t] = costs[v] + w
                    parents[t] = v
    for i in extract():
        relax(i)
    return DijkstraResult(n, costs, parents)

class _PQEdge:
    def __init__(self, u, v, w):
        self.u = u
        self.v = v
        self.w = w
    def __eq__(self, other):
        return self.w == other.w
    def __lt__(self, other):
        return self.w < other.w
    def __gt__(self, other):
        return self.w > other.w
    def __le__(self, other):
        return self.w <= other.w
    def __ge__(self, other):
        return self.w >= other.w

def dijkstra2(n, edges, s):
    visited = [False] * n
    costs, parents = [None] * n, [i for i in range(n)]
    costs[s] = 0
    visited[s] = True
    queue, u = [], s
    for _ in range(n):
        for (v, w) in edges[u]:
            if not visited[v]:
                heapq.heappush(queue, _PQEdge(u, v, costs[u] + w))
        def smallest_edge():
            while len(queue) > 0:
                x = heapq.heappop(queue)
                if not visited[x.v]:
                    return x
            return None
        e = smallest_edge()
        if not e:
            break
        u = e.v
        costs[u] = e.w
        parents[u] = e.u
        visited[u] = True
    return DijkstraResult(n, costs, parents)

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
