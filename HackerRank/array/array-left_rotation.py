#!/bin/python3

def left_rotate(arr, k):
    return arr[k:] + arr[:k]

if __name__ == '__main__':
    n,d = map(int, input().split())
    a = list(map(int, input().rstrip().split()))
    b = left_rotate(a, d)
    print(' '.join(map(str, b)))
