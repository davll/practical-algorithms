# T = O(nk)
def countsort(arr):
    maxval, minval = max(arr), min(arr)
    n, k = len(arr), (maxval - minval + 1)
    count = [0] * k
    # count values
    for x in arr:
        count[x - minval] += 1
    # transform to actual position
    for i in range(1, k):
        count[i] += count[i-1]
    # build output
    result = [0] * n
    for (i, x) in enumerate(arr):
        j = count[x - minval] - 1
        result[j] = x
        count[x - minval] -= 1
    return result

def bucketsort(arr, nb, key):
    n = len(arr)
    buckets = [[] for _ in range(nb)]
    # group array elements
    for x in arr:
        k = key(x)
        buckets[k].append(x)
    # sort individual buckets
    for b in buckets:
        b.sort()
    # concatenate all buckets
    i = 0
    for b in buckets:
        j = i + len(b)
        arr[i:j] = b[:]
        i = j

# T = O(nw)
def radixsort(arr):
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
