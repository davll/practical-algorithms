# Based on Problem #256 - Paint House
#
#
#
#

def mincost_v2(costs):
    if not costs:
        return 0
    n, k = len(costs), len(costs[0])
    F1, F2 = [[0] * k for _ in range(2)]
    F1[:] = costs[0][:]
    for i in range(1,n):
        for j in range(k):
            F2[j] = min(F1[l] for l in range(k) if l != j) + costs[i][j]
        F1, F2 = F2, F1
    return min(F1)

def mincost_v3(costs):
    # TODO: O(nk) runtime
    pass

class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
        return mincost_v2(costs)
