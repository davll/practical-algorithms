# https://leetcode.com/problems/group-anagrams/

from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        d = defaultdict(lambda: [])
        for s in strs:
            d[''.join(sorted(s))] += [s]
        return list(d.values())
