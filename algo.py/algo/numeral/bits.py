def set_bit(x, pos):
    return x | (1 << pos)

def unset_bit(x, pos):
    return x & ~(1 << pos)

def toggle_bit(x, pos):
    return x ^ (1 << pos)

def check_bit(x, pos):
    return bool((x >> pos) & 0x1)

def get_lsb(x):
    return x & (-x)

def unset_lsb(x):
    return x & (x-1)

def bitmask(n):
    return (1 << n) - 1

def left_rotate(x, d, bits=32):
    mask = bitmask(bits)
    return ((x << d) & mask) | (x >> (bits - d))

def right_rotate(x, d, bits=32):
    mask = bitmask(bits)
    return (x >> d) | ((x << (bits - d)) & mask)

def reverse_bits(x):
    y = 0
    while x > 0:
        y = (y << 1) | (x & 1)
        x = x >> 1
    return y

# https://www.geeksforgeeks.org/bits-manipulation-important-tactics/
# https://www.geeksforgeeks.org/bitwise-algorithms/
# https://www.geeksforgeeks.org/category/algorithm/bit-magic/
# https://www.geeksforgeeks.org/bitwise-hacks-for-competitive-programming/
