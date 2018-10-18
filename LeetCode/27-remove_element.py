def remove_elements(arr, key):
    n, k = len(arr), 0
    for i in range(n):
        if arr[i] != key:
            arr[k] = arr[i]
            k += 1
    return k

class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        return remove_elements(nums, val)
