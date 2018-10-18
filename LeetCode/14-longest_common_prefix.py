def lcp(strings):
    if not strings:
        return ""
    pfx = []
    for i, c in enumerate(strings[0]):
        ok = True
        for s in strings[1:]:
            if i >= len(s) or c != s[i]:
                ok = False
                break
        if ok:
            pfx.append(c)
        else:
            break
    return ''.join(pfx)

class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        return lcp(strs)
