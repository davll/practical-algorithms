from unittest import TestCase
from ..median import MedianHeap

class TestMedianHeap(TestCase):
    def test1(self):
        mh = MedianHeap()
        a = [12, 4, 5, 3, 8, 7]
        m = []
        for x in a:
            mh.insert(x)
            m.append(mh.query())
        self.assertListEqual(m, [12, 8, 5, 4.5, 5, 6])
