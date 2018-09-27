from unittest import TestCase
from algo.data.graph import Graph
from ..dijkstra import dijkstra, dijkstra2
from math import isinf

class TestDijkstra(TestCase):
    def test_case1(self):
        g = _graph1()
        spt = dijkstra(g, 0)
        self.assertEqual(spt.distance(0), 0)
        self.assertListEqual(spt.path(0), [0])
    def test_case2(self):
        g = _graph2()
        spt = dijkstra(g, 0)
        self.assertEqual(spt.distance(0), 0)
        self.assertListEqual(spt.path(0), [0])
        self.assertEqual(spt.distance(1), 1.0)
        self.assertListEqual(spt.path(1), [0,1])
    def test_case3(self):
        g = _graph3()
        spt = dijkstra(g, 2)
        self.assertEqual(spt.distance(0), 3)
        self.assertListEqual(spt.path(0), [2, 0])
        self.assertEqual(spt.distance(1), 27)
        self.assertListEqual(spt.path(1), [2,0,1])
        self.assertEqual(spt.distance(2), 0)
        self.assertListEqual(spt.path(2), [2])
        self.assertEqual(spt.distance(3), 23)
        self.assertListEqual(spt.path(3), [2,0,3])
    def test_case4(self):
        g = _graph4()
        spt = dijkstra(g, 0)
        self.assertEqual(spt.distance(0), 0)
        self.assertListEqual(spt.path(0), [0])
        # TODO
    def test_case5(self):
        g = _graph5()
        spt = dijkstra(g, 0)
        self.assertEqual(spt.distance(0), 0)
        self.assertListEqual(spt.path(0), [0])
        # TODO

def _graph1():
    g = Graph(1)
    g.add_edge(0, 0, 1.0)
    g.add_edge(0, 0, 2.0)
    return g

def _graph2():
    g = Graph(2)
    g.add_edge(0, 1, 1.0)
    g.add_edge(1, 0, 2.0)
    return g

def _graph3():
    g = Graph(4)
    g.add_edge(0, 1, 24)
    g.add_edge(0, 3, 20)
    g.add_edge(2, 0, 3)
    g.add_edge(3, 2, 12)
    return g

def _graph4():
    g = Graph(5)
    g.add_edge(0, 1, 10)
    g.add_edge(0, 2, 6)
    g.add_edge(1, 3, 8)
    return g

def _graph5():
    g = Graph(5)
    g.add_edge(0, 1, 2)
    g.add_edge(1, 4, 5)
    g.add_edge(1, 2, 4)
    g.add_edge(0, 3, 1)
    g.add_edge(3, 2, 3)
    g.add_edge(2, 4, 1)
    return g
