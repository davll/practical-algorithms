# https://leetcode.com/problems/combination-sum/

def combisum_v1(candidates, target):
    N = len(candidates)
    def backtrack(i, x, buffer):
        if x == target:
            yield buffer[:]
        elif i < N and x < target:
            # skip the i-th number
            yield from backtrack(i+1, x, buffer)
            # contain the i-th number
            cnt = 0
            while x < target:
                x += candidates[i]
                buffer.append(candidates[i])
                cnt += 1
                yield from backtrack(i+1, x, buffer)
            for _ in range(cnt):
                buffer.pop()
    return list(backtrack(0, 0, []))

# F[t;i] = set of combinations of X[0]..X[i-1] whose total sum is t
#
# F[0;0] = [[]]
# F[t;0] = []
# F[t;i] = F[t-X[i-1];i-1]
#
def combisum_v2(candidates, target):
    raise NotImplementedError()

class Solution:
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        return combisum_v1(candidates, target)
