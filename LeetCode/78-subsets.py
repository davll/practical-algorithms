def backtrack(nums, i, buffer):
    if i < len(nums):
        # not include this
        yield from backtrack(nums, i+1, buffer)
        # include this
        buffer.append(nums[i])
        yield from backtrack(nums, i+1, buffer)
        buffer.pop()
    else:
        yield buffer[:]

class Solution:
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        return list(backtrack(nums, 0, []))
