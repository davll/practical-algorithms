# Fibonacci Sequence
#
# f(n) = 0                if n = 0
#        1                if n = 1
#        f(n-1)+f(n-2)    if n > 1
#

def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a+b

if __name__ == "__main__":
    it = fibonacci()
    for _ in range(10):
        print(str(next(it)))
