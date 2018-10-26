# https://leetcode.com/problems/find-the-duplicate-number/description/

# Idea: Binary Search
# Idea: The pigeonhole principle
#
def find_duplicate_v1(nums):
    n = len(nums)-1
    l, r = 1, n
    while l < r:
        m = (l + r) // 2
        # find the number of numbers that are less than or equal to m
        count = sum(map(lambda x: int(x <= m), nums))
        # if count > m
        #   => according to the pigeonhole principle
        #   => there must be a duplicate number x where 1 <= x <= m
        # otherwise
        #   => x must be greater than m
        if count > m:
            r = m
        else:
            l = m+1
    return l

# Idea: Detect Cycle
#
# Similar Problems:
#   - 142 Linked List Cycle II
#
def find_duplicate_v2(nums):
    slow, fast = nums[0], nums[nums[0]]
    while slow != fast:
        fast = nums[nums[fast]]
        slow = nums[slow]
    fast = 0
    while slow != fast:
        fast = nums[fast]
        slow = nums[slow]
    return fast

class Solution:
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return find_duplicate_v2(nums)
