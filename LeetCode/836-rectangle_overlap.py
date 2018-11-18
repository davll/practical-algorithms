# https://leetcode.com/problems/rectangle-overlap/

class Solution(object):
    def isRectangleOverlap(self, rec1, rec2):
        """
        :type rec1: List[int]
        :type rec2: List[int]
        :rtype: bool
        """
        # rect = x1, y1, x2, y2
        ax1, ay1, ax2, ay2 = rec1
        bx1, by1, bx2, by2 = rec2
        return intersect_1d(ax1, ax2, bx1, bx2) and intersect_1d(ay1, ay2, by1, by2)

def intersect_1d(ax1, ax2, bx1, bx2):
    return bx2 > ax1 and ax2 > bx1
