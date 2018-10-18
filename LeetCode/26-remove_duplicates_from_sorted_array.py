def dedup(arr):
    if not arr:
        return 0
    n, k = len(arr), 0
    for i in range(1, n):
        if arr[k] != arr[i]:
            k += 1
            arr[k] = arr[i]
    return k+1

class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return dedup(nums)
