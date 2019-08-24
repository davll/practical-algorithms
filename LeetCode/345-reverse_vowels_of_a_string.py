def isvowel(c):
    return str.lower(c) in ['a', 'i', 'u', 'e', 'o']

def revowl(s):
    s = list(s)
    n = len(s)
    l, r = 0, n-1
    while l < r:
        if not isvowel(s[l]):
            l = l + 1
        elif not isvowel(s[r]):
            r = r - 1
        else:
            s[l], s[r] = s[r], s[l]
            l, r = l+1, r-1
    return ''.join(s)

class Solution:
    def reverseVowels(self, s: str) -> str:
        return revowl(s)
