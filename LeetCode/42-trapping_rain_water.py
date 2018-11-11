# https://leetcode.com/problems/trapping-rain-water/description/

# Idea: Dynamic Programming
# T = O(n)
def trap_water_v2(heights):
    n = len(heights)
    left = [0] * n
    right = [n-1] * n
    # compute left barriers
    curr_left = 0
    for i in range(1, n):
        if heights[i] >= heights[curr_left]:
            curr_left = i
        left[i] = curr_left
    # compute right barriers
    curr_right = n-1
    for i in range(n-2,-1,-1):
        if heights[i] >= heights[curr_right]:
            curr_right = i
        right[i] = curr_right
    #
    result = 0
    for i in range(n):
        h = min(heights[left[i]], heights[right[i]])
        result += max(0, h - heights[i])
    return result

# Idea: BFS
def trap_water_v3(heights):
    from heapq import heappush, heappop, heapify
    #
    n = len(heights)
    heap = []
    visited = [False] * n
    # visit borders
    for i in (0, n-1):
        if i not in range(n):
            continue
        heap.append((heights[i], i))
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
                heappush(heap, (heights[ni], ni))
                visited[ni] = True
    return water

# Idea: Stack
def trap_water_v4(heights):
    n = len(heights)
    result = 0
    stack = []
    for i in range(n):
        while stack and heights[stack[-1]] <= heights[i]:
            t = stack.pop()
            if not stack:
                break
            w = i - stack[-1] - 1
            h = min(heights[i], heights[stack[-1]]) - heights[t]
            result += w * h
        stack.append(i)
    return result

# Idea: 2 Pointers
def trap_water_v5(heights):
    n = len(heights)
    l, r = 0, n-1
    lmax, rmax = 0, 0
    result = 0
    while l < r:
        if heights[l] < heights[r]:
            result += max(0, lmax - heights[l])
            lmax = max(lmax, heights[l])
            l += 1
        else:
            result += max(0, rmax - heights[r])
            rmax = max(rmax, heights[r])
            r -= 1
    return result

class Solution:
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        return trap_water_v5(height)
