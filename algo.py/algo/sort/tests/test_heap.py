from unittest import TestCase
from ..heap import heapsort

class TestHeapSort(TestCase):
    def test1(self):
        arr = [3, 44, 38, 5, 47, 15, 36, 26, 27, 2, 46, 4, 19, 50, 48]
        exp = list(sorted(arr))
        heapsort(arr)
        self.assertListEqual(arr, exp)
