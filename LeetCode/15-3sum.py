# https://leetcode.com/problems/3sum/

from collections import Counter

def threesum_v2(nums):
    lut = {}
    results = set()
    for i, x in enumerate(nums):
        for y, z in lut.get(-x, []):
            results.add(tuple(sorted((x, y, z))))
        for j, y in enumerate(nums[:i]):
            s = lut.get(x+y, set())
            s.add((nums[i], nums[j]))
            lut[x+y] = s
    return list(results)

def threesum_v3(nums):
    nums.sort()
    lut = Counter()
    for x in nums:
        lut[x] += 1
    a, b = set(), set()
    for x in nums:
        lut[x] -= 1
        for y in a:
            if lut[-(x+y)] > 0:
                b.add((y, x, -(x+y)))
        a.add(x)
    return list(b)

def threesum_v4(nums, target):
    n = len(nums)
    nums.sort()
    result = []
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
                result.append((nums[i], nums[l], nums[r]))
                while l < r and nums[l] == nums[l+1]:
                    l += 1
                while l < r and nums[r] == nums[r-1]:
                    r -= 1
                l, r = l+1, r-1
    return result

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        return threesum_v4(nums, 0)
