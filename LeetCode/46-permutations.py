# https://leetcode.com/problems/permutations/

def permute_v1(nums):
    n = len(nums)
    buf = [-1] * n
    used = [False] * n
    def backtrack(i):
        if i < n:
            for j in range(n):
                if not used[j]:
                    used[j] = True
                    buf[i] = nums[j]
                    yield from backtrack(i+1)
                    used[j] = False
        else:
            yield buf[:]
    return list(backtrack(0))

def permute_v2(nums):
    perms, perms2 = [[]], []
    for n in nums:
        for perm in perms:
            for i in range(len(perm)+1):
                perms2.append(perm[:i] + [n] + perm[i:])
        perms, perms2 = perms2, perms
        perms2.clear()
    return perms

def permute_v3(nums):
    from itertools import permutations
    return list(permutations(nums, len(nums)))

class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        return permute_v3(nums)
