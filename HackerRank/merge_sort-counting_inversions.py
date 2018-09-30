#
#
#

from sys import stdin, stdout, stderr

def mergesort(arr, lo, hi, tmp):
    if lo >= hi:
        return 0
    mid = (lo + hi) // 2
    #stderr.write("lo, mid, hi = {lo}, {mid}, {hi}\n".format(lo=lo, hi=hi, mid=mid))
    nswaps = 0
    nswaps += mergesort(arr, lo, mid, tmp)
    nswaps += mergesort(arr, mid+1, hi, tmp)
    nswaps += merge(arr, lo, mid, mid+1, hi, tmp)
    return nswaps

def merge(arr, lo0, hi0, lo1, hi1, tmp):
    i, j, k = lo0, lo1, lo0
    nswaps = 0
    while i <= hi0 and j <= hi1:
        if arr[i] <= arr[j]:
            tmp[k] = arr[i]
            i, k = i+1, k+1
        else: # arr[i] > arr[j] => means arr[i:hi0+1] > arr[j]
            tmp[k] = arr[j]
            j, k = j+1, k+1
            nswaps += hi0 - i + 1
    if i <= hi0:
        tmp[k:hi1+1] = arr[i:hi0+1]
    if j <= hi1:
        tmp[k:hi1+1] = arr[j:hi1+1]
    arr[lo0:hi1+1] = tmp[lo0:hi1+1]
    return nswaps

def count_inversions(arr):
    n = len(arr)
    tmp = [0] * n
    return mergesort(arr, 0, n-1, tmp)

if __name__ == '__main__':
    for _ in range(int(stdin.readline().rstrip())):
        n = int(stdin.readline().rstrip())
        arr = list(map(int, stdin.readline().rstrip().split()))
        result = count_inversions(arr)
        stdout.write(str(result) + '\n')
