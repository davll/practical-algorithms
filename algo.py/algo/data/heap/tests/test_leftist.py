from unittest import TestCase
from ..leftist import LeftistHeap
from sys import stderr

class TestLeftistHeap(TestCase):
    def test_init(self):
        lh = LeftistHeap()
        self.assertIsInstance(lh, LeftistHeap)
    def test_push(self):
        arr = [2, 7, 26, 25, 19, 17, 1, 90, 3, 36]
        lh = LeftistHeap()
        for x in arr:
            lh.push(x)
    def test_pop(self):
        arr = [2, 7, 26, 25, 19, 17, 1, 90, 3, 36]
        lh = LeftistHeap()
        for x in arr:
            lh.push(x)
        for x in sorted(arr):
            y = lh.pop()
            self.assertEqual(x, y)
    def test_peek(self):
        arr = [2, 7, 26, 25, 19, 17, 1, 90, 3, 36]
        peaks = arr[:1]
        for x in arr[1:]:
            peaks.append(min(peaks[-1], x))
        lh = LeftistHeap()
        for x, y in zip(arr, peaks):
            lh.push(x)
            self.assertEqual(lh.peak(), y)
