# https://leetcode.com/problems/pour-water/

class Solution(object):
    def pourWater(self, heights, V, K):
        """
        :type heights: List[int]
        :type V: int
        :type K: int
        :rtype: List[int]
        """
        n = len(heights)
        for _ in range(V):
            pos = K
            # move left
            for l in range(K-1, -1, -1):
                if heights[l] < heights[pos]:
                    pos = l
                elif heights[l] > heights[pos]:
                    break
            # move right
            if pos == K:
                for r in range(K+1, n):
                    if heights[r] < heights[pos]:
                        pos = r
                    elif heights[r] > heights[pos]:
                        break
            heights[pos] += 1
        return heights
