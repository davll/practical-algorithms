def one_edit_distance(s1, s2):
    n1, n2 = len(s1), len(s2)
    l, r = 0, 0
    while l < n1 and l < n2:
        if s1[l] == s2[l]:
            l += 1
        else:
            break
    n1, n2 = n1-l, n2-l
    while r < n1 and r < n2:
        if s1[-1-r] == s2[-1-r]:
            r += 1
        else:
            break
    n1, n2 = n1-r, n2-r
    return max(n1, n2) == 1

class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        return one_edit_distance(s, t)
