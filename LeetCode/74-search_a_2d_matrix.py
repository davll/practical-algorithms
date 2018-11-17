# https://leetcode.com/problems/search-a-2d-matrix/

# t, b, l, r = top, bottom, left, right
def binary_search_2d_v1(mat, t, b, l, r, target):
    l0, r0 = l, r
    while t <= b:
        mr = (t + b) // 2
        if mat[mr][0] > target:
            b = mr-1
        elif mat[mr][-1] < target:
            t = mr+1
        else:
            l, r = l0, r0
            while l <= r:
                m = (l + r) // 2
                if mat[mr][m] == target:
                    return True
                elif mat[mr][m] < target:
                    l = m+1
                else:
                    r = m-1
            return False
    return False

class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not matrix[0]:
            return False
        m, n = len(matrix), len(matrix[0])
        return binary_search_2d_v1(matrix, 0, m-1, 0, n-1, target)
