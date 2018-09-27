from unittest import TestCase
from algo.data.graph import Graph
from algo.graph.toposort import *
from sys import stderr

def _graph1():
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
    return g

class TestTopoSort(TestCase):
    def test_dfs(self):
        g = _graph1()
        order = toposort_dfs(g)
        self._check_result(order, g)
    def test_kahn(self):
        g = _graph1()
        order = toposort_kahn(g)
        self._check_result(order, g)
    def _check_result(self, ans, g):
        n = len(g)
        for u in range(n):
            u_idx = ans.index(u)
            for (v,_) in g.edges_from(u):
                self.assertLess(u_idx, ans.index(v))
