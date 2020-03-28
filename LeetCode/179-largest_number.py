from functools import cmp_to_key

def elen(x):
    if x == 0:
        return 1
    n = 0
    while x > 0:
        n += 1
        x = x // 10
    return n

def compare_num(a, b):
    x = a * (10 ** elen(b)) + b
    y = b * (10 ** elen(a)) + a
    return y - x

def largest_number_v1(nums):
    if all(map(lambda x: x == 0, nums)):
        return "0"
    nums.sort(key = cmp_to_key(compare_num))
    return ''.join(map(str,nums))

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        return largest_number_v1(nums)
