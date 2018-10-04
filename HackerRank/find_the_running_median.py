# https://www.hackerrank.com/challenges/find-the-running-median/problem

import operator as op
from sys import stdin, stdout, stderr

def heapify(h, n: int, i: int, lt=op.lt) -> None:
    """Heapify the array in place
    """
    # upward
    while i > 0:
        p = (i - 1) // 2 # parent
        if lt(h[p], h[i]):
            h[p], h[i] = h[i], h[p]
            i = p
        else:
            return
    # downward
    while i < n:
        l = i * 2 + 1 # left child
        r = i * 2 + 2 # right child
        maxi = i
        if l < n and lt(h[maxi], h[l]):
            maxi = l
        if r < n and lt(h[maxi], h[r]):
            maxi = r
        if maxi != i:
            h[i], h[maxi] = h[maxi], h[i]
            i = maxi
        else:
            return

def heap_peak(h):
    return h[0]

def max_heapify(h, n: int, i: int) -> None:
    heapify(h, n, i, lt=op.lt)

def min_heapify(h, n: int, i: int) -> None:
    heapify(h, n, i, lt=op.gt)

def max_heap_pop(h):
    h[0], h[-1] = h[-1], h[0]
    max_heapify(h, len(h)-1, 0)
    return h.pop()

def max_heap_push(h, x):
    h.append(x)
    max_heapify(h, len(h), len(h)-1)

def min_heap_pop(h):
    h[0], h[-1] = h[-1], h[0]
    min_heapify(h, len(h)-1, 0)
    return h.pop()

def min_heap_push(h, x):
    h.append(x)
    min_heapify(h, len(h), len(h)-1)

class MedianHeap:
    def __init__(self) -> None:
        self.left = []
        self.right = []
    #
    def query(self) -> float:
        nl, nr = len(self.left), len(self.right)
        if nl == 0 and nr == 0:
            raise IndexError()
        elif nl > nr:
            return heap_peak(self.left)
        elif nl < nr:
            return heap_peak(self.right)
        else: # nl == nr
            ml = heap_peak(self.left)
            mr = heap_peak(self.right)
            return (ml + mr) / 2
    #
    def insert(self, x) -> None:
        if not self.left and not self.right:
            max_heap_push(self.left, x)
        elif x <= heap_peak(self.left):
            max_heap_push(self.left, x)
            if len(self.left) > len(self.right) + 1:
                x = max_heap_pop(self.left)
                min_heap_push(self.right, x)
        elif not self.right or x >= heap_peak(self.right):
            min_heap_push(self.right, x)
            if len(self.left) + 1 < len(self.right):
                x = min_heap_pop(self.right)
                max_heap_push(self.left, x)
        elif len(self.left) < len(self.right):
            max_heap_push(self.left, x)
        else:
            min_heap_push(self.right, x)

def runningMedian(n, a):
    mh = MedianHeap()
    for x in a:
        mh.insert(x)
        yield mh.query()

if __name__ == "__main__":
    n = int(stdin.readline().rstrip())
    a = [int(stdin.readline().rstrip()) for _ in range(n)]
    for m in runningMedian(n, a):
        stdout.write(str(m) + '\n')
