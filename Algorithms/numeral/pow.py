def pow(x, y):
    a = 1
    while y > 0:
        if y & 0x1 == 1:
            a *= x
        x, y = x*x, y>>1
    return a
