def backtrack(nums, i, buffer):
    if i == len(nums):
        yield buffer[:]
        return
    n = 1
    while i+n < len(nums) and nums[i+n] == nums[i]:
        n += 1
    yield from backtrack(nums, i+n, buffer)
    oldsiz = len(buffer)
    for _ in range(n):
        buffer.append(nums[i])
        yield from backtrack(nums, i+n, buffer)
    del buffer[oldsiz:]

class Solution:
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        return list(backtrack(nums, 0, []))
