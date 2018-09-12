def lis(A):
    n = len(A)
    dp = [1] * n
    for i in range(1, n):
        l = 1
        for j in range(0, i):
            if A[j] < A[i]:
                l = max(l, dp[j] + 1)
        dp[i] = l
    return max(dp)

if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n = int(input().strip())
        a = list(map(int, input().strip().split()))
        if not a:
            print("0")
        else:
            print(str(lis(a)))
