def three_sum_closest_v1(nums, target):
    n = len(nums)
    result = float('inf')
    psum = set()
    for i in range(n):
        for x in map(lambda x: x + nums[i], psum):
            if abs(target - x) < abs(target - result):
                result = x
        for j in range(i):
            psum.add(nums[i] + nums[j])
    return result

def three_sum_closest_v2(nums, target):
    # suppose nums is sorted
    n = len(nums)
    result = float('inf')
    for i in range(n-2):
        dist = nums[i] + two_sum_closest_v1(nums[i+1:], target-nums[i]) - target
        if abs(dist) < abs(result):
            result = dist
    return result + target

def two_sum_closest_v1(nums, target):
    # suppose nums is sorted
    n = len(nums)
    l, r = 0, n-1
    result = float('inf')
    while l < r:
        dist = nums[l] + nums[r] - target
        if abs(dist) < abs(result):
            result = dist
        if nums[l] + nums[r] == target:
            return target
        elif nums[l] + nums[r] < target:
            l += 1
        else: # nums[l] + nums[r] > target:
            r -= 1
    return result + target

class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        return three_sum_closest_v2(nums, target)
