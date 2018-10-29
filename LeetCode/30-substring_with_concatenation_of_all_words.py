# Rabin-Karp Algorithm
def find_substring_v1(text, words):
    wc = {}
    wi = {}
    for w in words:
        wc[w] = wc.get(w, 0) + 1
        if wc[w] == 1:
            wi[w] = len(wi)
    nw = sum(wc.values())
    m = len(words[0])
    for i in range(len(text) - len(words) * m + 1):
        count = [0] * nw
        for j in range(0, len(words) * m, m):
            s = text[i+j:i+j+m]
            if s in wc:
                if count[wi[s]] < wc[s]:
                    count[wi[s]] += 1
                else:
                    break
        if sum(count) == len(words):
            yield i

# Aho-Corasick Algorithm
def find_substring_v2(text, words):
    raise NotImplemented()

class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        if not words:
            return []
        return list(find_substring_v1(s, words))
