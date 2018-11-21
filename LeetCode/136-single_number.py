# https://leetcode.com/problems/single-number/description/

from collections import Counter

def find_single_number_v1(nums):
    count = Counter(nums)
    return [x for x, n in count.items() if n == 1][0]

# Idea: Bit Manipulation
#
# a xor 0 = a
# a xor a = 0
# a xor b xor a = (a xor a) xor b = 0 xor b = b
#
def find_single_number_v2(nums):
    ans = 0
    for x in nums:
        ans = ans ^ x
    return ans

class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return find_single_number_v2(nums)
