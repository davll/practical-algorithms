# Find Median

from typing import TypeVar, Sequence, Generic, List, Iterator
from algo.data.heap.binary import min_heap_push, max_heap_push, min_heap_pop, max_heap_pop, min_heap_peak, max_heap_peak

T = TypeVar('T', int, float)

# T = O(log(min(m,n)))
def find_median_of_two_sorted(arr1: Sequence[T], arr2: Sequence[T]):
    # arr1 should be smaller than arr2
    if len(arr1) > len(arr2):
        arr1, arr2 = arr2, arr1
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
    n1, n2 = len(arr1), len(arr2)
    psize = (n1 + n2) // 2
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
    while lo < hi:
        i = (lo + hi) // 2
        j = psize - i
        yield (i, j, lo, hi)
        if i == 0 or arr1[i-1] > arr2[j]:
            hi = i
        elif j == 0 or arr2[j-1] > arr2[i]:
            lo = i
    #
    i, j = lo, psize - lo
    yield (i, j, lo, hi)
    #if (n1 + n2) % 2 == 1:
    #    return min(arr1[i:i+1] + arr2[j:j+1])
    #else:
    #    return (max(arr1[i-1:i] + arr2[j-1:j]) + min(arr1[i:i+1] + arr2[j:j+1])) / 2

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

if __name__ == "__main__":
    a1 = [1, 2]
    a2 = [3, 4]
    #a1 = [-5, 3, 6, 12, 15]
    #a2 = [-12, -10, -6, -3, 4, 10]
    #print(str(find_median_of_two_sorted(a1, a2)))
    for i, j, lo, hi in find_median_of_two_sorted(a1, a2):
        print("lo = {lo}, hi = {hi}".format(lo=lo, hi=hi))
        print("a1[:{i}:]: [{l} | {r}]".format(i=i, l=' '.join(map(str, a1[:i])), r=' '.join(map(str, a1[i:]))))
        print("a2[:{i}:]: [{l} | {r}]".format(i=j, l=' '.join(map(str, a2[:j])), r=' '.join(map(str, a2[j:]))))
