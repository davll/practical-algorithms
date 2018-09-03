class Solution:
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [1 for i in range(0,n)]
        i2, i3, i5, k = 0, 0, 0, 1
        while k < n:
            v2 = dp[i2] * 2
            v3 = dp[i3] * 3
            v5 = dp[i5] * 5
            tmp = min([v2, v3, v5])
            if tmp == v2:
                i2 += 1
            if tmp == v3:
                i3 += 1
            if tmp == v5:
                i5 += 1
            dp[k] = tmp
            k += 1
        return dp[n-1]

if __name__ == "__main__":
    x = int(input("Enter a number: "))
    s = Solution()
    y = s.nthUglyNumber(x)
    print(str(x) + "-th ugly number is " + str(y))
