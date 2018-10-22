# Maximal Rectangle
#
# => Hint: Largest rectangle in Histogram
#

class Solution:
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix or not matrix[0]:
            return 0
        m, n = len(matrix), len(matrix[0])
        heights = [list(map(int, matrix[i])) for i in range(m)]
        for i in range(1, m):
            for j in range(n):
                if heights[i][j] != 0:
                    heights[i][j] += heights[i-1][j]
        return max(map(lambda h: largest_rect_in_histogram(h), heights))

def largest_rect_in_histogram(heights):
    n = len(heights)
    stack, result = [], 0
    for i in range(n):
        hr, ir, il = heights[i], i, i
        while stack and stack[-1][0] >= hr:
            hl, il = stack.pop()
            area = hl * (ir - il)
            result = max(result, area)
        stack.append((hr, il))
    for h, i in stack:
        area = h * (n - i)
        result = max(result, area)
    return result
