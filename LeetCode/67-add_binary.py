def sol1(a, b):
    a = int(a, base=2)
    b = int(b, base=2)
    return format(a+b, 'b')

def sol2(a, b):
    if len(a) > len(b):
        a, b = b, a
    i, j, k = len(a)-1, len(b)-1, 0
    result = [0] * max(len(a), len(b))
    carry = 0
    while i >= 0 and j >= 0:
        tmp = int(a[i]) + int(b[j]) + carry
        result[k] = tmp % 2
        carry = tmp // 2
        i, j, k = i-1, j-1, k+1
    while j >= 0:
        tmp = int(b[j]) + carry
        result[k] = tmp % 2
        carry = tmp // 2
        j, k = j-1, k+1
    if carry > 0:
        result.append(carry)
    return ''.join(map(str, reversed(result)))

class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        return sol2(a, b)
