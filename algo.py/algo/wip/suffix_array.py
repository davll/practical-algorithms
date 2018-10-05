# https://visualgo.net/en/suffixarray

# Suffix Array
#
# 1. a sorted array of all suffixes of a string S
# 2. A[i] denotes the starting position of i-th suffix
# 3. an empty string is also a suffix
# 4. S[A[i-1]:] < S[A[i]:]
#

class SuffixArray:
    def __init__(self, text):
        arr = [i for i in range(len(text) + 1)]
        arr.sort(key = lambda x: text[x:])
        self._text = text
        self._suffix = arr
    @property
    def text(self):
        return self._text
    def __len__(self):
        return len(self._suffix)
    def __getitem__(self, i):
        return self._text[self._suffix[i]:]
    def __iter__(self):
        return iter(map(lambda x: self._text[x:], self._suffix))
    def suffixrange(self, i):
        return (self._suffix[i], len(self._text))
    #
    def find_pattern(self, pattern):
        n = len(self._text)
        # find lower bound
        l, r = 0, n
        while l < r:
            m = (l+r) // 2
            if pattern > self[m]:
                l = m+1
            else:
                r = m
        # find upper bound
        s, r = l, n
        while l < r:
            m = (l+r) // 2
            if pattern < self[m]:
                r = m
            else:
                l = m+1
        return (s, r)
