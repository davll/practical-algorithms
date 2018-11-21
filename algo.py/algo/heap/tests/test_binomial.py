from unittest import TestCase
from ..binomial import BinomialHeap
from sys import stderr

class TestBinomialHeap(TestCase):
    def test_init(self):
        bh = BinomialHeap()
        self.assertIsInstance(bh, BinomialHeap)
    def test_push(self):
        arr = [2, 7, 26, 25, 19, 17, 1, 90, 3, 36]
        bh = BinomialHeap()
        for x in arr:
            bh.push(x)
    def test_pop(self):
        arr = [2, 7, 26, 25, 19, 17, 1, 90, 3, 36]
        bh = BinomialHeap()
        for x in arr:
            bh.push(x)
        for x in sorted(arr):
            y = bh.pop()
            self.assertEqual(x, y)
    def test_peek(self):
        arr = [2, 7, 26, 25, 19, 17, 1, 90, 3, 36]
        peaks = arr[:1]
        for x in arr[1:]:
            peaks.append(min(peaks[-1], x))
        bh = BinomialHeap()
        for x, y in zip(arr, peaks):
            bh.push(x)
            self.assertEqual(bh.peak(), y)
