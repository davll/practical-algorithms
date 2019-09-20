from bisect import bisect_left

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        for i in range(n):
            x = target - numbers[i]
            j = bisect_left(numbers, x, lo=i+1)
            if i < j and j >= 0 and j < n and numbers[j] == x:
                return [i+1,j+1]
