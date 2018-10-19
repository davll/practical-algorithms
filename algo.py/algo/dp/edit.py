# Edit Distance
#
# Given two strings s1 and s2 and below operations that can performed on s1.
# Find minimum number of edits (operations) required to convert s1 into s2.
#
# Operations:
# - Insert
# - Remove
# - Replace
#
# All of the above operations are of equal cost.
#
# f[i,j] = minimum number of edits required to convert s1[:i] into s2[:j]
#
# f[i,j] = 0                        if i = 0 and j = 0
#        = j (insert)               if i = 0 and j > 0
#        = i (remove)               if i > 0 and j = 0
#        = f[i-1,j-1] (no-op)       if s1[i-1] = s2[j-1] 
#        = min {
#              f[i,j-1] + 1 (insert)
#              f[i-1,j] + 1 (remove)
#              f[i-1,j-1] + 1 (replace)
#          }                        otherwise
#

def edit_distance(s1, s2):
    m, n = len(s1), len(s2)
    #dp1 = [0] * (n+1)
    #dp2 = [0] * (n+1)
    dp = [[0] * (n+1) for _ in range(m+1)]
    for j in range(n+1):
        dp[0][j] = j
    for i in range(1, m+1):
        dp[i][0] = i
        for j in range(1, n+1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = min(
                    dp[i][j-1] + 1,
                    dp[i-1][j] + 1,
                    dp[i-1][j-1] + 1
                )
    return dp[m][n]
