# https://leetcode.com/problems/image-overlap/
# https://leetcode.com/articles/image-overlap/

class Solution:
    def largestOverlap(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: int
        """
        n = len(A)
        assert n == len(A[0]) and n == len(B) and n == len(B[0])
        A = convert_to_bitmap(n, A)
        B = convert_to_bitmap(n, B)
        return max(bruteforce(n, A, B), bruteforce(n, B, A))

def bruteforce(n, A, B):
    largest = 0
    for i in range(n):
        for j in range(n):
            C = translate(n, A, i, j)
            overlapped = sum(map(lambda t: count_1s(t[0] & t[1]), zip(C, B)))
            largest = max(largest, overlapped)
    return largest

def translate(n, A, i, j):
    return [0] * i + [r >> j for r in A[:(n-i)]]

def convert_to_bitmap(n, arr):
    bmp = [0] * n
    for i in range(n):
        for j in range(n):
            bmp[i] = (bmp[i] << 1) | int(arr[i][j])
    return bmp

def count_1s(x):
    n = 0
    while x > 0:
        n += x & 1
        x = x >> 1
    return n
