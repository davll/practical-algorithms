class Solution:
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        tmp1 = [0] * (rowIndex+1)
        tmp2 = tmp1[:]
        tmp1[0] = 1
        for i in range(1,rowIndex+1):
            tmp2[0] = tmp1[0]
            tmp2[i] = tmp1[i-1]
            for j in range(1,i):
                tmp2[j] = tmp1[j-1] + tmp1[j]
            tmp1, tmp2 = tmp2, tmp1
        return tmp1
