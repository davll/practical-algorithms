# Max-Heap
#
# Consider k-th element of the array (k: 1 indexed)
# - its left child is located at 2*k index
# - its right child is located at 2*k+1 index
# - its parent is located at k/2 index
# - and its parent is larger than or equal to it

import unittest

def heap_init(a):
    """
    Heapify the input array in place
    a: [T]
    """
    for i in range(1, len(a)+1):
        while i > 1:
            # k: parent of i
            k = i // 2
            if a[i-1] > a[k-1]:
                a[i-1], a[k-1] = a[k-1], a[i-1]
            i = k

def heap_sort(h):
    """
    Sort the input heapified array in place
    h: [T]
    """
    for k in range(len(h)-1, -1, -1):
        h[0], h[k] = h[k], h[0]
        i, n = 1, k
        while i <= n:
            # l, r: children of i
            l, r = 2*i, 2*i+1
            # v: max value, t: selected index
            v, t = h[i-1], i
            if l <= n and v < h[l-1]:
                v, t = h[l-1], l
            if r <= n and v < h[r-1]:
                v, t = h[r-1], r
            if t != i:
                h[i-1], h[t-1] = h[t-1], h[i-1]
                i = t
            else:
                break

class TestHeap(unittest.TestCase):
    def test_init(self):
        for n in range(1, 16):
            a = list(range(1,n+1))
            heap_init(a)
            #print(str(a))
            for i in range(n,0,-1):
                p = i // 2
                if p >= 1:
                    #print("i = " + str(i) + ", p = " + str(p))
                    #print("a[i] = " + str(a[i-1]) + ", a[p] = " + str(a[p-1]))
                    self.assertGreaterEqual(a[p-1], a[i-1])
    #
    def test_sort(self):
        for n in range(1, 16):
            a = list(range(1,n+1))
            heap_init(a)
            heap_sort(a)
            #print(str(a))
            for i in range(0,n-1):
                self.assertLessEqual(a[i], a[i+1])

if __name__ == '__main__':
    unittest.main()
