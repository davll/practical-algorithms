# https://www.hackerrank.com/challenges/coin-change/problem
#
# f[x;c]: the number of ways that make up the amount x
#         with 1...c coin types
#
# f[x;c] = 1                    if x = 0 and c = 0
#        = f[x;c-1]             if x < c and c > 0
#        = f[x;c-1] + f[x-c;c]  if x >= c and c > 0
#


def coinchange(amount, coins):
    count = [0] * (amount + 1)
    count[0] = 1
    for c in coins:
        for i in range(c, amount+1):
            count[i] += count[i-c]
    return count[amount]

if __name__ == "__main__":
    n, m = map(int, input().split())
    c = list(map(int, input().split()))
    result = coinchange(n, c)
    print(str(result))
