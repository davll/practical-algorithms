from sys import stderr

def maxRegion(n, m, grid):
    visited = [[False] * m for _ in range(n)]
    def _dfs(i, j):
        if i < 0 or i >= n or j < 0 or j >= m:
            return 0
        if visited[i][j] or grid[i][j] == 0:
            return 0
        print("Visited ({i}, {j})".format(i=i,j=j), file=stderr)
        visited[i][j] = True
        count = 1
        count += _dfs(i-1, j-1)
        count += _dfs(i-1, j)
        count += _dfs(i-1, j+1)
        count += _dfs(i, j-1)
        count += _dfs(i, j+1)
        count += _dfs(i+1, j-1)
        count += _dfs(i+1, j)
        count += _dfs(i+1, j+1)
        return count
    #
    ans = 0
    for i in range(m):
        for j in range(n):
            ans = max(ans, _dfs(i, j))
    return ans

if __name__ == "__main__":
    n = int(input())
    m = int(input())
    grid = [
        list(map(int, input().split()))
        for _ in range(n)
    ]
    ans = maxRegion(n, m, grid)
    print(str(ans))
