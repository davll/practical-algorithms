# https://www.hackerrank.com/challenges/maxsubarray/problem

#
# f[i]: maximum sum of subarray ending at i
#
# f[i] = a[0] if i = 0
#      = max { a[i], f[i-1] + a[i] } if i > 0
#
def max_subarray(a):
    result, c = a[0], a[0]
    for x in a[1:]:
        c = max(x, c + x)
        result = max(c, result)
    return result

#
# f[i]: maximum sum of subsequence ending at i
#
# f[i] = a[0] if i = 0
#      = max { a[i], f[i-1], f[i-1]+a[i] } if i > 0
#
def max_subsequence(a):
    result, c = a[0], a[0]
    for x in a[1:]:
        c = max(x, c, c+x)
        result = max(c, result)
    return result

if __name__ == "__main__":
    for _ in range(int(input())):
        n = int(input())
        arr = list(map(int, input().split()))
        res1 = max_subarray(arr)
        res2 = max_subsequence(arr)
        print("%d %d" % (res1, res2))
