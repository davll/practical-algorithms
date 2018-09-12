# https://practice.geeksforgeeks.org/problems/magic-triplets/0

# O(n^3)
def naive(arr):
    n = len(arr)
    count = 0
    for i in range(n):
        for j in range(i+1, n):
            if arr[i] >= arr[j]:
                continue
            for k in range(j+1, n):
                if arr[j] < arr[k]:
                    count += 1
    return count

# O(n^2)
def naive2(arr):
    n = len(arr)
    cnt = [0] * n
    for j in range(1,n):
        for i in range(0,j):
            if arr[i] < arr[j]:
                cnt[j] += 1
    result = 0
    for k in range(2,n):
        for j in range(1,k):
            if arr[j] < arr[k]:
                result += cnt[j]
    return result

# O(nlog(maxval))
def fenwick(arr):
    # init BIT
    def bit_zeros(n):
        return [0] * (n+1)
    # sum of A[0:i] (not including A[i])
    def bit_sum(bit, i):
        result = 0
        while i > 0:
            result += bit[i]
            i -= i & (-i)
        return result
    # update A[i]
    def bit_update(bit, n, i, val):
        i = i + 1
        while i <= n:
            bit[i] += val
            i += i & (-i)
    #
    n, maxval = len(arr), max(arr)
    cnt = [0] * n
    bit = bit_zeros(maxval+1)
    for j in range(n):
        x = arr[j]
        c = bit_sum(bit, x)
        bit_update(bit, maxval, x, 1)
        cnt[j] = c
    bit = bit_zeros(maxval+1)
    result = 0
    for k in range(n):
        x = arr[k]
        c = bit_sum(bit, x)
        bit_update(bit, maxval, x, cnt[k])
        result += c
    return result

# O(nlogn)
def fenwick2(arr):
    # convert array
    tmp = dict(map(lambda t: (t[1],t[0]), enumerate(sorted(arr))))
    ls = [tmp[x] for x in arr]
    # call fenwick
    return fenwick(ls)

if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n = int(input().strip())
        arr = list(map(int, input().strip().split()))
        result = fenwick2(arr)
        print(str(result))
