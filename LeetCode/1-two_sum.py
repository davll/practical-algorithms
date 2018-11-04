def two_sum_v1(nums, target):
    lut = {}
    for i in range(len(nums)):
        if nums[i] in lut:
            return [lut[nums[i]], i]
        else:
            lut[target - nums[i]] = i

def two_sum_v2(nums, target):
    n = len(nums)
    index = list(range(n))
    index.sort(key = lambda i: nums[i])
    l, r = 0, n-1
    while l < r:
        i, j = index[l], index[r]
        if nums[i] + nums[j] == target:
            return [i, j]
        elif nums[i] + nums[j] < target:
            l += 1
        else: # nums[i] + nums[j] > target
            r -= 1

class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        return two_sum_v2(nums, target)
