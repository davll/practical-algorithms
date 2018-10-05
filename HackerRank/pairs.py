from sys import stdin, stdout, stderr

def pairs(k, arr):
    n = len(arr)
    arr.sort()
    count = 0
    for i in range(n):
        for j in range(i+1, n):
            if arr[j] - arr[i] == k:
                count += 1
            elif arr[j] - arr[i] > k:
                break
    return count

if __name__ == "__main__":
    n, k = map(int, stdin.readline().rstrip().split())
    arr = list(map(int, stdin.readline().rstrip().split()))
    ans = pairs(k, arr)
    stdout.write(str(ans) + '\n')
