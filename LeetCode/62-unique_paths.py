class Solution:
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        # (m+n-2)!/((m-1)!(n-1)!)
        # = C(m+n-2, n-1)
        #
        # C(n,k) = C(n-1,k-1) + C(n-1,k)
        # C(n,0) = C(n,n) = 1
        #
        dp1 = [0] * (m+n)
        dp2 = [0] * (m+n)
        dp1[0] = 1 # C(0,0)
        for i in range(1, m+n-1):
            dp2[0] = 1
            dp2[i] = 1
            for j in range(1, i):
                dp2[j] = dp1[j-1] + dp1[j]
            dp1, dp2 = dp2, dp1
        return dp1[n-1]
