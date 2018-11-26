# https://leetcode.com/problems/longest-consecutive-sequence/
# https://leetcode.com/problems/longest-consecutive-sequence/discuss/41055/My-really-simple-Java-O(n)-solution-Accepted
# https://leetcode.com/problems/longest-consecutive-sequence/discuss/197781/UnionFind-Solution-easy-understanding-(Java)
# https://leetcode.com/problems/longest-consecutive-sequence/discuss/197792/Python-solution-easy-to-understand

def lcss_v0(nums):
    result = 0
    for x in nums:
        curr = x
        size = 1
        while curr+1 in nums:
            curr += 1
            size += 1
        result = max(size, result)
    return result

def lcss_v1(nums):
    if not nums:
        return 0
    nums.sort()
    result = 1
    curlen = 1
    n = 1
    for i in range(1, len(nums)):
        if nums[n-1] != nums[i]:
            nums[n] = nums[i]
            n += 1
    for i in range(1, n):
        if nums[i-1] + 1 == nums[i] or nums[i-1] == nums[i]:
            curlen += 1
        else:
            curlen = 1
        result = max(curlen, result)
    return result

# HashSet
def lcss_v2(nums):
    raise NotImplementedError()

# Union Find
def lcss_v3(nums):
    raise NotImplementedError()

class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return lcss_v0(nums)
