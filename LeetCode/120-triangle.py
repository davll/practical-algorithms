class Solution:
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        n = len(triangle)
        tmp = triangle[-1][:]
        for i in range(n-2, -1, -1):
            for j in range(i+1):
                tmp[j] = min(tmp[j], tmp[j+1]) + triangle[i][j]
        return tmp[0]
