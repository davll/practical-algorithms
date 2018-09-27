# find key in arr[start:end] (not including arr[end])
def binary_search(arr, start, end, key):
    if end > start:
        mid = (start + end - 1) // 2
        if key == arr[mid]:
            return mid
        else if key < arr[mid]:
            return binary_search(arr, start, mid, key)
        else:
            return binary_search(arr, mid+1, end, key)
    else:
        return -1

# References:
# Python: bisect in standard library
# https://ai.googleblog.com/2006/06/extra-extra-read-all-about-it-nearly.html
