# https://www.geeksforgeeks.org/median-two-sorted-arrays-different-sizes-ologminn-m/

def median_v1(nums1, nums2):
    n, a = len(nums1) + len(nums2), nums1 + nums2
    a.sort()
    if n % 2 == 1:
        return a[n // 2]
    else:
        return (a[n // 2] + a[n // 2 - 1]) / 2

def median_v2(nums1, nums2):
    a, b = sorted((nums1, nums2), key=len)
    m, n = len(a), len(b)
    after = (m + n - 1) // 2
    lo, hi = 0, m
    while lo < hi:
        i = (lo + hi) // 2
        j = after-i-1
        if j < 0 or a[i] >= b[j]:
            hi = i
        else:
            lo = i + 1
    i = lo
    j = after - i
    tmp = sorted(a[i:i+2] + b[j:j+2])
    return (tmp[0] + tmp[1-(m+n)%2]) / 2

class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        return median_v2(nums1, nums2)

#if __name__ == "__main__":
#    l1 = [1,2,3]
#    l2 = [1,2,2]
#    print("median = " + str(median_v2(l1, l2)))
