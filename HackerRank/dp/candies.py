# https://www.hackerrank.com/challenges/candies/problem
#
# Hint: Dynamic Programming
#
# suppose a[0:n] is non-decreasing
#
# m[i] => the cost at a[i]
#
# m[i] = m[i-1] + 1                  if a[i-1] < a[i]
#      = 1                           if a[i-1] = a[i]
#      = 1                           if i = 0
#      = 1                           otherwise
#
# then generalize m[i] to allow increasing and decreasing
#
# m1[i] = m1[i-1] + 1       (forward direction)
# m2[i] = m2[i+1] - 1       (reverse direction)
# m[i] = max(m1[i], m2[i])
#
# then answer = sum(m[:])
#
# case 1: [10 10 10 10 10] => [1 1 1 1 1]
# case 2: [10 9 8 7 6] => [5 4 3 2 1]
# case 3: [1 2 2] => [1 2 1]
# case 4: [5 6 7 8 9] => [1 2 3 4 5]
# case 5: [5 6 6 8 9] => [1 2 1 2 3]
# case 6: [1 2 4 3 2 1] => [1 2 4 3 2 1]
# case 7: [1 2 4 4 3 2 1] => [1 2 3 4 3 2 1]
# case 8: [2 4 2 6 1 7 8 9 2 1] => [1 2 1 2 1 2 3 4 2 1]
# case 9: [2 4 3 5 2 6 4 5] => [1 2 1 2 1 2 1 2]

from sys import stdin, stdout, stderr

def candies(n, arr):
    m1 = [0] * n
    m2 = [0] * n
    m1[0] = 1
    m2[-1] = 1
    for i in range(1,n):
        if arr[i-1] < arr[i]:
            m1[i] = m1[i-1] + 1
        elif arr[i-1] == arr[i]:
            m1[i] = 1
        else:
            m1[i] = 1
    for i in range(n-2,-1,-1):
        if arr[i+1] < arr[i]:
            m2[i] = m2[i+1] + 1
        elif arr[i+1] == arr[i]:
            m2[i] = 1
        else:
            m2[i] = 1
    stderr.write("arr: " + ' '.join(map(str, arr)) + '\n')
    stderr.write("m1: " + ' '.join(map(str, m1)) + '\n')
    stderr.write("m2: " + ' '.join(map(str, m2)) + '\n')
    return sum(map(lambda x: max(x), zip(m1, m2)))

if __name__ == "__main__":
    n = int(stdin.readline().rstrip())
    arr = [int(stdin.readline().rstrip()) for _ in range(n)]
    ans = candies(n, arr)
    stdout.write(str(ans) + '\n')
