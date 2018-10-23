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

def largest_rectangle(heights):
    n = len(heights)
    stack, result = [], 0
    for i in range(n):
        # hr, ir => the height and position of the right side
        # il => the position of the left side so that stack[:][0] < height[il]
        hr, ir, il = heights[i], i, i
        # maintain invariant
        while stack and stack[-1][0] >= hr:
            # compute the area of rectangle:
            #           __
            #         __
            #       __
            #    ___.......
            #    |hl      |
            #    |        |__
            #    |  here! |hr
            #    |        |
            #=================
            #     il       ir
            hl, il = stack.pop()
            area = hl * (ir - il)
            result = max(result, area)
        # push the current height to the stack
        #    __
        #    hl
        #    __.......__
        #  __hr       hr
        #
        #  ===============
        #    il       ir
        stack.append((hr, il))
    # clean the stack to compute rectangles as if hr = 0 at ir = n
    for h, i in stack:
        area = h * (n - i)
        result = max(result, area)
    return result
