def solve_sudoku(board):
    rows = [[False] * 9 for _ in range(9)]
    cols = [[False] * 9 for _ in range(9)]
    subs = [[False] * 9 for _ in range(9)]
    cells = [
        (i, j)
        for i in range(9)
            for j in range(9)
                if board[i][j] == '.'
    ]
    for i in range(9):
        for j in range(9):
            if board[i][j] == '.':
                continue
            x = ord(board[i][j]) - ord('1')
            rows[i][x] = True
            cols[j][x] = True
            subs[(i//3)*3+(j//3)][x] = True
    def backtrack(cellidx):
        if cellidx < len(cells):
            i, j = cells[cellidx]
            for x in range(1, 10):
                if rows[i][x-1]:
                    continue
                if cols[j][x-1]:
                    continue
                if subs[(i//3)*3+(j//3)][x-1]:
                    continue
                rows[i][x-1] = True
                cols[j][x-1] = True
                subs[(i//3)*3+(j//3)][x-1] = True
                board[i][j] = format(x + ord('0'), 'c')
                if backtrack(cellidx + 1):
                    return True
                board[i][j] = '.'
                rows[i][x-1] = False
                cols[j][x-1] = False
                subs[(i//3)*3+(j//3)][x-1] = False
            return False
        else:
            return True
    backtrack(0)

class Solution:
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        solve_sudoku(board)
