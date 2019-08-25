#
# F[n][c] : total cost of painting 1..n houses when the color of n-th is c
#         = C[0][c] when n = 1
#         = min {
#             F[n-1][c1] + C[n-1][c] for all c1 in { R,B,G } and c1 != c
#           }
#

def mincost_v1(costs):
    if not costs:
        return 0
    n = len(costs)
    F = [[0] * 3 for _ in range(n)]
    F[0][:] = costs[0][:]
    for i in range(1,n):
        F[i][0] = min(F[i-1][1], F[i-1][2]) + costs[i][0]
        F[i][1] = min(F[i-1][0], F[i-1][2]) + costs[i][1]
        F[i][2] = min(F[i-1][0], F[i-1][1]) + costs[i][2]
    return min(F[-1])

def mincost_v2(costs):
    if not costs:
        return 0
    n = len(costs)
    F = [0] * 3
    F[:] = costs[0][:]
    for i in range(1,n):
        t0 = min(F[1], F[2]) + costs[i][0]
        t1 = min(F[0], F[2]) + costs[i][1]
        t2 = min(F[0], F[1]) + costs[i][2]
        F[0], F[1], F[2] = t0, t1, t2
    return min(F)

class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        return mincost_v2(costs)
