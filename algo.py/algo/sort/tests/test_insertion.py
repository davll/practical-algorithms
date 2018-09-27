from unittest import TestCase
from ..insertion import insertionsort

class TestInsertionSort(TestCase):
    def test1(self):
        arr = [3, 44, 38, 5, 47, 15, 36, 26, 27, 2, 46, 4, 19, 50, 48]
        exp = list(sorted(arr))
        insertionsort(arr)
        self.assertListEqual(arr, exp)
