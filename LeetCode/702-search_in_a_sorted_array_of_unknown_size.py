# https://leetcode.com/problems/search-in-a-sorted-array-of-unknown-size/

INVALID_VAL = 2147483647

def search_v1(reader, target):
    i = 0
    while reader.get(i) < target:
        i += 1
    if target == reader.get(i):
        return i
    else:
        return -1

def search_v2(reader, target):
    lower = 0
    upper = target - reader.get(0) + 1
    while lower < upper:
        mid = (lower + upper) // 2
        if target < reader.get(mid):
            upper = mid
        elif target > reader.get(mid):
            lower = mid+1
        else:
            return mid
    return -1

class Solution:
    def search(self, reader, target):
        """
        :type reader: ArrayReader
        :type target: int
        :rtype: int
        """
        return search_v2(reader, target)
