# https://leetcode.com/problems/multiply-strings/

from array import array

# result += (xs * scale * (10 ^ shift)) where scale = 0..9
def scaled_shifted_add(result, xs, scale, shift):
    if scale == 0:
        return
    carry = 0
    j = shift
    for i, x in enumerate(xs):
        j = i + shift
        if j >= len(result):
            result += [0] * (j - len(result) + 1)
        tmp = carry + result[j] + x * scale
        result[j] = tmp % 10
        carry = tmp // 10
    j += 1
    while carry > 0:
        if j >= len(result):
            result += [0] * (j - len(result) + 1)
        tmp = carry + result[j]
        result[j] = tmp % 10
        carry = tmp // 10

def mult_v1(num1, num2):
    result = [0]
    for i, x in enumerate(num1):
        scaled_shifted_add(result, num2, x, i)
    while len(result) > 1 and result[-1] == 0:
        result.pop()
    return result

class Solution:
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        num1 = array('i', map(int, reversed(num1)))
        num2 = array('i', map(int, reversed(num2)))
        result = mult_v1(num1, num2)
        return ''.join(map(str, reversed(result)))
