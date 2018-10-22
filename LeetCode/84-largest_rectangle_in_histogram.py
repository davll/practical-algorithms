# Largest Rectangle in Histogram
# https://leetcode.com/problems/largest-rectangle-in-histogram
# https://www.geeksforgeeks.org/largest-rectangle-under-histogram/

def largest_rect_in_histogram(heights):
    n = len(heights)
    stack, result = [], 0
    for i in range(n):
        # hr, ir => the height and position of the right side
        # il => the position of the left side so that stack[:][0] < height[il]
        hr, ir, il = heights[i], i, i
        # maintain invariant
        while stack and stack[-1][0] >= hr:
            # compute the area of rectangle:
            #           __
            #         __
            #       __
            #    ___.......
            #    |hl      |
            #    |        |__
            #    |  here! |hr
            #    |        |
            #=================
            #     il       ir
            hl, il = stack.pop()
            area = hl * (ir - il)
            result = max(result, area)
        # push the current height to the stack
        #    __
        #    hl
        #    __.......__
        #  __hr       hr
        #
        #  ===============
        #    il       ir
        stack.append((hr, il))
    # clean the stack to compute rectangles as if hr = 0 at ir = n
    for h, i in stack:
        area = h * (n - i)
        result = max(result, area)
    return result

class Solution:
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        if not heights:
            return 0
        return largest_rect_in_histogram(heights)
