# Bubble Sort

def bubblesort(a):
    """
    Sort an array inplace with bubble sorting algorithm

    - Worst case: O(n^2) comparisons, O(n^2) swaps
    - Avg case: O(n^2) comparisons, O(n^2) swaps
    - Best case: O(n) comparisons, O(1) swaps
    - Worst case space: O(1) auxiliary
    """
    n = len(a)
    for _ in range(n):
        for i in range(n-1):
            if a[i] > a[i+1]:
                a[i], a[i+1] = a[i+1], a[i]
