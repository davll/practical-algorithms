from enum import Enum

class Mode(Enum):
    DEFAULT = 0
    LOWER_BOUND = 1
    UPPER_BOUND = 2

def bsearch(func, l, r, key, mode=Mode.DEFAULT):
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
# Python: bisect in standard library
# https://ai.googleblog.com/2006/06/extra-extra-read-all-about-it-nearly.html
