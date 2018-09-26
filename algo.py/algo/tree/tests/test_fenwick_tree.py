import unittest
from algo.tree.fenwick_tree import *

class TestFenwick1D(unittest.TestCase):
    def test_4_init(self):
        arr = [10, 5, 23, 6]
        ft = ft_init(arr)
        self.assertListEqual(ft, [10, 15, 23, 44])
    def test_4_query(self):
        arr = [10, 5, 23, 6]
        ft = ft_init(arr)
        q = [ft_query(ft, i) for i in range(4)]
        self.assertListEqual(q, [10, 15, 38, 44])
    def test_4_update(self):
        arr = [10, 5, 23, 6]
        ft = ft_init(arr)
        ft_update(ft, 0, 4)
        q = [ft_query(ft, i) for i in range(4)]
        self.assertListEqual(q, [14, 19, 42, 48])
        ft_update(ft, 1, 1)
        q = [ft_query(ft, i) for i in range(4)]
        self.assertListEqual(q, [14, 20, 43, 49])
        ft_update(ft, 2, 3)
        q = [ft_query(ft, i) for i in range(4)]
        self.assertListEqual(q, [14, 20, 46, 52])
        ft_update(ft, 3, 5)
        q = [ft_query(ft, i) for i in range(4)]
        self.assertListEqual(q, [14, 20, 46, 57])
    def test_4_update_neg(self):
        arr = [10, 5, 23, 6]
        ft = ft_init(arr)
        ft_update(ft, 0, -4)
        q = [ft_query(ft, i) for i in range(4)]
        self.assertListEqual(q, [6, 11, 34, 40])
    def test_11(self):
        arr = [68, 94, 79, 80, 88, 69, 14, 28, 17, 78, 70]
        n = len(arr)
        pre = arr[:]
        for i in range(1,n):
            pre[i] += pre[i-1]
        ft = ft_init(arr)
        q = [ft_query(ft, i) for i in range(n)]
        self.assertListEqual(q, pre)
