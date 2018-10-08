import math
import heapq

class SPT:
    """Shortest Path Tree of the single source vertex

    Attributes:
        source (int): source vertex
        costs ([W]): costs[v] = distance from the source to v
        parents ([int]): parents[v] = the previous vertex followed by v in the shortest path from s to v

    """
    def __init__(self, source, costs, parents):
        self.source = source
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
        if path[0] == self.source and path[-1] == v:
            return path
        else:
            return []

def dijkstra(graph, source):
    """Compute a shortest path tree from the graph

    Args:
        graph (Graph): directed graph
        source (int): source vertex

    Returns:
        SPT: shortest path tree

    """
    n = len(graph)
    # visited[v] = True if visited
    visited = [False] * n
    # costs[v] = distance from s to v
    # parents[v] = the previous vertex followed by v in the shortest path from s to v
    costs, parents = [math.inf] * n, [-1] * n
    # process source vertex in the beginning
    costs[source] = 0
    # pending: the set of unvisited vertices with finitie costs[v] (not infinite)
    pendings = set([source])
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
        for (v, w) in graph.edges_from(u):
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
    return SPT(source, costs, parents)

def dijkstra2(graph, source):
    n = len(graph)
    costs, parents = [math.inf] * n, [-1] * n
    visited = [False] * n
    # initialise
    costs[source] = 0
    queue = [(0, -1, source)]
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
        for (v, w) in graph.edges_from[u]:
            if not visited[v]:
                heapq.heappush(queue, (costs[u] + w, u, v))
    # finish when the queue is empty
    return SPT(source, costs, parents)
