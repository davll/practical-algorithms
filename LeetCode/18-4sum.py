def four_sum_v1(nums, target):
    n = len(nums)
    nums.sort()
    results = []
    for i in range(n-3):
        if i > 0 and nums[i] == nums[i-1]:
            continue
        x = nums[i]
        for y, z, w in threesum_v4(nums[i+1:], target-x):
            results.append((x, y, z, w))
    return results

def threesum_v4(nums, target):
    n = len(nums)
    #nums.sort()
    for i in range(n-2):
        if i > 0 and nums[i] == nums[i-1]:
            continue
        l, r = i+1, n-1
        while l < r:
            s = nums[i] + nums[l] + nums[r]
            if s < target:
                l += 1
            elif s > target:
                r -= 1
            else: # s == target
                yield (nums[i], nums[l], nums[r])
                while l < r and nums[l] == nums[l+1]:
                    l += 1
                while l < r and nums[r] == nums[r-1]:
                    r -= 1
                l, r = l+1, r-1

class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        return four_sum_v1(nums, target)
