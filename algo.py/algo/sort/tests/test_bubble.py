from unittest import TestCase
from ..bubble import bubblesort

class TestBubbleSort(TestCase):
    def test1(self):
        arr = [3, 44, 38, 5, 47, 15, 36, 26, 27, 2, 46, 4, 19, 50, 48]
        exp = list(sorted(arr))
        bubblesort(arr)
        self.assertListEqual(arr, exp)
