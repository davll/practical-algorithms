# https://www.hackerrank.com/challenges/largest-rectangle/problem
#
#
#         X
#         X X        => [3:5]
#       X X X        => [2:5]
#       X X X
#       X X X   X
#     X X X X   X    => [1:5]
#     X X X X X X    => [1:7]
#   X X X X X X X X  => [0:8] 
#  -----------------
#  |0|1|2|3|4|5|6|7|
#

from sys import stdin, stdout, stderr

def largestRectangle(n, height):
    assert len(height) == n
    stack = [(height[0], 0)]
    result = 0
    for i in range(1, n):
        if height[i] > height[i-1]:
            stack.append((height[i], i))
        else:
            h1, i2 = height[i], i
            while stack and stack[-1][0] > h1:
                h2, j = stack.pop()
                i2 = j
                a = h2 * (i - j)
                result = max(result, a)
            stack.append((h1, i2))
    for h, i in stack:
        a = h * (n - i)
        result = max(result, a)
    return result

if __name__ == "__main__":
    n = int(stdin.readline().rstrip())
    h = list(map(int, stdin.readline().rstrip().split()))
    ans = largestRectangle(n, h)
    stdout.write(str(ans) + '\n')
