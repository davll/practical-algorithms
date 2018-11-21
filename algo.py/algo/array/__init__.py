from typing import TypeVar, Iterator, Sequence, MutableSequence

T = TypeVar('T', int, float)

def merge_sorted(xs: Sequence[T], ys: Sequence[T], xl: int, xr: int, yl: int, yr: int) -> Iterator[T]:
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

def reverse(xs: MutableSequence[T], l: int, r: int) -> None:
    while l < r:
        xs[l], xs[r] = xs[r], xs[l]
        l, r = l+1, r-1

def right_rotate(xs: MutableSequence[T], k: int) -> None:
    raise NotImplementedError()
