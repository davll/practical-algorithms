# Heap Sort

from ..heap.binary import heap_shiftdown, max_heap_lt, heap_init

# T = O(n*log(n))
def heapsort(a):
    """
    Sort an array inplace with heap

    - Worst case: O(n*log(n))
    - Avg case: O(n*log(n))
    - Best case: O(n*log(n)) distinct keys, O(n) equal keys
    - Worst case space: O(1) aux
    """
    heap_init(a)
    for k in range(len(a)-1, -1, -1):
        a[0], a[k] = a[k], a[0]
        heap_shiftdown(a, k, 0, lt=max_heap_lt)
