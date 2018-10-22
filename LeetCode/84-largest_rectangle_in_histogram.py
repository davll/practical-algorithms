# Largest Rectangle in Histogram
#
#
#

class Solution:
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        n = len(heights)
        stack = [(heights[0], 0)]
        result = 0
        for i in range(1, n):
            pass
