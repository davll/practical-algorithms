# Perfect Squares
#
# Hint: Coin Changes

from math import sqrt, floor

def coins(x):
    y = 1
    while y*y <= x:
        yield y*y
        y += 1

def compute_v1(n):
    dp = [0] * (n+1)
    dp[:2] = [0, 1]
    for x in range(2, n+1):
        dp[x] = min(map(lambda c: dp[x-c]+1, coins(x)))
    return dp[n]

class Solution:
    def numSquares(self, n: int) -> int:
        m = int(sqrt(n))
        if m ** 2 == n:
            return 1
        return compute_v1(n)
