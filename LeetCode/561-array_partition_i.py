# https://leetcode.com/problems/array-partition-i/

from heapq import heapify, heappop

def part_pairs_v1(nums):
    heapify(nums)
    result = 0
    while nums:
        result += min(heappop(nums), heappop(nums))
    return result

class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        return part_pairs_v1(nums)
