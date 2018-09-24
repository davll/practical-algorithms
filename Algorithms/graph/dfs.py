# Depth-First Search

from adjlist import Graph
from enum import Enum

class Order(Enum):
    PRE = 1
    POST = 2

class UnexpectedCycleError(Exception):
    pass

def dfs(graph, order = Order.PRE, acyclic = False, source = None):
    order = Order(order)
    n = len(graph)
    visited = [False] * n
    if acyclic:
        intree = [False] * n
    def _dfs_visit(u):
        assert not visited[u]
        if acyclic:
            assert not intree[u]
        if order == Order.PRE:
            yield u
        visited[u] = True
        if acyclic:
            intree[u] = True
        for (v,_) in graph.edges_from(u):
            if not visited[v]:
                yield from _dfs_visit(v)
            elif acyclic and intree[v]:
                raise UnexpectedCycleError()
        if acyclic:
            intree[u] = False
        if order == Order.POST:
            yield u
    if source:
        source = iter(source)
    else:
        source = range(0, n)
    for s in source:
        if visited[s]:
            continue
        yield from _dfs_visit(s)

def dfs_i(n, edges, start, visited):
    stack = [start]
    # Iterate
    while len(stack) > 0:
        u = stack.pop()
        if visited[u]:
            continue
        yield u
        visited[u] = True
        for v in reversed(edges[u]):
            if not visited[v]:
                stack.append(v)

# http://alrightchiu.github.io/SecondRound/graph-depth-first-searchdfsshen-du-you-xian-sou-xun.html
# https://www.geeksforgeeks.org/detect-cycle-in-a-graph/

if __name__ == "__main__":
    g = Graph(9)
    g.add_edge(0, 1)
    g.add_edge(1, 2)
    g.add_edge(1, 4)
    g.add_edge(2, 0)
    g.add_edge(2, 3)
    g.add_edge(2, 5)
    g.add_edge(3, 2)
    g.add_edge(4, 5)
    g.add_edge(4, 6)
    g.add_edge(5, 4)
    g.add_edge(5, 6)
    g.add_edge(5, 7)
    g.add_edge(6, 7)
    g.add_edge(7, 8)
    g.add_edge(8, 6)
    print(str(list(dfs(g, source = reversed(range(9))))))
