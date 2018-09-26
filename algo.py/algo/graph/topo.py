# Topological Sort

# Lemma: After DFS, if it exists a path from vertex A to vertex B,
#        then finish[A] > finish[B]

from adjlist import Graph

# Legacy DFS algorithm
def topo_dfs(graph):
    from dfs import dfs, Order
    stack = list(dfs(graph, order=Order.POST, acyclic=True))
    # order by finish time (from new to old)
    stack.reverse()
    return stack

# Kahn's algorithm
def topo_kahn(graph):
    from collections import deque
    n = len(graph)
    indegree = graph.indegrees()
    used = [[False] * graph.outdegree(i) for i in range(0,n)]
    result = []
    q = deque([i for i in range(0,n) if indegree[i] == 0])
    while len(q) > 0:
        u = q.popleft()
        result.append(u)
        # for each edge (u -> v)
        for (i,(v,_)) in enumerate(graph.edges_from(u)):
            if used[u][i]:
                continue
            assert indegree[v] > 0
            # remove the edge (u -> v) from the graph
            used[u][i] = True
            indegree[v] -= 1
            # enqueue the vertex if its in-degree is zero
            if indegree[v] == 0:
                q.append(v)
    if any([not f for us in used for f in us]):
        # the graph has at least a cycle
        return None
    else:
        # a topologically sorted vertices
        return result

if __name__ == "__main__":
    g = Graph(15)
    g.add_edge(0, 2)
    g.add_edge(1, 2)
    g.add_edge(2, 6)
    g.add_edge(2, 7)
    g.add_edge(3, 4)
    g.add_edge(4, 5)
    g.add_edge(5, 6)
    g.add_edge(5, 14)
    g.add_edge(6, 8)
    g.add_edge(6, 9)
    g.add_edge(6, 11)
    g.add_edge(6, 12)
    g.add_edge(7, 8)
    g.add_edge(9, 10)
    g.add_edge(12, 13)
    #g.add_edge(12, 0)
    def check_result(ans):
        n = len(g)
        for u in range(n):
            u_idx = ans.index(u)
            for (v,_) in g.edges_from(u):
                assert u_idx < ans.index(v)
    result1 = topo_dfs(g)
    result2 = topo_kahn(g)
    print(str(result1))
    print(str(result2))
    check_result(result1)
    check_result(result2)
