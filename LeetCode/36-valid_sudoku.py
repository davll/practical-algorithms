def valid_sudoku(board):
    # check rows
    for i in range(9):
        show = [False] * 9
        for j in range(9):
            if board[i][j] == '.':
                continue
            x = ord(board[i][j]) - ord('1')
            if show[x]:
                return False
            show[x] = True
    # check columns
    for j in range(9):
        show = [False] * 9
        for i in range(9):
            if board[i][j] == '.':
                continue
            x = ord(board[i][j]) - ord('1')
            if show[x]:
                return False
            show[x] = True
    # check 3x3 subsets
    for i0 in range(0, 9, 3):
        for j0 in range(0, 9, 3):
            show = [False] * 9
            for i in range(i0, i0+3):
                for j in range(j0, j0+3):
                    if board[i][j] == '.':
                        continue
                    x = ord(board[i][j]) - ord('1')
                    if show[x]:
                        return False
                    show[x] = True
    return True

class Solution:
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        return valid_sudoku(board)
