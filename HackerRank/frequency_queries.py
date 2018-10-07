# https://www.hackerrank.com/challenges/frequency-queries/problem

from sys import stdin, stdout, stderr

def freqQuery(queries):
    freq = {}
    inv = {}
    for cmd, val in queries:
        if cmd == 1:
            f0 = freq.get(val, 0)
            freq[val] = f0 + 1
            if f0 != 0:
                inv[f0] -= 1
            inv[f0+1] = inv.get(f0+1, 0) + 1
        elif cmd == 2:
            f0 = freq.get(val, 0)
            if f0 > 0:
                freq[val] = f0 - 1
                inv[f0] -= 1
                if f0 > 1:
                    inv[f0-1] += 1
        elif cmd == 3:
            if inv.get(val, 0) > 0:
                yield 1
            else:
                yield 0

if __name__ == "__main__":
    n = int(stdin.readline().rstrip())
    queries = [
        tuple(map(int, stdin.readline().rstrip().split()))
        for _ in range(n)
    ]
    for ans in freqQuery(queries):
        stdout.write(str(ans) + '\n')
