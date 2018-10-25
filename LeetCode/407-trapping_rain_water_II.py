# https://leetcode.com/problems/trapping-rain-water-ii/description/

# Hint: BFS

def trap_water_v1(heights):
    from heapq import heapify, heappush, heappop
    #
    m, n = len(heights), len(heights[0])
    heap = []
    visited = [[False] * n for _ in range(m)]
    

class Solution:
    def trapRainWater(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: int
        """
        return trap_water_v1(heights)
