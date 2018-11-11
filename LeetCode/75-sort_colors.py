# https://leetcode.com/problems/sort-colors/

def sort_colours_v1(nums):
    count = [0] * 3
    for x in nums:
        count[x] += 1
    print("count = " + str(count))
    start = 0
    for k in range(3):
        for i in range(count[k]):
            nums[i+start] = k
        start += count[k]

def sort_colours_v2(nums):
    n = len(nums)
    if n < 2:
        return
    i, tail0, head2 = 0, 0, n-1
    while i <= head2:
        if nums[i] == 0:
            nums[i], nums[tail0] = nums[tail0], 0
            tail0 += 1
            i += 1
        elif nums[i] == 2:
            nums[i], nums[head2] = nums[head2], 2
            head2 -= 1
        else:
            i += 1

class Solution:
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        sort_colours_v2(nums)
