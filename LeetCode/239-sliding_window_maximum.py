from collections import deque

# Hint: Amortized O(n)

def max_sliding_window_v0(nums, k):
    if not nums or k == 0:
        return []
    queue = deque(nums[:k])
    result = [max(queue)]
    for i in range(k, len(nums)):
        x = queue.popleft()
        queue.append(nums[i])
        result.append(max(queue))
    return result

def max_sliding_window_v1(nums, k):
    queue = deque() # store indices instead of values
    result = []
    for i in range(len(nums)):
        # drain overflow indices
        while queue and queue[0] <= i-k:
            queue.popleft()
        # remove unlikely maximals
        while queue and nums[queue[-1]] <= nums[i]:
            queue.pop()
        # push current index
        queue.append(i)
        # emit current maximal value
        if i >= k-1:
            result.append(nums[queue[0]])
    return result

class Solution:
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        return max_sliding_window_v1(nums, k)
