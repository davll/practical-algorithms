def solve_nqueens(n):
    horiz = [True] * n
    diag0 = [True] * (2*n-1)
    diag1 = [True] * (2*n-1)
    pos = [-1] * n
    def idx_of_horiz(i, j):
        return i
    def idx_of_diag0(i, j):
        return (i-j+n-1)
    def idx_of_diag1(i, j):
        return (i+j)
    def backtrack(j):
        if j < n:
            count = 0
            for i in range(n):
                h = idx_of_horiz(i, j)
                d0 = idx_of_diag0(i, j)
                d1 = idx_of_diag1(i, j)
                if horiz[h] and diag0[d0] and diag1[d1]:
                    horiz[h] = diag0[d0] = diag1[d1] = False
                    pos[j] = i
                    count += backtrack(j+1)
                    horiz[h] = diag0[d0] = diag1[d1] = True
            return count
        else:
            return 1
    return backtrack(0)

class Solution:
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        return solve_nqueens(n)
