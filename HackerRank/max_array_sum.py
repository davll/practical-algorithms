#!/bin/python3
# https://www.hackerrank.com/challenges/max-array-sum/problem

# Complete the maxSubsetSum function below.
def maxSubsetSum(arr):
    n = len(arr)
    opt = [0] * n
    opt[0] = arr[0]
    opt[1] = max(arr[0], arr[1])
    for i in range(2, n):
        opt[i] = max(arr[i], opt[i-1], arr[i] + opt[i-2])
    return max(opt)

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().rstrip().split()))
    res = maxSubsetSum(arr)
    print(str(res))
