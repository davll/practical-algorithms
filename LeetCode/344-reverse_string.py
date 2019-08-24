def revstr_v1(s):
    n = len(s)
    l, r = 0, n-1
    while l < r:
        s[l], s[r] = s[r], s[l]
        l, r = l+1, r-1

def revstr_v2(s):
    s.reverse()

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        revstr_v2(s)
