# https://leetcode.com/problems/single-number-ii/description/
# https://leetcode.com/problems/single-number-ii/discuss/167343/topic
# https://leetcode.com/problems/single-number-ii/discuss/43297/Java-O(n)-easy-to-understand-solution-easily-extended-to-any-times-of-occurance

def find_single_number_v2(nums):
    a, b = 0, 0
    for x in nums:
        b = b ^ x & ~a
        a = a ^ x & ~b
    return a | b

class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return find_single_number_v2(nums)
