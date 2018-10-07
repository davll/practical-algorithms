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

# x: decibinary
# y: decimal
def db2dec(x):
    a, y = 1, 0
    while x > 0:
        y += (x % 10) * a
        a = a * 2
        x = x // 10
    return y

# x: decimal
# y: decibinary
def dec2db(x):
    y = 0
    e = 1
    while x > 0:
        y = y + (x % 2) * e
        x = x // 2
        e = e * 10
    return y

# x: decibinary
# a: most significant digit
# e: power
def dbmsd(x):
    e = 0
    while x >= 10:
        e = e + 1
        x = x // 10
    return (x, e)

# x: decimal
# a: most significant bit mask
def msb(x):
    a = 1
    while a * 2 <= x:
        a = a * 2
    return a

# n: decimal
# returns how many decibinary numbers equal to n
def bruteforce(n):
    mem = {}
    def f(x):
        a, e = dbmsd(x)
        if e == 0:
            return 1
        else:
            if x in mem:
                return mem[x]
            s = f(x - a * (10 ** e))
            if (x // (10 ** (e-1))) % 10 < 8:
                s += f(x - (10 ** e) + 2 * (10 ** (e-1)))
            mem[x] = s
            return s
    return f(dec2db(n))

#for i in range(50):
#    stderr.write('count({x}) = {y}\n'.format(x=i+1, y=count(i+1)))

for i in range(200):
    stderr.write('{i}-{j}: '.format(i=i*10, j=(i+1)*10-1) + str([db2dec(x) for x in range(i*10, (i+1)*10)]) + '\n')

#for i in range(9):
#    stderr.write(str(i) +" => " + str(dec2db(i)) + '\n')

def decibinaryNumbers(x):
    k = 0
    while k < x:
        pass

#if __name__ == "__main__":
#    for _ in range(int(stdin.readline().rstrip())):
#        x = int(stdin.readline().rstrip())
#        ans = decibinaryNumbers(x)
#        stdout.write(str(ans) + '\n')
