# Binary Search
#
# https://ai.googleblog.com/2006/06/extra-extra-read-all-about-it-nearly.html

def _make_func(seq_or_func):
    if callable(seq_or_func):
        return seq_or_func
    else:
        return lambda i: seq_or_func[i]

def binary_search(seq_or_func, first: int, end: int, target):
    """
    Find a element in the range [first, end) with its value == target

    Time Complexity: O(log(n))
    """
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

def lower_bound(seq_or_func, first: int, end: int, target) -> int:
    """
    Find the first element in the range [first, end) with its value >= target

    Example:
        i = lower_bound(arr, 0, len(arr), k)
        # all the elements of arr[i:] are greater than or equal to k
        # all the elements of arr[:i] are less than k
    
    Time Complexity: O(log(n))
    """
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

def upper_bound(seq_or_func, first: int, end: int, target) -> int:
    """
    Find the first element in the range [first, end) with its value > target

    Example:
        i = lower_bound(arr, 0, len(arr), k)
        # all the elements of arr[i:] are greater than k
        # all the elements of arr[:i] are less than or equal to k
    
    Time Complexity: O(log(n))
    """
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

# References:
#
# https://github.com/python/cpython/blob/3.7/Lib/bisect.py
# http://www.cplusplus.com/reference/algorithm/binary_search/
# http://www.cplusplus.com/reference/algorithm/lower_bound/
# http://www.cplusplus.com/reference/algorithm/upper_bound/
# https://en.cppreference.com/w/cpp/algorithm/lower_bound
# https://www.geeksforgeeks.org/lower_bound-in-cpp/
