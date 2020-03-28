class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        lookup = set(nums1)
        return list(set(filter(lambda x: x in lookup, nums2)))
