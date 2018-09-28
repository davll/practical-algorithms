# Heap Sort
#
# Worst case: O(n*log(n))
# Avg case: O(n*log(n))
# Best case: O(n*log(n)) distinct keys, O(n) equal keys
# Worst case space: O(1) aux
#

from algo.data.tree.heap import heapify, heap_init
from typing import TypeVar, MutableSequence

T = TypeVar('T', int, float)

# T = O(n*log(n))
def heapsort(a: MutableSequence[T]) -> None:
    heap_init(a)
    for k in range(len(a)-1, -1, -1):
        a[0], a[k] = a[k], a[0]
        heapify(a, k, 0)