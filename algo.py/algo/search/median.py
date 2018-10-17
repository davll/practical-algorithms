# Find Median

from typing import TypeVar, Sequence, List, Iterator

T = TypeVar('T', int, float)

# T = O()
def median_of_two_sorted(arr1: Sequence[T], arr2: Sequence[T]) -> float:
    pass

def running_median(nums: Iterator[T]) -> Iterator[float]:
    from algo.data.heap.binary import min_heap_push, max_heap_push, min_heap_pop, max_heap_pop, heap_peak
    #
    left: List[T] = [] # max-heap
    right: List[T] = [] # min-heap
    #
    def push(x: T) -> None:
        max_heap_push(left, x)
        if right:
            while heap_peak(left) > heap_peak(right):
                x = max_heap_pop(left)
                min_heap_push(right, x)
        while len(left) > len(right) + 1:
            x = max_heap_pop(left)
            min_heap_push(right, x)
        while len(left) + 1 < len(right):
            x = min_heap_pop(right)
            max_heap_push(left, x)
    #
    def query() -> float:
        nl, nr = len(left), len(right)
        assert abs(nl - nr) <= 1
        if nl == 0 and nr == 0:
            raise IndexError()
        elif nl > nr:
            return heap_peak(left)
        elif nl < nr:
            return heap_peak(right)
        else: # nl == nr
            ml = heap_peak(left)
            mr = heap_peak(right)
            return (ml + mr) / 2
    #
    for x in iter(nums):
        push(x)
        yield query()

# https://www.geeksforgeeks.org/k-th-element-two-sorted-arrays/
# https://www.geeksforgeeks.org/median-of-stream-of-integers-running-integers/
# https://www.geeksforgeeks.org/median-of-two-sorted-arrays/
# https://www.geeksforgeeks.org/median-of-two-sorted-arrays-of-different-sizes/
# https://www.geeksforgeeks.org/median-two-sorted-arrays-different-sizes-ologminn-m/
# 
