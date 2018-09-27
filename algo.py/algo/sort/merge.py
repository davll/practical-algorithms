# T = O(n*log(n))
def mergesort(a):
    return _mergesort(a)

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
