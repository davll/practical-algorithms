# https://www.hackerrank.com/challenges/abbr/problem
#
# Abbreviation
#
# State Transition:
#
# f[i,j]: whether it is possible to make A[:i] into B[:j]
#
# f[i,j] = f[i-1,j-1] or f[i-1,j]       if A[i-1].upper = B[j-1]
#          f[i-1,j]                     if A[i-1] is lowercase
#          True                         if j == 0 and i == 0
#          False                        if i == 0 and j > 0
#

def abbrev(A: str, B: str):
    m, n = len(A), len(B)
    dp = [[False] * (n+1) for _ in range(m+1)]
    dp[0][0] = True
    for i in range(1,m+1):
        if A[i-1].islower():
            dp[i][0] = dp[i-1][0]
    for j in range(1,n+1):
        for i in range(1,m+1):
            if A[i-1].islower():
                dp[i][j] = dp[i][j] or dp[i-1][j]
            if A[i-1].upper() == B[j-1]:
                dp[i][j] = dp[i][j] or dp[i-1][j-1]
    return dp[m][n]

if __name__ == "__main__":
    for _ in range(int(input().rstrip())):
        A = input().rstrip()
        B = input().rstrip()
        ans = abbrev(A, B)
        if ans:
            print("YES")
        else:
            print("NO")
