# https://leetcode.com/problems/combination-sum-ii/

def combisum_v1(candidates, target):
    N = len(candidates)
    candidates.sort()
    def backtrack(i, x, buffer):
        if x == target:
            yield buffer[:]
        elif i < N and x < target:
            # count how many candidates[i]
            n = 1
            for j in range(i+1, N):
                if candidates[j] == candidates[i]:
                    n += 1
                else:
                    break
            # skip the i-th number
            yield from backtrack(i+n, x, buffer)
            # contain the i-th number
            cnt = 0
            while x < target and cnt < n:
                x += candidates[i]
                buffer.append(candidates[i])
                cnt += 1
                yield from backtrack(i+n, x, buffer)
            for _ in range(cnt):
                buffer.pop()
    return list(backtrack(0, 0, []))

#
#
def combisum_v2(candidates, target):
    raise NotImplementedError()

class Solution:
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        return combisum_v1(candidates, target)
