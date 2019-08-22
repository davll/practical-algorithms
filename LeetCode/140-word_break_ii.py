#
#
#

def wdbrk(s, wdict):
    n = len(s)
    F = [[] for _ in range(n+1)]
    F[0] = True
    for i in range(1, n+1):
        for w in wdict:
            if len(w) <= i and w == s[i-len(w):i]:
                if F[i-len(w)]:
                    F[i].append(w)
    def backtrack(l, stack):
        if l == 0 and stack:
            yield ' '.join(reversed(stack))
        else:
            for w in F[l]:
                stack.append(w)
                yield from backtrack(l-len(w), stack)
                stack.pop()
    return list(backtrack(n, []))

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        return wdbrk(s, wordDict)
