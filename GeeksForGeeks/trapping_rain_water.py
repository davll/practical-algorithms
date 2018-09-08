# https://practice.geeksforgeeks.org/problems/trapping-rain-water/

def compute_left_barriers(arr):
    n = len(arr)
    left = [0] * n
    curr_left = 0
    for i in range(1, n):
        if arr[i] >= arr[curr_left]:
            curr_left = i
        left[i] = curr_left
    return left

def compute_right_barriers(arr):
    n = len(arr)
    right = [n-1] * n
    curr_right = n-1
    for i in range(n-2,-1,-1):
        if arr[i] >= arr[curr_right]:
            curr_right = i
        right[i] = curr_right
    return right

def trap_water(arr):
    left = compute_left_barriers(arr)
    right = compute_right_barriers(arr)
    #print("left = " + str(left))
    #print("right = " + str(right))
    result = 0
    n = len(arr)
    for i in range(n):
        h = min(arr[left[i]], arr[right[i]])
        result += max(0, h - arr[i])
    return result

if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        N = int(input())
        A = list(map(int, input().split()))
        water = trap_water(A)
        print(str(water))
