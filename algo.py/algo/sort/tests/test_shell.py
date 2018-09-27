from unittest import TestCase
from ..shell import shellsort

class TestShellSort(TestCase):
    def test1(self):
        arr = [3, 44, 38, 5, 47, 15, 36, 26, 27, 2, 46, 4, 19, 50, 48]
        exp = list(sorted(arr))
        shellsort(arr)
        self.assertListEqual(arr, exp)
