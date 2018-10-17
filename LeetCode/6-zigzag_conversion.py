def zigzag(s, nrow):
    if nrow == 1:
        yield from iter(s)
        return
    n = len(s)
    ns = nrow * 2 - 2
    i = 0
    # the first row
    while i < n:
        yield s[i]
        i += ns
    # the middle rows
    for r in range(1, nrow-1):
        i, j = r, ns-r
        while i < n and j < n:
            yield s[i]
            yield s[j]
            i, j = i+ns, j+ns
        while i < n:
            yield s[i]
            i += ns
    i = nrow-1
    # the last row
    while i < n:
        yield s[i]
        i += ns

class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        return ''.join(zigzag(s, numRows))
