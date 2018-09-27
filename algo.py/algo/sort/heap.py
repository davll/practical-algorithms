from algo.data.tree.heap import heapify, heap_init

# T = O(n*log(n))
def heapsort(a):
    heap_init(a)
    for k in range(len(a)-1, -1, -1):
        a[0], a[k] = a[k], a[0]
        heapify(a, k, 0)
    return a
