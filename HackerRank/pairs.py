# ww.hackerrank.com/challenges/pairs/problem

from sys import stdin, stdout, stderr

# O(n^2)
def pairs_v1(k, arr):
    n = len(arr)
    arr.sort()
    count = 0
    for i in range(n):
        for j in range(i+1, n):
            if arr[j] - arr[i] == k:
                count += 1
            elif arr[j] - arr[i] > k:
                break
    return count

# O(n*log(n))
def pairs_v2(k, arr):
    n = len(arr)
    arr.sort()
    count = 0
    for i in range(n):
        key = arr[i]+k
        if bsearch(arr, i+1, n-1, key):
            count += 1
    return count

def bsearch(arr, l, r, key):
    """
    l: lower bound (ex: 0)
    r: upper bound (ex: N-1)
    key: target key
    """
    result = None
    while l <= r:
        m = (l + r) // 2
        k = arr[m]
        if key == k:
            result = m
            break
        elif key < k:
            r = m-1
        else: # key > k
            l = m+1
    return result

if __name__ == "__main__":
    n, k = map(int, stdin.readline().rstrip().split())
    arr = list(map(int, stdin.readline().rstrip().split()))
    ans = pairs_v2(k, arr)
    stdout.write(str(ans) + '\n')
