# https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/

def dedup2(nums):
    if not nums:
        return 0
    n, k = len(nums), 2
    if n == 1:
        return 1
    for i in range(2, n):
        if nums[k-2] == nums[k-1] and nums[k-1] == nums[i]:
            continue
        nums[k] = nums[i]
        k += 1
    return k

class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return dedup2(nums)
