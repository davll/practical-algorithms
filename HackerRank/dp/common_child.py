# https://www.hackerrank.com/challenges/common-child/problem

# Hint: LCS

from sys import stdin, stdout

# Complete the commonChild function below.
def commonChild(s1, s2):
    s1 = list(map(ord, s1))
    s2 = list(map(ord, s2))
    m, n = len(s1), len(s2)
    #lcs = [[0] * (n+1) for _ in range(m+1)]
    lcs1 = [0] * (n+1)
    lcs2 = lcs1[:]
    for i in range(1,m+1):
        for j in range(1,n+1):
            if s1[i-1] == s2[j-1]:
                lcs2[j] = lcs1[j-1] + 1
                #lcs[i][j] = lcs[i-1][j-1] + 1
            else:
                lcs2[j] = max(lcs1[j], lcs2[j-1])
                #lcs[i][j] = max(lcs[i-1][j], lcs[i][j-1])
        lcs1, lcs2 = lcs2, lcs1
    return lcs1[n]
    #return lcs[m][n]

if __name__ == '__main__':
    s1 = stdin.readline()
    s2 = stdin.readline()
    result = commonChild(s1, s2)
    stdout.write(str(result)+'\n')
