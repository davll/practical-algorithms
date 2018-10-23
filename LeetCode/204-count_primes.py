from math import sqrt, ceil

class Solution:
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0
        primes = [1] * (n+1)
        primes[0] = 0
        primes[1] = 0
        for i in range(2, int(ceil(sqrt(n)))):
            if primes[i]:
                primes[i*i:n:i] = [0] * len(primes[i*i:n:i])
            i += 1
        return sum(primes[:n])
