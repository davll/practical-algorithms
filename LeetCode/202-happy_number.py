# https://leetcode.com/problems/happy-number/

def is_happy_v1(n):
    if n < 1:
        return False
    used = set([n])
    while n != 1:
        m = 0
        while n > 0:
            m += (n % 10) ** 2
            n = n // 10
        n = m
        if n in used:
            return False
        used.add(n)
    return True

# Tortoise-Hare Algorithm
def is_happy_v2(n):
    def advance(x):
        m = 0
        while x > 0:
            m += (x % 10) ** 2
            x = x // 10
        return m
    slow, fast = n, n
    while slow != 1 and fast != 1:
        slow = advance(slow)
        fast = advance(advance(fast))
        if slow == fast:
            break
    return slow == 1 or fast == 1

class Solution:
    def isHappy(self, n: int) -> bool:
        return is_happy_v2(n)
