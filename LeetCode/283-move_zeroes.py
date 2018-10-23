class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        #m = sum(map(lambda x: 1 if x == 0 else 0, nums))
        k = 0
        for i in range(n):
            if nums[i] != 0:
                nums[k] = nums[i]
                k += 1
        for i in range(k, n):
            nums[i] = 0
