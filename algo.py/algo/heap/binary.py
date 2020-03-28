"""
Binary Heap

Consider k-th element of the array (k: 1 indexed)
- its left child is located at 2*k index
- its right child is located at 2*k+1 index
- its parent is located at k/2 index
- its parent is larger than or equal to it (Max-Heap)
"""

import operator as op

def heap_node_parent(i: int) -> int:
    # same as (i + 1) // 2 - 1
    return (i - 1) // 2

def heap_node_children(i: int) -> int:
    return ((i*2+1), (i*2+2))

def heap_shiftup(h, i: int, lt=op.lt) -> int:
    """
    move up the `i`-th element in `h` to satify its heap property

    Time Complexity: O(log(N))
    """
    while i > 0:
        p = heap_node_parent(i)
        if lt(h[p], h[i]):
            h[p], h[i] = h[i], h[p]
            i = p
        else:
            break
    return i

def heap_shiftdown(h, n: int, i: int, lt=op.lt) -> int:
    """
    move down the `i`-th element in `h` to satify its heap property

    Time Complexity: O(log(N))
    """
    while i < n:
        l, r = heap_node_children(i)
        maxi = i
        if l < n and lt(h[maxi], h[l]):
            maxi = l
        if r < n and lt(h[maxi], h[r]):
            maxi = r
        if maxi != i:
            h[i], h[maxi] = h[maxi], h[i]
            i = maxi
        else:
            break
    return i

max_heap_lt = op.lt
min_heap_lt = op.gt

def heap_peak(h):
    """
    Peak the root of the heap `h`

    Time Complexity: O(1)
    """
    return h[0]

def heap_init(a, lt=op.lt) -> None:
    """
    Initialize the heap `a` inplace

    Time Complexity: O(N)
    """
    for i in range(1, len(a)+1):
        heap_shiftup(a, i-1, lt=lt)

def heap_pop(h, lt=op.lt):
    """
    Extract the largest value from the heap `h`

    Time Complexity: O(log(N))
    """
    h[0], h[-1] = h[-1], h[0]
    heap_shiftdown(h, len(h)-1, 0, lt=lt)
    return h.pop()

def heap_push(h, x, lt=op.lt) -> None:
    """
    Add the value `x` to the heap `h`

    Time Complexity: O(log(N))
    """
    h.append(x)
    heap_shiftup(h, len(h)-1, lt=lt)

def _make_heap_func(lt):
    def peak(h):
        return heap_peak(h)
    def init(a):
        return heap_init(a, lt=lt)
    def pop(h):
        return heap_pop(h, lt=lt)
    def push(h, x):
        return heap_push(h, x, lt=lt)
    return (peak, init, pop, push)

max_heap_peak, max_heap_init, max_heap_pop, max_heap_push = _make_heap_func(max_heap_lt)
min_heap_peak, min_heap_init, min_heap_pop, min_heap_push = _make_heap_func(min_heap_lt)

def make_graph(h):
    from graphviz import Digraph, nohtml
    g = Digraph(node_attr={'shape': 'record', 'height': '.1'})
    for i, k in enumerate(h):
        g.node('node-{}'.format(i), nohtml("<f0>|<f1> {}|<f2>".format(k)))
    n = len(h)
    for i, k in enumerate(h):
        l, r = heap_node_children(i)
        if l < n:
            g.edge("node-{}:f0".format(i), "node-{}:f1".format(l))
        if r < n:
            g.edge("node-{}:f2".format(i), "node-{}:f1".format(r))
    return g

if __name__ == "__main__":
    a = [5, 2, 10, 3, 1, 6, 8]
    heap_init(a)
    g = make_graph(a)
    g.view()
