# https://www.hackerrank.com/challenges/swap-nodes-algo/problem

from sys import stdin, stdout, stderr
import sys

sys.setrecursionlimit(2000)

if __name__ == "__main__":
    n = int(stdin.readline().rstrip())
    left = [-1] * n
    right = [-1] * n
    for i in range(n):
        a, b = map(int, stdin.readline().rstrip().split())
        left[i] = a - 1 if a != -1 else -1
        right[i] = b - 1 if b != -1 else -1
    #
    def inorder(i, d, k, ls):
        if i == -1:
            return
        if d % k == 0:
            left[i], right[i] = right[i], left[i]
        #yield from inorder(left[i], d+1, k)
        #yield i+1
        #yield from inorder(right[i], d+1, k)
        inorder(left[i], d+1, k, ls)
        ls.append(i+1)
        inorder(right[i], d+1, k, ls)
    #
    t = int(stdin.readline().rstrip())
    queries = [
        int(stdin.readline().rstrip())
        for _ in range(t)
    ]
    ls = []
    for k in queries:
        inorder(0, 1, k, ls)
        s = ' '.join(map(str, ls))
        stdout.write(s + '\n')
        ls.clear()
