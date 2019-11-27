from collections.abc import Sequence

class ListSlice(Sequence):
    def __init__(self, arr, start = 0, end = None):
        self.arr = arr
        self.start = start
        self.end = end if end is not None else len(arr)
    #
    def __len__(self):
        return self.end - self.start
    #
    def __getitem__(self, i):
        return self.arr[(i + self.start)]
    #
    def __setitem__(self, i, x):
        self.arr[(i + self.start)] = x

def merge_sorted(xs, ys, xl: int, xr: int, yl: int, yr: int):
    while xl < xr and yl < yr:
        if xs[xl] < ys[yl]:
            yield xs[xl]
            xl += 1
        else:
            yield ys[yl]
            yl += 1
    while xl < xr:
        yield xs[xl]
        xl += 1
    while yl < yr:
        yield ys[yl]
        yl += 1

def reverse(xs, l=0, r=None):
    r = len(xs) if r is None else r
    r = r-1
    while l < r:
        xs[l], xs[r] = xs[r], xs[l]
        l, r = l+1, r-1

def right_rotate(xs, k: int):
    raise NotImplementedError()
