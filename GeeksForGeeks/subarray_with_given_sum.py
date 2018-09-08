# https://practice.geeksforgeeks.org/problems/subarray-with-given-sum/

def find_subarray(arr, sum):
    i, j, n = 0, 0, len(arr)
    x = arr[0]
    while i < n and j < n:
        if x == sum:
            return (i, j)
        elif x < sum:
            j += 1
            if j < n:
                x += arr[j]
        elif x > sum:
            x -= arr[i]
            i += 1
            if i > j:
                j = i
    return None

if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        N, S = map(int, input().split())
        A = list(map(int, input().split()))
        B = find_subarray(A, S)
        if not B:
            print("-1")
        else:
            print("%i %i" % (B[0]+1, B[1]+1))
