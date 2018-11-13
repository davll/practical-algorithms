class Solution:
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        m = len(matrix)
        if m == 0:
            return []
        n = len(matrix[0])
        return list(spiral_order(matrix, m, n))

def spiral_order(matrix, m, n):
    row0, row1, col0, col1 = 0, m-1, 0, n-1
    while row0 <= row1 and col0 <= col1:
        yield from get_row(matrix, row0, col0, col1)
        row0 += 1
        if row0 > row1: break
        yield from get_col(matrix, row0, row1, col1)
        col1 -= 1
        if col0 > col1: break
        yield from get_row(matrix, row1, col0, col1, rev=True)
        row1 -= 1
        if row0 > row1: break
        yield from get_col(matrix, row0, row1, col0, rev=True)
        col0 += 1
        if col0 > col1: break

def get_row(matrix, i, j0, j1, rev = False):
    nums = range(j0, j1+1)
    if rev:
        nums = reversed(nums)
    for j in nums:
        yield matrix[i][j]

def get_col(matrix, i0, i1, j, rev = False):
    nums = range(i0, i1+1)
    if rev:
        nums = reversed(nums)
    for i in nums:
        yield matrix[i][j]
