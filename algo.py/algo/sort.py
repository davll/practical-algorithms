# Sorting algorithms

# T = O(n^2)
def bubblesort(a):
    n = len(a)
    for _ in range(n):
        for i in range(n-1):
            if a[i] > a[i+1]:
                a[i], a[i+1] = a[i+1], a[i]
    return a

# T = O(n^2)
def selectionsort(a):
    n = len(a)
    for i in range(n-1):
        j = min(range(i, n),  key=lambda j: a[j])
        if i != j:
            a[i], a[j] = a[j], a[i]
    return a

# T = O(n^2)
def insertionsort(a):
    n = len(a)
    for i in range(1, n):
        for j in range(i, 0, -1):
            if a[j-1] > a[j]:
                a[j], a[j-1] = a[j-1], a[j]
            else:
                break
    return a

# T = O(n*log(n))
def heapsort(a):
    from algo.tree.heap import heapify, heap_init
    heap_init(a)
    for k in range(len(a)-1, -1, -1):
        a[0], a[k] = a[k], a[0]
        heapify(a, k, 0)
    return a

# T = O(n*log(n))
def mergesort(a):
    def _merge(xs, ys):
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
    def _mergesort(arr):
        if not arr:
            return []
        if len(arr) == 1:
            return arr
        mid = len(arr) // 2
        xs = _mergesort(arr[:mid])
        ys = _mergesort(arr[mid:])
        return list(_merge(xs, ys))
    return _mergesort(a)

# T = O(nk)
def countsort(arr):
    maxval, minval = max(arr), min(arr)
    n, k = len(arr), (maxval - minval + 1)
    count = [0] * k
    # count values
    for x in arr:
        count[x - minval] += 1
    # transform to actual position
    for i in range(1, k):
        count[i] += count[i-1]
    # build output
    result = [0] * n
    for (i, x) in enumerate(arr):
        j = count[x - minval] - 1
        result[j] = x
        count[x - minval] -= 1
    return result

def bucketsort(arr, nb, key):
    n = len(arr)
    buckets = [[] for _ in range(nb)]
    # group array elements
    for x in arr:
        k = key(x)
        buckets[k].append(x)
    # sort individual buckets
    for b in buckets:
        b.sort()
    # concatenate all buckets
    i = 0
    for b in buckets:
        j = i + len(b)
        arr[i:j] = b[:]
        i = j

# T = O(nw)
def radixsort(arr):
    n, maxval = len(arr), max(arr)
    tmp = [0] * n
    count = [0] * 10
    exp = 1
    while maxval // exp > 0:
        for i in range(10):
            count[i] = 0
        for x in arr:
            count[(x // exp) % 10] += 1
        for i in range(1, 10):
            count[i] += count[i-1]
        for i in range(n-1, -1, -1):
            x = (arr[i] // exp) % 10
            tmp[count[x]-1] = arr[i]
            count[x] -= 1
        arr, tmp = tmp, arr
        exp *= 10
    return arr
