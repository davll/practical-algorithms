from typing import TypeVar, List

# T = O(nw)
def radixsort(arr: List[int]) -> List[int]:
    n, maxval = len(arr), max(arr)
    tmp = [0] * n
    count = [0] * 10
    exp = 1
    while maxval // exp > 0:
        for i in range(10):
            count[i] = 0
        for x in arr:
            count[(x // exp) % 10] += 1
        for i in range(1, 10):
            count[i] += count[i-1]
        for i in range(n-1, -1, -1):
            x = (arr[i] // exp) % 10
            tmp[count[x]-1] = arr[i]
            count[x] -= 1
        arr, tmp = tmp, arr
        exp *= 10
    return arr
