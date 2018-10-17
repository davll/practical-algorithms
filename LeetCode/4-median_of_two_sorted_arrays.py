# https://www.geeksforgeeks.org/k-th-element-two-sorted-arrays/

def median_v1(nums1, nums2):
    l = len(nums1) + len(nums2)
    a = nums1 + nums2
    a.sort()
    if l % 2 == 1:
        return a[l // 2]
    else:
        x = a[l // 2]
        y = a[l // 2 - 1]
        return (x + y) / 2

def median_v2(nums1, nums2):
    l = len(nums1) + len(nums2)
    if l % 2 == 1:
        return kth_v2(nums1, nums2, l//2)
    else:
        x = kth_v2(nums1, nums2, l//2)
        y = kth_v2(nums1, nums2, l//2-1)
        return (x + y) / 2

class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        return median_v2(nums1, nums2)

if __name__ == "__main__":
    l1 = [1,2,3]
    l2 = [1,2,2]
    print("median = " + str(median_v2(l1, l2)))
