def reformat(S, K):
    i = 0
    result = []
    for c in filter(lambda c: c.isalnum(), reversed(S)):
        if i > 0 and i % K == 0:
            result.append('-')
        result.append(c.upper())
        i += 1
    result.reverse()
    return ''.join(result)

class Solution:
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        return reformat(S, K)
