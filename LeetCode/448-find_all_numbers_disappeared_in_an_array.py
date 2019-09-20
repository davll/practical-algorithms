#

from collections import Counter

def find_disappeared_v1(nums):
    counter = Counter(nums)
    return [x for x in range(1,len(nums)+1) if x not in counter]

def find_disappeared_v2(nums):
    n = len(nums)
    missing = list(range(1,n+1))
    for x in nums:
        missing[x-1] = -1
    l, r = 0, 0
    while r < n:
        if missing[r] != -1:
            missing[l] = missing[r]
            l += 1
        r += 1
    return missing[:l]

def find_disappeared_v3(nums):
    n = len(nums)
    for i in range(n):
        x = abs(nums[i])
        nums[x-1] = -abs(nums[x-1])
    return [i+1 for i in range(n) if nums[i] > 0]

def find_disappeared_v4(nums):
    pass

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        return find_disappeared_v3(nums)
