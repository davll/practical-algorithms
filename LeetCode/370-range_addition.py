# https://leetcode.com/problems/range-addition/

def range_add_v1(n, updates):
    nums = [0] * n
    for i, j, x in updates:
        for k in range(i, j+1):
            nums[k] += x
    return nums

def range_add_v2(n, updates):
    nums = [0] * n
    for i, j, x in updates:
        nums[i] += x
        if j+1 < n:
            nums[j+1] -= x
    for i in range(1,n):
        nums[i] += nums[i-1]
    return nums

class Solution:
    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:
        return range_add_v2(length, updates)
