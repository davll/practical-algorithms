# https://www.geeksforgeeks.org/k-th-element-two-sorted-arrays/

# T = O(k)
def kth_v1(l1, l2, k):
    """
    l1: [T] => an ascending sorted array
    l2: [T] => an ascending sorted array
    k: int => 0 indexed. ex: k = 0 for 1st element
    return: T => the k-th element of the final sorted array
    """
    i, j, m, n = 0, 0, len(l1), len(l2)
    while k > 0 and i < m and j < n:
        if l1[i] < l2[j]:
            i, k = i+1, k-1
        else:
            j, k = j+1, k-1
    if k > 0 and i < m:
        i, k = i+k, 0
    if k > 0 and j < n:
        j, k = j+k, 0
    if i < m and j < n:
        return min(l1[i], l2[j])
    elif i < m:
        return l1[i]
    else:
        return l2[j]
