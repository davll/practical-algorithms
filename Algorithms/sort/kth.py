# https://www.geeksforgeeks.org/k-th-element-two-sorted-arrays/

import unittest

# T = O(k)
def kth_v1(l1, l2, k):
    """
    l1: [T] => an ascending sorted array
    l2: [T] => an ascending sorted array
    k: int => 0 indexed. ex: k = 0 for 1st element
    return: T => the k-th element of the final sorted array
    """
    i, j, m, n = 0, 0, len(l1), len(l2)
    while k > 0 and i < m and j < n:
        if l1[i] < l2[j]:
            i, k = i+1, k-1
        else:
            j, k = j+1, k-1
    if k > 0 and i < m:
        i, k = i+k, 0
    if k > 0 and j < n:
        j, k = j+k, 0
    if i < m and j < n:
        return min(l1[i], l2[j])
    elif i < m:
        return l1[i]
    else:
        return l2[j]

# T = O(log(m)+log(n))
def kth_v2(l1, l2, k):
    """
    l1: [T] => an ascending sorted array
    l2: [T] => an ascending sorted array
    k: int => 0 indexed. ex: k = 0 for 1st element
    return: T => the k-th element of the final sorted array
    """
    if not l1:
        return l2[k]
    elif not l2:
        return l1[k]
    def _bs(r1, r2, k):
        (s1, t1), (s2, t2) = r1, r2
        if s1 == t1:
            return l2[s2+k]
        elif s2 == t2:
            return l1[s1+k]
        m1, m2 = (t1-s1)//2, (t2-s2)//2
        if m1 + m2 < k:
            if l1[s1+m1] > l2[s2+m2]:
                return _bs((s1, t1), (s2+m2+1, t2), k-m2-1)
            else:
                return _bs((s1+m1+1, t1), (s2, t2), k-m1-1)
        else:
            if l1[s1+m1] > l2[s2+m2]:
                return _bs((s1, s1+m1), (s2, t2), k)
            else:
                return _bs((s1, t1), (s2, s2+m2), k)
    return _bs((0, len(l1)), (0, len(l2)), k)

# T = O(log(k))
def kth_v3(l1, l2, k):
    """
    l1: [T] => an ascending sorted array
    l2: [T] => an ascending sorted array
    k: int => 0 indexed. ex: k = 0 for 1st element
    return: T => the k-th element of the final sorted array
    """
    if not l1:
        return l2[k]
    elif not l2:
        return l1[k]
    def _bs(l1, l2, r1, r2, k):
        (s1,t1), (s2,t2) = r1, r2
        if (t1-s1) > (t2-s2):
            # force r1 <= r2
            return _bs(l2, l1, r2, r1, k)
        if s1 == t1:
            return l2[s2+k-1]
        if k == 1:
            return min(l1[s1], l2[s2])
        # divide and conquer
        i, j = min(t1-s1, k//2), min(t2-s2, k//2)
        if l1[s1+i-1] > l2[s2+j-1]:
            return _bs(l1, l2, (s1, t1), (s2+j, t2), k-j)
        else:
            return _bs(l1, l2, (s1+i, t1), (s2, t2), k-i)
    return _bs(l1, l2, (0, len(l1)), (0, len(l2)), k+1)
