from math import log2, floor

class LazyTable:
    def __init__(self):
        self.table = None
    def __contains__(self, x):
        if not self.table:
            self._lazy_init()
        return x in self.table
    def _lazy_init(self):
        self.table = set([4 << (2 * i) for i in range(16)])
        self.table.add(1)

TABLE = LazyTable()

def is_power_of_four_v1(num):
    return num in TABLE

def is_power_of_four_v2(num):
    if num <= 0:
        return False
    x = log2(num)
    if floor(x) != x:
        return False
    return int(x) % 2 == 0

class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        return is_power_of_four_v2(num)
