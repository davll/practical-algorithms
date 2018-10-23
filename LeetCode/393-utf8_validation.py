def validate_utf8(data):
    n = len(data)
    i = 0
    while i < n:
        nb = _nsucc_bits(data[i])
        if nb < 0:
            return False
        i += 1
        for _ in range(nb):
            if i < n:
                if not _follow_check(data[i]):
                    return False
                i += 1
            else:
                return False
    return True

_HEADER_MASK = [
    int('10000000', base=2),
    int('11100000', base=2),
    int('11110000', base=2),
    int('11111000', base=2)
]

_HEADER_VALUE = list(map(lambda x: (x << 1) & 0xFF, _HEADER_MASK))

_FOLLOW_MASK =  int('11000000', base=2)
_FOLLOW_VALUE = int('10000000', base=2)

#print(', '.join(map(bin, _HEADER_MASK)))
#print(', '.join(map(bin, _HEADER_VALUE)))

def _nsucc_bits(x):
    for i, (m, v) in enumerate(zip(_HEADER_MASK, _HEADER_VALUE)):
        if (x & m) == v:
            return i
    return -1

def _follow_check(x):
    return (x & _FOLLOW_MASK) == _FOLLOW_VALUE

class Solution:
    def validUtf8(self, data):
        """
        :type data: List[int]
        :rtype: bool
        """
        return validate_utf8(data)
