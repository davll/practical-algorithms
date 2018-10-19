from typing import Optional, Callable, Sequence, TypeVar, Union
from ..ty import Comparable
from enum import Enum

class Mode(Enum):
    DEFAULT = 0
    LOWER_BOUND = 1
    UPPER_BOUND = 2

T = TypeVar('T', bound=Comparable)

def bsearch(func: Callable[[int], T], l: int, r: int, key: T, mode: Mode = Mode.DEFAULT) -> Optional[int]:
    """
    func
    l: lower bound (ex: 0)
    r: upper bound (ex: N-1)
    key: target key
    """
    result = None
    while l <= r:
        m = (l + r) // 2
        k = func(m)
        if key == k:
            result = m
            if mode == Mode.DEFAULT:
                break
            elif mode == Mode.LOWER_BOUND:
                r = m-1
            elif mode == Mode.UPPER_BOUND:
                l = m+1
        elif key < k:
            r = m-1
        else: # key > k
            l = m+1
    return result

# References:
# https://github.com/python/cpython/blob/3.7/Lib/bisect.py
# https://ai.googleblog.com/2006/06/extra-extra-read-all-about-it-nearly.html
