# https://www.geeksforgeeks.org/median-two-sorted-arrays-different-sizes-ologminn-m/

from sys import stderr

def median(arr1, arr2):
    from math import inf
    if len(arr1) > len(arr2):
        arr1, arr2 = arr2, arr1
    def get(a, i):
        if i < 0:
            return -inf
        elif i >= len(a):
            return inf
        else:
            return a[i]
    n1, n2 = len(arr1), len(arr2)
    psiz = (n1 + n2) // 2
    lo, hi = 0, n1
    lo, hi = 0, len(arr1)
    index = None
    while lo <= hi:
        i = (lo + hi) // 2
        j = psiz - i
        if get(arr1, i-1) > get(arr2, j):
            hi = i-1
        elif get(arr2, j-1) > get(arr1, i):
            lo = i+1
        else:
            index = i
            break
    i = index
    j = psiz - i
    if (n1 + n2) % 2 == 1:
        return min(get(arr1, i), get(arr2, j))
    else:
        return (max(get(arr1, i-1), get(arr2, j-1)) + min(get(arr1, i), get(arr2, j))) / 2

class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        return median(nums1, nums2)
