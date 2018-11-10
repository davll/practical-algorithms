# https://leetcode.com/problems/escape-the-ghosts/

class Solution:
    def escapeGhosts(self, ghosts, target):
        """
        :type ghosts: List[List[int]]
        :type target: List[int]
        :rtype: bool
        """
        tx, ty = target
        for gx, gy in ghosts:
            if abs(gx-tx) + abs(gy-ty) <= abs(tx) + abs(ty):
                return False
        return True
