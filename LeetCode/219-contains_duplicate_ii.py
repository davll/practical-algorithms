#
#
#

# TLE
def hasdup_v1(nums, k):
    n = len(nums)
    for d in range(1,k+1):
        for i, x in enumerate(nums):
            if i + d >= n:
                break
            if nums[i+d] == x:
                return True
    return False

def hasdup_v2(nums, k):
    table = dict()
    for i, x in enumerate(nums):
        if x in table:
            if i - table[x] <= k:
                return True
        table[x] = i
    return False

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        return hasdup_v2(nums, k)
