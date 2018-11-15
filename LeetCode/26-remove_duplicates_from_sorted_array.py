# https://leetcode.com/problems/remove-duplicates-from-sorted-array/

def dedup(arr):
    if not arr:
        return 0
    n, k = len(arr), 1
    for i in range(1, n):
        if arr[k-1] != arr[i]:
            arr[k] = arr[i]
            k += 1
    return k

class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return dedup(nums)
