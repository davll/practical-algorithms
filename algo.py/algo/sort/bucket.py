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
