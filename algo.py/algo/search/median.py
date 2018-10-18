# Find Median

from typing import TypeVar, Sequence, Generic, List, Iterator
from algo.data.heap.binary import min_heap_push, max_heap_push, min_heap_pop, max_heap_pop, min_heap_peak, max_heap_peak

T = TypeVar('T', int, float)

# T = O(log(min(m,n)))
def find_median_of_two_sorted(arr1: Sequence[T], arr2: Sequence[T]) -> float:
    from math import inf
    # arr1 should be smaller than arr2
    if len(arr1) > len(arr2):
        arr1, arr2 = arr2, arr1
    def get(a, i):
        if i < 0:
            return -inf
        elif i >= len(a):
            return inf
        else:
            return a[i]
    #
    # define a partition:
    #
    #       left | right
    #       part | part
    # ---------------------
    # arr1: [:i] | [i:]
    # arr2: [:j] | [j:]
    #
    # where 0 <= i <= len(arr1)
    #       j     = psize - i
    #       psize = (len(arr1) + len(arr2)) / 2
    #
    # p.s. the right part can be bigger than the left part at most one
    #
    n1, n2 = len(arr1), len(arr2)
    psiz = (n1 + n2) // 2
    #
    # find a partition so that
    #     all elements of arr1[:i]+arr2[:j] <= all elements of arr1[i:]+arr2[j:]
    # that is
    #   1) arr1[i-1] <= arr1[i] (trivial)
    #   2) arr1[i-1] <= arr2[j]
    #   3) arr2[j-1] <= arr2[j] (trivial)
    #   4) arr2[j-1] <= arr1[i]
    #
    lo, hi = 0, n1
    lo, hi = 0, len(arr1)
    index = None
    while lo <= hi:
        i = (lo + hi) // 2
        j = psiz - i
        if get(arr1, i-1) > get(arr2, j):
            #
            #  ... (i-1) | (i) ...
            #  ... (j-1) | (j) ...
            #
            # and arr1[i-1] > arr2[j]
            #
            # => move (i-1) to the right part
            # => move (j) to the left part
            #
            #  ... | (i-1) (i) ...
            #  ... (j-1) (j) | ...
            #
            hi = i-1
        elif get(arr2, j-1) > get(arr1, i):
            #
            #  ... (i-1) | (i) ...
            #  ... (j-1) | (j) ...
            #
            # and arr2[j-1] > arr1[i]
            #
            # => move (i) to the left part
            # => move (j-1) to the right part
            #
            #  ... (i-1) (i) | ...
            #  ... | (j-1) (j) ...
            #
            lo = i+1
        else:
            # terminate if the condition is satisfied
            index = i
            break
    i = index
    j = psiz - i
    if (n1 + n2) % 2 == 1:
        return min(get(arr1, i), get(arr2, j))
    else:
        return (max(get(arr1, i-1), get(arr2, j-1)) + min(get(arr1, i), get(arr2, j))) / 2

# Find running medians from stream
class MedianHeap(Generic[T]):
    def __init__(self):
        self.left: List[T] = []
        self.right: List[T] = []
        self.even = True
    #
    def append(self, x: T):
        if self.even:
            min_heap_push(self.right, x)
            max_heap_push(self.left, min_heap_pop(self.right))
        else:
            max_heap_push(self.left, x)
            min_heap_push(self.right, max_heap_pop(self.left))
        self.even = not self.even
    #
    def query(self) -> float:
        if not self.left:
            raise IndexError()
        if self.even:
            ml = max_heap_peak(self.left)
            mr = min_heap_peak(self.right)
            return (ml + mr) / 2
        else:
            return max_heap_peak(self.left)

# https://www.geeksforgeeks.org/k-th-element-two-sorted-arrays/
# https://www.geeksforgeeks.org/median-of-stream-of-integers-running-integers/
# https://www.geeksforgeeks.org/median-of-two-sorted-arrays/
# https://www.geeksforgeeks.org/median-of-two-sorted-arrays-of-different-sizes/
# https://www.geeksforgeeks.org/median-two-sorted-arrays-different-sizes-ologminn-m/
# 
