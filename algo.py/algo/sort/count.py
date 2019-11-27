# Counting Sort

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
