# https://leetcode.com/problems/trapping-rain-water/description/

# Idea: Dynamic Programming
# T = O(n)
def trap_water_v2(height):
    n = len(height)
    left = [0] * n
    right = [n-1] * n
    # compute left barriers
    curr_left = 0
    for i in range(1, n):
        if height[i] >= height[curr_left]:
            curr_left = i
        left[i] = curr_left
    # compute right barriers
    curr_right = n-1
    for i in range(n-2,-1,-1):
        if height[i] >= height[curr_right]:
            curr_right = i
        right[i] = curr_right
    #
    result = 0
    for i in range(n):
        h = min(height[left[i]], height[right[i]])
        result += max(0, h - height[i])
    return result

# Idea: BFS
def trap_water_v3(height):
    from heapq import heappush, heappop, heapify
    #
    n = len(height)
    heap = []
    visited = [False] * n
    # visit borders
    for i in (0, n-1):
        if i not in range(n):
            continue
        heap.append((height[i], i))
        visited[i] = True
    heapify(heap)
    # visit cells
    max_height = 0
    water = 0
    while heap:
        h, i = heappop(heap)
        if h > max_height:
            max_height = h
        else:
            water += max_height - h
        for ni in (i-1, i+1):
            if ni not in range(n):
                continue
            if not visited[ni]:
                heappush(heap, (height[ni], ni))
                visited[ni] = True
    return water

class Solution:
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        return trap_water_v3(height)
