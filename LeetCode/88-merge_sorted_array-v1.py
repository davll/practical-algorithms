import numpy as np

def merge_v1(nums1, nums2):
    m, n = len(nums1), len(nums2)
    result = [0 for i in range(0, m+n)]
    i, j, k = 0, 0, 0
    while i < m and j < n:
        if nums1[i] <= nums2[j]:
            result[k] = nums1[i]
            i = i + 1
        elif nums1[i] > nums2[j]:
            result[k] = nums2[j]
            j = j + 1
        k = k + 1
    while i < m:
        result[k] = nums1[i]
        i = i + 1
        k = k + 1
    while j < n:
        result[k] = nums2[j]
        j = j + 1
        k = k + 1
    for k in range(0, m+n):
        nums1[k] = result[k]

def merge_v2()

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        merge_array()
