class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
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
