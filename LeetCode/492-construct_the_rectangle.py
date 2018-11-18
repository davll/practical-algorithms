# https://leetcode.com/problems/construct-the-rectangle/

from math import sqrt, floor

class Solution(object):
    def constructRectangle(self, area):
        """
        :type area: int
        :rtype: List[int]
        """
        w = int(floor(sqrt(area)))
        while area % w != 0:
            w = w - 1
        return [area // w, w]
