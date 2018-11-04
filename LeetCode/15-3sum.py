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

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        return threesum_v3(nums)
