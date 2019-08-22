#
#
#

def wdbrk(s, wdict):
    n = len(s)
    F = [False] * (n+1)
    F[0] = True
    for i in range(1, n+1):
        for w in wdict:
            if len(w) <= i and w == s[i-len(w):i]:
                F[i] = F[i] or F[i-len(w)]
    return F[n]

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        return wdbrk(s, wordDict)
