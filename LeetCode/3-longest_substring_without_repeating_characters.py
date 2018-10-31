from collections import Counter

class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = Counter()
        maxlen = 0
        n, k = len(s), 0
        for i, c in enumerate(s):
            while count[c] > 0:
                maxlen = max(maxlen, i - k)
                count[s[k]] -= 1
                k += 1
            count[c] += 1
        maxlen = max(maxlen, n - k)
        return maxlen
