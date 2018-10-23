# Perfect Squares
#
# Hint: Coin Change Problem
#

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
    return dp

# 1) Lagrange's Four Square theorem
# 2) Legendre's three square theorem
def compute_v2(n):
    ns = int(floor(sqrt(n)))
    # n is a perfect square
    if ns * ns == n:
        return 1
    # four square thm
    while n % 4 == 0:
        n //= 4
    if n % 8 == 7:
        return 4
    # check 2
    ns = int(floor(sqrt(n)))
    for i in range(1,ns+1):
        x = n - i*i
        xs = int(floor(sqrt(x)))
        if xs*xs == x:
            return 2
    #
    return 3

class Solution:
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        return compute_v2(n)
