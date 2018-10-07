# https://www.hackerrank.com/challenges/sherlock-and-cost/problem
#
# S(N) = sum(map(lambda i: abs(A[i] - A[i-1]), range(1, N)))
#
# f(n, x) = max { f(n-1, y) + abs(x - y) for all y }
#          where
#              1 <= x <= B[n-1]
#              1 <= y <= B[n-2]
#
# f(1, x) = 0 where 1 <= x <= B[0]
#

from sys import stdin, stdout, stderr

def cost1(B):
    n = len(B)
    dp1 = [0] * 101
    dp2 = [0] * 101
    for i in range(1,n):
        for x in range(1, B[i]+1):
            dp2[x] = max(map(lambda y: dp1[y]+abs(x-y), range(1, B[i-1]+1)))
        dp1, dp2 = dp2, dp1
    return max(dp1)

def cost2(B):
    n = len(B)
    L, H = 0, 0
    for i in range(1,n):
        L2 = max(L, H + abs(1 - B[i-1]))
        H2 = max(L + abs(B[i] - 1), H + abs(B[i] - B[i-1]))
        L, H = L2, H2
    return max(L, H)

if __name__ == "__main__":
    for _ in range(int(stdin.readline().rstrip())):
        n = int(stdin.readline().rstrip())
        B = list(map(int, stdin.readline().rstrip().split()))
        ans = cost2(B)
        stdout.write(str(ans) + '\n')
