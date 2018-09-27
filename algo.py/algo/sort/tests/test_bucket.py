from unittest import TestCase
from ..bucket import bucketsort

class TestBucketSort(TestCase):
    def test1(self):
        arr = [3, 44, 38, 5, 47, 15, 36, 26, 27, 2, 46, 4, 19, 50, 48]
        exp = list(sorted(arr))
        bucketsort(arr, 10, key=lambda x: x // 10)
        self.assertListEqual(arr, exp)
