# Merge Sort
#
# Worst case: O(n*log(n))
# Avg case: O(n*log(n))
# Best case: O(n*log(n)) typical, O(n) natural variant
# Worst case space: O(n) aux; O(1) aux for linked lists
#

from typing import TypeVar, List, Iterator
from algo.data.array import merge_sorted

T = TypeVar('T', int, float)

def mergesort(arr: List[T]) -> List[T]:
    if not arr:
        return []
    if len(arr) == 1:
        return arr
    mid = len(arr) // 2
    xs = mergesort(arr[:mid])
    ys = mergesort(arr[mid:])
    return list(merge_array(xs, ys))

def merge_array(xs: List[T], ys: List[T]) -> Iterator[T]:
    i, j, xn, yn = 0, 0, len(xs), len(ys)
    while i < xn and j < yn:
        if xs[i] < ys[j]:
            yield xs[i]
            i += 1
        else:
            yield ys[j]
            j += 1
    yield from iter(xs[i:])
    yield from iter(ys[j:])
