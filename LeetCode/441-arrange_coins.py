class Solution:
    def arrangeCoins(self, n: int) -> int:
        # n >= k * (1 + k) / 2
        def total(x):
            return x * (1 + x) // 2
        k = 1
        while total(k) < n:
            k += 1
        if total(k) == n:
            return k
        else:
            return k-1
