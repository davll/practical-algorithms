# https://www.hackerrank.com/challenges/decibinary-numbers/problem
#
#
#

# (0)db = 0
# (1)db = 1
# (2)db  = 2 = (0*2 + 2*1)
# (10)db = 2 = (1*2 + 0*1)
# (3)db  = 3 = (0*2 + 3*1)
# (11)db = 3 = (1*2 + 1*1)
#

from sys import stdin, stdout, stderr
#from heapq import heapify, heappush, heappop

def db2dec(x):
    a, y = 1, 0
    while x > 0:
        y += (x % 10) * a
        a = a * 2
        x = x // 10
    return y

def dec2db(x):
    y = 0
    e = 1
    while x > 0:
        y = y + (x % 2) * e
        x = x // 2
        e = e * 10
    return y

def msb(x):
    a = 1
    while a * 2 <= x:
        a = a * 2
    return a

for i in range(5):
    stderr.write('{i}-{j}: '.format(i=i*10, j=(i+1)*10-1) + str([db2dec(x) for x in range(i*10, (i+1)*10)]) + '\n')

for i in range(15):
    stderr.write(str(i) +" => " + str(dec2db(i)) + '\n')

def decibinaryNumbers(x):
    k = 0
    while k < x:
        pass

#if __name__ == "__main__":
#    for _ in range(int(stdin.readline().rstrip())):
#        x = int(stdin.readline().rstrip())
#        ans = decibinaryNumbers(x)
#        stdout.write(str(ans) + '\n')
