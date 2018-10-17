import operator as op
import heapq

class MedianFinder:
    def __init__(self):
        self.left = []
        self.right = []
        self.even = True
    def addNum(self, x):
        """
        :type num: int
        :rtype: void
        """
        if self.even:
            min_heap_push(self.right, x)
            max_heap_push(self.left, min_heap_pop(self.right))
        else:
            max_heap_push(self.left, x)
            min_heap_push(self.right, max_heap_pop(self.left))
        self.even = not self.even
    #
    def findMedian(self):
        """
        :rtype: float
        """
        if self.even:
            ml = max_heap_peak(self.left)
            mr = min_heap_peak(self.right)
            return (ml + mr) / 2
        else:
            return max_heap_peak(self.left)

def max_heap_peak(h):
    return -h[0]

def min_heap_peak(h):
    return h[0]

# T = O(log(n))
def max_heap_pop(h):
    return -heapq.heappop(h)

# T = O(log(n))
def max_heap_push(h, x):
    heapq.heappush(h, -x)

# T = O(log(n))
def min_heap_pop(h):
    return heapq.heappop(h)

# T = O(log(n))
def min_heap_push(h, x):
    heapq.heappush(h, x)

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
