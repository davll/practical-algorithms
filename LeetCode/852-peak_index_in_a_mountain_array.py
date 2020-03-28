import numpy as np

# it can be solved with binary search

class Solution:
    def peakIndexInMountainArray(self, A: List[int]) -> int:
        return np.argmax(A)
