# Maximal Rectangle
#
# => Strategy: Dynamic Programming
#
# suppose the area [0:i+1][0:j+1] has a maximal rectangle where
#   1) the bottom-right corner of the maximal rectangle is at (i,j)
#   2) the area of the maximal rectangle = width[i,j] * height[i,j]
#
# width[i,j] =  0                                       if grid[i,j] = 0
#               1                                       if i == 0 and j == 0
#               min(width[i,j-1] + 1, width[i-1,j])
#
# height[i,j] = 0                                       if grid[i,j] = 0
#               1                                       if i == 0 and j == 0
#               min(height[i,j-1], height[i-1,j] + 1)
#

class Solution:
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        m, n = len(matrix), len(matrix[0])
        horizon = [[0] * n for _ in range(m)]
        vertical = [[0] * n for _ in range(m)]
        if matrix[0][0] == '1':
            horizon[0][0] = 1
            vertical[0][0] = 1
        for i in range(m):
            if matrix[i][0] == '1':
                horizon[i][0] = 1
            for j in range(1,n):
                if matrix[i][j] == '1':
                    horizon[i][j] = horizon[i][j-1] + 1
        for j in range(n):
            if matrix[0][j] == '1':
                vertical[0][j] = 1
            for i in range(1,m):
                if matrix[i][j] == '1':
                    vertical[i][j] = vertical[i-1][j] + 1
        print('Horizon')
        print('\n'.join(map(str, horizon)))
        print('Vertical')
        print('\n'.join(map(str, vertical)))

if __name__ == "__main__":
    s = Solution()
    mat = [
        "10100",
        "10111",
        "11111",
        "10011"
    ]
    ans = s.maximalRectangle(mat)
    print(str(ans))
