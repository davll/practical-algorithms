# Binomial Coefficient
#
# c[n,k]:
#   (1) the coefficient of X^k in the expansion of (1 + X)^n
#   (2) the number of ways, disregarding order,
#       that k objects can be chosen from among n objects
#   (3) the number of k-element subsets (or k-combinations)
#       of an n-element set.
#
# Definition: c[n,k] = n!/(k!(n-k)!)
#
#    c[0,0] = 1
#    c[n,0] = 1
#    c[n,n] = 1
#    c[n,k] = c[n-1,k] + c[n-1,k-1]
#
#  => c[n,k] = (n * (n-1) * ... * (n-k+1)) / (k * (k-1) * ... * 1)
#
# Pascal Rule
# c[n,k] = c[n-1,k] + c[n-1,k-1]
#   => builds a Pascal triangle
#
