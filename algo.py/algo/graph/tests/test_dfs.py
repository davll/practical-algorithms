from unittest import TestCase
from algo.data.graph import Graph
from algo.graph.dfs import dfs, detect_cycle
from sys import stderr

def _graph1():
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
    return g

def _graph2():
    g = Graph(6)
    g.add_edge(2, 1)
    g.add_edge(1, 0)
    g.add_edge(2, 3)
    g.add_edge(2, 4)
    return g

class TestDFS(TestCase):
    def test_default(self):
        g = _graph1()
        order = list(dfs(g))
        self.assertListEqual(order, [0, 1, 2, 3, 5, 4, 6, 7, 8])
        #print(str(order), file=stderr)
    def test_postorder(self):
        g = _graph1()
        order = list(dfs(g, postorder=True))
        self.assertListEqual(order, [3, 8, 7, 6, 4, 5, 2, 1, 0])
        #print(str(order), file=stderr)
    def test_reversed_source(self):
        g = _graph1()
        order = list(dfs(g, source = reversed(range(len(g)))))
        self.assertListEqual(order, [8, 6, 7, 5, 4, 3, 2, 0, 1])
        #print(str(order), file=stderr)
    def test_detect_cylce1(self):
        g = _graph1()
        self.assertTrue(detect_cycle(g))
    def test_detect_cylce2(self):
        g = _graph2()
        self.assertFalse(detect_cycle(g))
