from sys import stdin, stdout, stderr
from array import array

def subranges(n):
    for i in range(n):
        for j in range(i+1, n):
            yield (i, j+1)

A = ord('a')

def analysis1(s, i, j):
    buck = array('i', [0] * 26)
    for i in range(i, j):
        buck[s[i]] += 1
    return buck

def sherlockAndAnagrams(s):
    n = len(s)
    count = 0
    # compute single word anagram
    for b in analysis1(s, 0, n):
        count += b * (b-1) // 2
    #
    anagrams = [
        (j-i, analysis1(s, i, j))
        for i, j in subranges(n)
            if (j-i) != n and (j-i) != 1
    ]
    #
    stderr.write('precomputed\n')
    #
    m = len(anagrams)
    for i in range(m):
        for j in range(i+1, m):
            if anagrams[i][0] == anagrams[j][0]:
                if anagrams[i][1] == anagrams[j][1]:
                    count += 1
    return count

def sherlockAndAnagrams2(s):
    count = 0
    d = {}
    for i in range(len(s)):
        for j in range(len(s) - i):
            s1 = ''.join(sorted(s[j:j + i + 1]))
            d[s1] = d.get(s1, 0) + 1
    for key in d:
        count += (d[key] - 1) * d[key] // 2
    return count

if __name__ == "__main__":
    for _ in range(int(stdin.readline().rstrip())):
        s = stdin.readline().rstrip()
        #s = array('i', map(lambda x: ord(x) - A, s))
        ans = sherlockAndAnagrams2(s)
        stdout.write(str(ans) + '\n')
