def rotate_array(nums, k):
    if not nums:
        return
    n = len(nums)
    k = k % n
    reverse(nums, n-k, n-1)
    reverse(nums, 0, n-k-1)
    reverse(nums, 0, n-1)

def reverse(nums, l, r):
    while l < r:
        nums[l], nums[r] = nums[r], nums[l]
        l, r = l+1, r-1

class Solution:
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        return rotate_array(nums, k)
