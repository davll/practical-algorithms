from typing import Optional, Callable, Sequence, TypeVar, Union
from ..ty import Comparable
from enum import Enum

class Mode(Enum):
    DEFAULT = 0
    LOWER_BOUND = 1
    UPPER_BOUND = 2
    GREATER = 3
    LESS = 4

T = TypeVar('T', bound=Comparable)

def bsearch(func: Callable[[int], T], l: int, r: int, target: T, mode: Mode = Mode.DEFAULT) -> Optional[int]:
    """
    l: lower bound (ex: 0)
    r: upper bound (ex: N-1)
    """
    result = None
    while l <= r:
        m = (l + r) // 2
        k = func(m)
        if target == k:
            result = m
            if mode == Mode.DEFAULT:
                break
            elif mode == Mode.LOWER_BOUND or mode == Mode.RIGHT:
                r = m-1
            elif mode == Mode.UPPER_BOUND or mode == Mode.LEFT:
                l = m+1
        elif target < k:
            # ... target ... k ...
            if mode == Mode.RIGHT:
                result = m
            r = m-1
        else: # k < target
            # ... k ... target ...
            if mode == Mode.LEFT:
                result = m
            l = m+1
    return result

# References:
# https://github.com/python/cpython/blob/3.7/Lib/bisect.py
# https://ai.googleblog.com/2006/06/extra-extra-read-all-about-it-nearly.html
