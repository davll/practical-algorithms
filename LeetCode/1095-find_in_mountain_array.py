# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        n = mountain_arr.length()
        def get(i):
            return mountain_arr.get(i)
        # find peak
        peak = -1
        l, r = 0, n-1
        while l <= r:
            m = (l + r) // 2
            l_asc = (m == 0 or get(m-1) < get(m))
            r_dsc = (m == n-1 or get(m) > get(m+1))
            if l_asc and r_dsc:
                peak = m
                break
            elif l_asc:
                l = m+1
            else:
                r = m-1
        peak_val = get(peak)
        if peak == -1 or target > peak_val:
            return -1
        elif target == peak_val:
            return peak
        # find target in the left part
        l, r = 0, peak-1
        while l <= r:
            m = (l + r) // 2
            val = get(m)
            if target == val:
                return m
            elif target < val:
                r = m-1
            else:
                l = m+1
        # find target in the right part
        l, r = peak+1, n-1
        while l <= r:
            m = (l + r) // 2
            val = get(m)
            if target == val:
                return m
            elif target < val:
                l = m+1
            else:
                r = m-1
        # if not found
        return -1
