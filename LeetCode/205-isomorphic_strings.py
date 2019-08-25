#
#
#

def is_isomorphic_v1(s, t):
    assert len(s) == len(t)
    mappings = dict()
    mapped = set()
    for a, b in zip(s, t):
        if a in mappings:
            x = mappings[a]
            if x != b:
                return False
        elif b in mapped:
            return False
        else:
            mappings[a] = b
            mapped.add(b)
    return True

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        return is_isomorphic_v1(s, t)
