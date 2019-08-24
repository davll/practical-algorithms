#
# 1   -> A     1
# 2   -> B     2
# 3   -> C     3
#   ...
# 26  -> Z    10
# 27  -> AA   11
# 28  -> AB   12
#   ...
# 52  -> AZ   20
# 53  -> BA   21
#   ...
# 78  -> BZ   30
#   ...
# 701 -> ZY
# 702 -> ZZ   110
# 703 -> AAA  111
# 728 -> AAZ  120

TABLE = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')

class Solution:
    def convertToTitle(self, n: int) -> str:
        result = []
        while n > 0:
            n -= 1
            x = n % 26
            n = n // 26
            result.append(TABLE[x])
        return ''.join(reversed(result))
