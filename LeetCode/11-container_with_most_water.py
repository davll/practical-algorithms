# https://leetcode.com/problems/container-with-most-water/
#
# Container with Most Water 
#
# Hint: Greedy Method
#
# Proof:
#   The first candidate is the pair (0, N-1)
#
#   Consider the pair (L, R)
#     => area = min(H[L], H[R]) * (R-L)
#     1) if H[L] < H[R] => (L, R') wont be better than (L,R) where R' < R
#        a) if H[L] > H[R-1] => H[R-1] * (R-L-1) => worse!
#        b) if H[L] < H[R-1] => H[L] * (R-L-1) => still worse!
#     2) if H[L] > H[R] => (L', R) wont be better than (L,R) where L' > L
#
#   https://leetcode.com/problems/container-with-most-water/discuss/6100/Simple-and-clear-proofexplanation
#   https://leetcode.com/problems/container-with-most-water/discuss/6099/yet-another-way-to-see-what-happens-in-the-on-algorithm
#

def largestContainer(heights):
    n = len(heights)
    l, r = 0, n-1
    result = 0
    while l < r:
        result = max(result, min(heights[l], heights[r]) * (r-l))
        if heights[l] < heights[r]:
            l += 1
        else:
            r -= 1
    return result

class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        return largestContainer(height)
