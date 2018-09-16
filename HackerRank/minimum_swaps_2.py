#!/bin/python3

from sys import stdin, stdout, stderr

# Hint: Selection Sort

# Complete the minimumSwaps function below.
def minimumSwaps(a):
    n = len(a)
    # b: sorted index => original index
    b = list(sorted(range(n), key = lambda i: a[i]))
    # c: original index => sorted index
    c = [-1] * n
    for i in range(n):
        c[b[i]] = i
    #print("a = " + str(a), file = stderr)
    #print("b = " + str(b), file = stderr)
    #print("c = " + str(c), file = stderr)
    count = 0
    for i in range(n):
        src = b[i]
        if i != src:
            #print("swap a[%d] = %d, a[%d] = %d" % (i, a[i], src, a[src]), file = stderr)
            a[i], a[src] = a[src], a[i]
			#print("b[i] = %d, b[src] = %d" % (b[i], b[src]), file = stderr)
            b[c[i]], b[c[src]] = src, i
			c[i], c[src] = c[src], c[i]
            #print("a = " + str(a), file = stderr)
            #print("b = " + str(b), file = stderr)
            #print("c = " + str(c), file = stderr)
            count += 1
    return count

if __name__ == '__main__':
    n = int(stdin.readline().strip())
    arr = list(map(int, stdin.readline().strip().split()))
    res = minimumSwaps(arr)
    stdout.write(str(res) + '\n')
