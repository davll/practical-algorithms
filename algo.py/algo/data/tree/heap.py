# Max-Heap
#
# Consider k-th element of the array (k: 1 indexed)
# - its left child is located at 2*k index
# - its right child is located at 2*k+1 index
# - its parent is located at k/2 index
# - and its parent is larger than or equal to it

# T = O(log(n))
def heapify(h, n, i):
    tmp = i
    # upward
    while i > 0:
        p = (i+1) // 2 - 1 # parent
        if h[p] < h[i]:
            h[p], h[i] = h[i], h[p]
            i = p
        else:
            break
    # downward
    i = tmp
    while i < n:
        l = i * 2 + 1 # left child
        r = i * 2 + 2 # right child
        maxi = i
        if l < n and h[l] > h[maxi]:
            maxi = l
        if r < n and h[r] > h[maxi]:
            maxi = r
        if maxi != i:
            h[i], h[maxi] = h[maxi], h[i]
            i = maxi
        else:
            break

# T = O(n)
def heap_init(a):
    """
    Heapify the input array in place
    a: [T]
    """
    for i in range(1, len(a)+1):
        heapify(a, i, i-1)

# T = O(log(n))
def heap_pop(h):
    h[0], h[-1] = h[-1], h[0]
    heapify(h, len(h)-1, 0)
    return h.pop()

# T = O(log(n))
def heap_push(h, x):
    h.append(x)
    heapify(h, len(h), len(h)-1)
