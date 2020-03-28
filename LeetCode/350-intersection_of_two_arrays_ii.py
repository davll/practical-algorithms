from collections import Counter

def compute_v1(nums1, nums2):
    c1 = Counter(nums1)
    c2 = Counter(nums2)
    result = []
    for k in c1.keys():
        if k in c2:
            n = min(c1[k], c2[k])
            if n == 0:
                continue
            result.extend([k] * n)
    return result

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return compute_v1(nums1, nums2)
