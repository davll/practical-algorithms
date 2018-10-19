def strstr_naive(text, pat):
    if not pat:
        return 0
    n, p = len(text), len(pat)
    for i in range(n):
        if text[i:p+i] == pat:
            return i
    return -1

class KmpSearch:
    def __init__(self, pattern):
        table = [0] * (len(pattern) + 1)
        k = 0
        for i in range(1, len(pattern)):
            while k > 0 and pattern[k] != pattern[i]:
                k = table[k]
            if pattern[k] == pattern[i]:
                k += 1
            table[i+1] = k
        self.pattern = pattern
        self.table = table
    #
    def search(self, text):
        if not self.pattern:
            return 0
        k = 0
        for i, c in enumerate(text):
            while k > 0 and self.pattern[k] != c:
                k = self.table[k]
            if self.pattern[k] == c:
                k += 1
            if k == len(self.pattern):
                return (i-k+1)
        return -1

def strstr_kmp(text, pat):
    kmp = KmpSearch(pat)
    return kmp.search(text)

class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        return strstr_kmp(haystack, needle)
