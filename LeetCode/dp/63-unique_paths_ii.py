class Solution:
    def uniquePathsWithObstacles(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        grid[i,j] = 1 or 0 (obstacle or empty space)
        dp[i,j] = how many unique paths to the location (i,j)
        """
        if not grid or not grid[0]:
            return 0
        m, n = len(grid), len(grid[0])
        dp = [[0] * n for _ in range(m)]
        # the origin
        if grid[0][0] == 0:
            dp[0][0] = 1
        else:
            dp[0][0] = 0
        # the 1st row
        for j in range(1, n):
            if grid[0][j] == 0:
                dp[0][j] = dp[0][j-1]
            else:
                dp[0][j] = 0
        # the 1st column
        for i in range(1, m):
            if grid[i][0] == 0:
                dp[i][0] = dp[i-1][0]
            else:
                dp[i][0] = 0
        # the others
        for i in range(1, m):
            for j in range(1, n):
                if grid[i][j] == 0:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
                else:
                    dp[i][j] = 0
        return dp[m-1][n-1]

