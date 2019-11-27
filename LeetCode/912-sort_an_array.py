from collections import deque

def mergesort_r(arr, first, end, aux = None):
    if first >= end-1:
        return
    if aux is None:
        aux = [None] * len(arr)
    mid = (first + end) // 2
    mergesort_r(arr, first, mid, aux)
    mergesort_r(arr, mid, end, aux)
    merge_array(aux, first, arr, first, mid, arr, mid, end)
    for i in range(first, end):
        arr[i] = aux[i]

def mergesort_i(arr):
    n = len(arr)
    q = deque((i, i+1)for i in range(n))
    aux = [None] * n
    while len(q) >= 2:
        first1, end1 = q.popleft()
        first2, end2 = q.popleft()
        assert first1 < end1
        assert first2 < end2
        #print("[{}:{}] + [{}:{}]".format(first1, end1, first2, end2))
        if end1 == first2:
            # merge the two slices
            merge_array(aux, first1, arr, first1, end1, arr, first2, end2)
            for i in range(first1, end2):
                arr[i] = aux[i]
            # push merged slice
            q.append((first1, end2))
        else:
            # the two slices are not consecutive
            # push the first slice
            q.append((first1, end1))
            # put back the second slice
            q.appendleft((first2, end2))

def merge_array(dst, offset, src1, first1, end1, src2, first2, end2):
    i, j, k = first1, first2, offset
    while i < end1 and j < end2:
        if src1[i] <= src2[j]:
            dst[k] = src1[i]
            i += 1
        else:
            dst[k] = src2[j]
            j += 1
        k += 1
    while i < end1:
        dst[k] = src1[i]
        i, k = i+1, k+1
    while j < end2:
        dst[k] = src2[j]
        j, k = j+1, k+1

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

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        #mergesort_r(nums, 0, len(nums))
        #mergesort_i(nums)
        #return nums
        return countsort(nums)
