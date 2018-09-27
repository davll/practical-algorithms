from unittest import TestCase
from algo.graph.adjlist import Graph
from algo.graph.bfs import bfs
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

class TestBFS(TestCase):
    def test_default(self):
        g = _graph1()
        order = list(bfs(g))
        self.assertListEqual(order, [0, 1, 2, 4, 3, 5, 6, 7, 8])
        #print(str(order), file=stderr)
    def test_reversed_source(self):
        g = _graph1()
        order = list(bfs(g, source = reversed(range(len(g)))))
        self.assertListEqual(order, [8, 6, 7, 5, 4, 3, 2, 0, 1])
        #print(str(order), file=stderr)
