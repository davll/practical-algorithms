# https://leetcode.com/problems/trapping-rain-water-ii/description/

class Solution:
    def trapRainWater(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: int
        """
        m, n = len(heights), len(heights[0])
        upper = [[0] * n for _ in range(m)]
        lower = [[n-1] * n for _ in range(m)]
        left = [[0] * n for _ in range(m)]
        right = [[n-1] * n for _ in range(m)]
        
