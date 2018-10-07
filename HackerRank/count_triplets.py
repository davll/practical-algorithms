# https://www.hackerrank.com/challenges/count-triplets-1/problem

from sys import stdin, stdout, stderr

def countTriplets(arr, r):
    n2i = {}
    n2j = {}
    n2k = {}
    for x in arr:
        if x % r == 0:
            if x % (r * r) == 0:
                n2k[x] = n2k.get(x, 0) + n2j.get(x//r, 0)
            n2j[x] = n2j.get(x, 0) + n2i.get(x//r, 0)
        n2i[x] = n2i.get(x, 0) + 1
    return sum(n2k.values())

if __name__ == "__main__":
    n, r = map(int, stdin.readline().rstrip().split())
    arr = list(map(int, stdin.readline().rstrip().split()))
    ans = countTriplets(arr, r)
    stdout.write(str(ans) + '\n')
