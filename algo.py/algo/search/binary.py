from typing import Optional, Callable, Sequence, TypeVar, Union
from ..ty import Comparable

T = TypeVar('T', bound=Comparable)

def _make_func(seq_or_func: Union[Sequence[T], Callable[[int], T]]) -> Callable[[int], T]:
    if callable(seq_or_func):
        return seq_or_func
    else:
        return lambda i: seq_or_func[i]

def binary_search(seq_or_func: Union[Sequence[T], Callable[[int], T]], first: int, end: int, target: T) -> Optional[int]:
    """Find the element in the range [first, end) with its value = target"""
    func = _make_func(seq_or_func)
    while first < end:
        mid = (first + end) // 2
        value = func(mid)
        if target == value:
            # the target is right on mid
            return mid
        elif target < value:
            # the target is on the left of mid
            end = mid
        else:
            # the target is on the right of mid
            first = mid + 1
    return None

def lower_bound(seq_or_func: Union[Sequence[T], Callable[[int], T]], first: int, end: int, target: T) -> int:
    """Find the first element in the range [first, end) with its value >= target"""
    func = _make_func(seq_or_func)
    result = end
    while first < end:
        mid = (first + end) // 2
        value = func(mid)
        if target <= value:
            result = mid
            end = mid
        else:
            first = mid + 1
    return result

def upper_bound(seq_or_func: Union[Sequence[T], Callable[[int], T]], first: int, end: int, target: T) -> int:
    """Find the first element in the range [first, end) with its value > target"""
    func = _make_func(seq_or_func)
    result = end
    while first < end:
        mid = (first + end) // 2
        value = func(mid)
        if target < value:
            result = mid
            end = mid
        else:
            first = mid + 1
    return result

def floor_search(seq_or_func: Union[Sequence[T], Callable[[int], T]], first: int, end: int, target: T) -> Optional[int]:
    """Find the last element in the range [first, end) with its value < target"""
    func = _make_func(seq_or_func)
    result = None
    raise NotImplementedError()
    return result

# References:
# https://github.com/python/cpython/blob/3.7/Lib/bisect.py
# https://ai.googleblog.com/2006/06/extra-extra-read-all-about-it-nearly.html
# http://www.cplusplus.com/reference/algorithm/binary_search/
# http://www.cplusplus.com/reference/algorithm/lower_bound/
# http://www.cplusplus.com/reference/algorithm/upper_bound/
# https://en.cppreference.com/w/cpp/algorithm/lower_bound
# https://www.geeksforgeeks.org/lower_bound-in-cpp/
