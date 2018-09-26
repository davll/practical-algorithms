# Comparison-based sorting algorithms

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
    from tree.heap import heapify, heap_init
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
        mid = len(arr) // 2
        xs = _mergesort(arr[:mid])
        ys = _mergesort(arr[mid:])
        return list(_merge(xs, ys))
    return _mergesort(a)

def test():
    arr = [3, 44, 38, 5, 47, 15, 36, 26, 27, 2, 46, 4, 19, 50, 48]
    exp = list(sorted(arr))
    ans1 = bubblesort(arr[:])
    ans2 = selectionsort(arr[:])
    ans3 = insertionsort(arr[:])
    ans4 = heapsort(arr[:])
    #ans5 = mergesort(arr)
    assert exp == ans1
    assert exp == ans2
    assert exp == ans3
    assert exp == ans4

if __name__ == "__main__":
    test()
