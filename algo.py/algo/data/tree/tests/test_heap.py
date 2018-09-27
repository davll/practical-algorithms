from unittest import TestCase
from ..heap import heap_init, heap_push, heap_pop
from sys import stderr

def _arr1():
    return [2, 7, 26, 25, 19, 17, 1, 90, 3, 36]

class TestHeap(TestCase):
    def test_init(self):
        h = _arr1()
        heap_init(h)
        #print(str(h), file=stderr)
        self._check_heap(h)
    def test_push(self):
        h = _arr1()
        heap_init(h)
        heap_push(h, 50)
        self._check_heap(h)
    def test_pop(self):
        h = _arr1()
        heap_init(h)
        x = heap_pop(h)
        self.assertEqual(x, 90)
        self._check_heap(h)
    def _check_heap(self, h):
        for i in range(len(h), 1, -1):
            p = i // 2
            self.assertLessEqual(h[i-1], h[p-1], msg="p={p}, i={i}".format(i=i,p=p))
