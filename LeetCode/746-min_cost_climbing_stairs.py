# https://leetcode.com/problems/min-cost-climbing-stairs/

# Idea: Dynamic Programming
#
# f[i]: minimum cost to reach i-th step
#
# f[0] = costs[0]
# f[1] = costs[1]
# f[i] = min {
#            f[i-1] + costs[i],
#            f[i-2] + costs[i]
#        }
#
def climbing_stairs(costs):
    n = len(costs)
    dp = [0] * (n+1)
    dp[:2] = costs[:2]
    costs.append(0)
    for i in range(2, n+1):
        dp[i] = costs[i] + min(dp[i-1], dp[i-2])
    return dp[n]

class Solution(object):
    def minCostClimbingStairs(self, costs):
        """
        :type cost: List[int]
        :rtype: int
        """
        return climbing_stairs(costs)
