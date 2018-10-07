# https://www.hackerrank.com/challenges/min-max-riddle/problem
#
# Hint: two-way, least price stock problem
#
# https://www.geeksforgeeks.org/stock-buy-sell/
# https://www.geeksforgeeks.org/maximum-difference-between-two-elements/
#

from sys import stdin, stdout, stderr

# T = O(n^3)
def riddle_naive(n, arr):
    result = []
    for s in range(1,n+1):
        val = 0
        for i in range(n-s+1):
            val = max(val, min(arr[i:i+s]))
        result.append(val)
    return result

def left_window(arr):
    # left[i] = index of previous element that is smaller than arr[i]
    # => likewise, all elements in arr[left[i]+1:i] are greater or equal to arr[i]
    n = len(arr)
    stack = []
    left = [-1] * n
    for i in range(n):
        while stack and arr[stack[-1]] >= arr[i]:
            stack.pop()
        if stack:
            left[i] = stack[-1]
        stack.append(i)
    return left

def right_window(arr):
    # right[i] = index of next element that is smaller than arr[i]
    # => likewise, all elements in arr[i+1:right[i]] are greater or equal to arr[i]
    n = len(arr)
    stack = []
    right = [n] * n
    for i in reversed(range(n)):
        while stack and arr[stack[-1]] >= arr[i]:
            stack.pop()
        if stack:
            right[i] = stack[-1]
        stack.append(i)
    return right

# T = O(n)
def riddle(n, arr):
    left = left_window(arr)
    right = right_window(arr)
    span = [r-l-1 for l,r in zip(left, right)]
    result = [0] * (n+1)
    for a, s in zip(arr, span):
        result[s] = max(result[s], a)
    for i in reversed(range(n)):
        result[i] = max(result[i], result[i+1])
    return result[1:]

if __name__ == "__main__":
    n = int(stdin.readline().rstrip())
    arr = list(map(int, stdin.readline().rstrip().split()))
    assert len(arr) == n
    ans = riddle(n, arr)
    stdout.write(' '.join(map(str, ans)) + '\n')
