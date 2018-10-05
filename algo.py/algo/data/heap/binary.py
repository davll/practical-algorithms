# Binary Heap
#
# Consider k-th element of the array (k: 1 indexed)
# - its left child is located at 2*k index
# - its right child is located at 2*k+1 index
# - its parent is located at k/2 index
# - its parent is larger than or equal to it (Max-Heap)

from typing import TypeVar, Generic, MutableSequence, Callable
import operator as op

T = TypeVar('T')

# T = O(log(n))
def heapify(h: MutableSequence[T], n: int, i: int, lt: Callable[[T,T],bool] = op.lt) -> None:
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

def max_heapify(h: MutableSequence[T], n: int, i: int) -> None:
    heapify(h, n, i, lt=op.lt)

def min_heapify(h: MutableSequence[T], n: int, i: int) -> None:
    heapify(h, n, i, lt=op.gt)

# T = O(1)
def heap_peak(h: MutableSequence[T]) -> T:
    return h[0]

# T = O(n)
def max_heap_init(a: MutableSequence[T]) -> None:
    for i in range(1, len(a)+1):
        max_heapify(a, i, i-1)

# T = O(log(n))
def max_heap_pop(h: MutableSequence[T]) -> T:
    h[0], h[-1] = h[-1], h[0]
    max_heapify(h, len(h)-1, 0)
    return h.pop()

# T = O(log(n))
def max_heap_push(h: MutableSequence[T], x: T) -> None:
    h.append(x)
    max_heapify(h, len(h), len(h)-1)

# T = O(n)
def min_heap_init(a: MutableSequence[T]) -> None:
    for i in range(1, len(a)+1):
        min_heapify(a, i, i-1)

# T = O(log(n))
def min_heap_pop(h: MutableSequence[T]) -> T:
    h[0], h[-1] = h[-1], h[0]
    min_heapify(h, len(h)-1, 0)
    return h.pop()

# T = O(log(n))
def min_heap_push(h: MutableSequence[T], x: T) -> None:
    h.append(x)
    min_heapify(h, len(h), len(h)-1)

heap_init = max_heap_init
heap_pop = max_heap_pop
heap_push = max_heap_push
