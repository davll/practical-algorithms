# Window sliding

def previous_smaller(arr):
    # prev[i] = index of previous element that is smaller than arr[i]
    # => likewise, all elements in arr[prev[i]+1:i] are greater or equal to arr[i]
    n = len(arr)
    stack = []
    prev = [-1] * n
    for i in range(n):
        while stack and arr[stack[-1]] >= arr[i]:
            stack.pop()
        if stack:
            prev[i] = stack[-1]
        stack.append(i)
    return prev

def next_smaller(arr):
    # right[i] = index of next element that is smaller than arr[i]
    # => likewise, all elements in arr[i+1:right[i]] are greater or equal to arr[i]
    n = len(arr)
    stack = []
    right = [n] * n
    for i in reversed(range(n)):
        while stack and arr[stack[-1]] >= arr[i]:
            stack.pop()
        if stack:
            right[i] = stack[-1]
        stack.append(i)
    return right
