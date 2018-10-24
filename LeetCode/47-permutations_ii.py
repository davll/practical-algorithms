def permute_v1(nums):
    perms, perms2 = [[]], []
    for n in nums:
        for perm in perms:
            for i in range(len(perm)+1):
                perms2.append(perm[:i] + [n] + perm[i:])
                if i < len(perm) and perm[i] == n:
                    break
        perms, perms2 = perms2, perms
        perms2.clear()
    return perms

class Solution:
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        return permute_v1(nums)
