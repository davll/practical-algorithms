# Max-Heap
#
# Consider k-th element of the array (k: 1 indexed)
# - its left child is located at 2*k index
# - its right child is located at 2*k+1 index
# - its parent is located at k/2 index
# - and its parent is larger than or equal to it

import unittest

# T = O(log(n))
def heapify(h, n, i):
    tmp = i
    # upward
    while i > 0:
        p = (i+1) // 2 - 1 # parent
        if h[p] < h[i]:
            h[p], h[i] = h[i], h[p]
            i = p
        else:
            break
    # downward
    i = tmp
    while i < n:
        l = i * 2 + 1 # left child
        r = i * 2 + 2 # right child
        maxi = i
        if l < n and h[l] > h[maxi]:
            maxi = l
        if r < n and h[r] > h[maxi]:
            maxi = r
        if maxi != i:
            h[i], h[maxi] = h[maxi], h[i]
            i = maxi
        else:
            break

# T = O(n)
def heap_init(a):
    """
    Heapify the input array in place
    a: [T]
    """
    for i in range(1, len(a)+1):
        heapify(a, i, i-1)

# T = O(n*log(n))
def heap_sort(h):
    """
    Sort the input heapified array in place
    h: [T]
    """
    for k in range(len(h)-1, -1, -1):
        h[0], h[k] = h[k], h[0]
        heapify(h, k, 0)

class TestHeap(unittest.TestCase):
    def test_init(self):
        for n in range(1, 16):
            a = list(reversed(range(1,n+1)))
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
            a = list(reversed(range(1,n+1)))
            heap_init(a)
            heap_sort(a)
            #print(str(a))
            for i in range(0,n-1):
                self.assertLessEqual(a[i], a[i+1])

if __name__ == '__main__':
    unittest.main()
