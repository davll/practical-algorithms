from unittest import TestCase
from ..binary import binary_search, lower_bound, upper_bound

class TestBinarySearch(TestCase):
    def test_default_1(self):
        arr = [10, 20, 25, 30, 100]
        n = len(arr)
        for i, x in enumerate(arr):
            pos = binary_search(lambda i: arr[i], 0, n, x)
            self.assertEqual(pos, i)
        for x in range(0, arr[0]):
            pos = binary_search(lambda i: arr[i], 0, n, x)
            self.assertIsNone(pos)
        for i in range(1, n):
            for x in range(arr[i-1]+1, arr[i]):
                pos = binary_search(lambda i: arr[i], 0, n, x)
                self.assertIsNone(pos)
        for x in range(arr[-1]+1, 200):
            pos = binary_search(lambda i: arr[i], 0, n, x)
            self.assertIsNone(pos)
    def test_lower_bound_1(self):
        arr = [-1, -1, -1, 1, 3, 3, 5, 5, 5, 5, 7, 10, 10, 10]
        n = len(arr)
        kv = [
            (-1, 0),
            (1, 3),
            (3, 4),
            (5, 6),
            (7, 10),
            (10, 11),
            (-2, 0),
            (4, 6),
            (100, 14)
        ]
        for x, i in kv:
            pos = lower_bound(arr, 0, n, x)
            self.assertEqual(pos, i)
    def test_upper_bound_1(self):
        arr = [-1, -1, -1, 1, 3, 3, 5, 5, 5, 5, 7, 10, 10, 10]
        n = len(arr)
        kv = [
            (-1, 3),
            (1, 4),
            (3, 6),
            (5, 10),
            (7, 11),
            (10, 14),
            (-2, 0),
            (4, 6),
            (100, 14)
        ]
        for x, i in kv:
            pos = upper_bound(arr, 0, n, x)
            self.assertEqual(pos, i)
