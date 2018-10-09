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
    dp = [[0] * (n+1) for _ in range(m+1)]
    for i in range(m+1):
        for j in range(n+1):
            if i == 0:
                dp[i][j] = j
            elif j == 0:
                dp[i][j] = i
            elif s1[i-1] == s2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = min(
                    dp[i][j-1] + 1,
                    dp[i-1][j] + 1,
                    dp[i-1][j-1] + 1
                )
    return dp[m][n]
