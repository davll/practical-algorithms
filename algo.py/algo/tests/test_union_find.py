import unittest
from algo.union_find import UnionFind

class TestUnionFind(unittest.TestCase):
    def test_init(self):
        uf = UnionFind(128)
    def test_count_1(self):
        uf = UnionFind(32)
        self.assertEqual(uf.count, 32)
    def test_find_1(self):
        uf = UnionFind(16)
        for i in range(0, 16):
            self.assertEqual(uf.find(i), i)
    def test_union_1(self):
        uf = UnionFind(16)
        uf.union(4, 10)
        self.assertEqual(uf.count, 15)
        self.assertEqual(uf.find(4), uf.find(10))
    def test_union_2(self):
        uf = UnionFind(16)
        # 0, 1, ..., 9
        for i in range(0,9):
            uf.union(i, i+1)
        # 10, 11, 12, 13
        for i in range(10,13):
            uf.union(i+1, i)
        # 14, 15
        uf.union(14, 15)
        # check number of sets
        self.assertEqual(uf.count, 3)
        # check if 0...9 are connected
        for i in range(1,10):
            self.assertEqual(uf.find(0), uf.find(i))
        # check if 10...13 are connected
        for i in range(11,14):
            self.assertEqual(uf.find(10), uf.find(i))
        # check if 14, 15 are connected
        self.assertEqual(uf.find(14), uf.find(15))
        # combine two sets
        uf.union(5, 12)
        # check if 0...13 are connected
        for i in range(1,14):
            self.assertEqual(uf.find(0), uf.find(i))
