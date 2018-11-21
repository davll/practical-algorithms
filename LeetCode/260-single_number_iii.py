# https://leetcode.com/problems/single-number-iii/description/
# https://leetcode.com/problems/single-number-iii/discuss/68900/Accepted-C++Java-O(n)-time-O(1)-space-Easy-Solution-with-Detail-Explanations

def find_single_numbers(nums):
    mask = 0
    for x in nums:
        mask = mask ^ x
    lsb = (mask & (-mask))
    a, b = 0, 0
    for x in nums:
        if (x & lsb) == 0:
            a ^= x
        else:
            b ^= x
    return [a, b]

class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        return find_single_numbers(nums)
