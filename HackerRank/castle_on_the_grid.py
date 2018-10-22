# https://www.hackerrank.com/challenges/castle-on-the-grid/problem

from sys import stdin, stdout, stderr
from collections import deque

def minimumMoves(n, grid, startx, starty, goalx, goaly):
    moves = [[-1] * n for _ in range(n)]
    # do BFS
    queue = deque([(startx, starty)])
    moves[startx][starty] = 0
    def push(x, y, m) -> bool:
        if grid[x][y] == 'X':
            return False
        if moves[x][y] == -1:
            moves[x][y] = m
            queue.append((x, y))
        return True
    while len(queue) > 0:
        posx, posy = queue.popleft()
        assert grid[posx][posy] != 'X'
        assert moves[posx][posy] != -1
        if posx == goalx and posy == goaly:
            break
        m = moves[posx][posy]
        # +x direction
        for i in range(posx+1, n):
            if not push(i, posy, m+1):
                break
        # -x direction
        for i in range(posx-1, -1, -1):
            if not push(i, posy, m+1):
                break
        # +y direction
        for j in range(posy+1, n):
            if not push(posx, j, m+1):
                break
        # -y direction
        for j in range(posy-1, -1, -1):
            if not push(posx, j, m+1):
                break
    return moves[goalx][goaly]

if __name__ == "__main__":
    n = int(stdin.readline().rstrip())
    grid = [
        list(map(lambda x: x.upper(), stdin.readline().rstrip()))
        for _ in range(n)
    ]
    startx, starty, goalx, goaly = map(int, stdin.readline().rstrip().split())
    ans = minimumMoves(n, grid, startx, starty, goalx, goaly)
    stdout.write(str(ans) + '\n')
