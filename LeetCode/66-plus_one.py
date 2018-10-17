class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        n, carry = len(digits), 1
        for i in range(n-1,-1,-1):
            tmp = carry + digits[i]
            digits[i] = tmp % 10
            carry = tmp // 10
        if carry != 0:
            return [carry] + digits
        else:
            return digits
