# Hamming Numbers
#
# Example: Ugly Numbers
#
# 2: 1x2 2x2 3x2 4x2 5x2 ...
# 3: 1x3 2x3 3x3 4x3 5x3
# 5: 1x5 2x5 3x5 4x5 5x5
#
# f[i]: i-th ugly number
#
# f[i] = 1            if i = 0
#      = min { f[i2]*2, f[i3]*3, f[i5]*5 }
#

def ugly_numbers():
    return hamming2((2, 3, 5))

def hamming(multipliers):
    dp = [1]
    indices = [0] * len(multipliers)
    while True:
        yield dp[-1]
        vals = list(map(lambda x: dp[x[0]]*x[1], zip(indices, multipliers)))
        tmp = min(vals)
        for i, v in enumerate(vals):
            if tmp == v:
                indices[i] += 1
        dp.append(tmp)

def hamming2(multipliers):
    from heapq import heappush, heappop
    heap = [1]
    while True:
        h = heappop(heap)
        while heap and h == heap[0]:
            heappop(heap)
        for m in multipliers:
            heappush(heap, m*h)
        yield h

if __name__ == "__main__":
    it = ugly_numbers()
    for _ in range(20):
        print(str(next(it)))
