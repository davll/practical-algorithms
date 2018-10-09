# Catalan Numbers
#
# Definition:
#
#   c[0] = 1
#   c[n+1] = sum(c[i]c[n-i] for i in [0,n]) for n >= 0
#
# Formal Definition:
#
#   c[n] = (2n)!/((n+1)!n!) = PI((n+k)/k) for n >= 0, k >= 2
#
# Example:
#
# 1, 1, 2, 5, 14, 42, 132, 429, 1430, 4862, ...
#
# https://practice.geeksforgeeks.org/problems/nth-catalan-number/0
# https://www.geeksforgeeks.org/program-nth-catalan-number/
#

from itertools import count

def catalan():
    ct = [1]
    for n in count(1):
        yield ct[-1]
        x = sum(map(lambda i: ct[i] * ct[n-1-i], range(n)))
        ct.append(x)

# c[n] = binomial_coeff(2n, n) / (n+1)
# TODO

# Applications
# https://www.geeksforgeeks.org/applications-of-catalan-numbers/
#

if __name__ == "__main__":
    it = catalan()
    for _ in range(20):
        print(str(next(it)))
